from collections import Counter, defaultdict
from operator import itemgetter

import matplotlib.pyplot as plt
from scholarmetrics import hindex
from scopus import AbstractRetrieval, AuthorRetrieval, ScopusSearch


def get_subject_docs(identifier, refresh):
    """Returns (subject area, number of documents)-tuples."""
    au = AuthorRetrieval(identifier, refresh=refresh)
    docs = dict(au.classificationgroup)
    names = [(p.area, docs[p.code]) for p in au.subject_areas]
    names.sort(reverse=True, key=itemgetter(1))
    return names


def report(query, label, refresh=True):
    """Print out an org-mode report for search results.

    Parameters
    ----------
    query : str
        The search query based on which results the report should be
        generated.

    label : str
        The label used in the document title ("Report for ...").

    refresh : bool (optional, default=True)
        Whether to refresh a cached file containing results of a previous
        query or not.
    """
    # Header
    print('*** Report for {}\n'.format(label))
    print('#+attr_latex: :placement [H] :center nil')

    # Perform query
    s = ScopusSearch(query, refresh=refresh)
    journal_res = [p for p in s.results if p.aggregationType == "Journal"]

    # Parse results
    doc_types = Counter([p.aggregationType for p in s.results])
    paper_cites = {(p.title, p.doi): int(p.citedby_count) for p in journal_res}
    Ncites = sum(paper_cites.values())
    papers = len(journal_res)
    author_count = [len(p.authid.split(";")) for p in journal_res]
    au_counts = defaultdict(lambda: 0)
    j_counts = defaultdict(lambda: 0)
    for p in journal_res:
        for auth in zip(p.authname.split(";"), p.authid.split(";")):
            key = (auth[0], auth[1])
            au_counts[key] += 1
        jkey = (p.publicationName, p.source_id, p.issn)
        j_counts[jkey] += 1

    # Document information
    print('#+caption: Types of documents found for {}.'.format(label))
    print('| Document type | count |\n|-')
    for key, value in doc_types.items():
        print('| {} | {} |'.format(key, value))

    print('\n\n{} articles ({} citations) '
          'found by {} authors'.format(papers, Ncites, len(au_counts)))

    # Author counts {(name, scopus-id): count}
    auth_url = "[[https://www.scopus.com/authid/detail.uri?authorId={}][{}]]"
    view = [(auth_url.format(k[1], k[0]), v, k[1])
            for k, v in au_counts.items()]
    view.sort(reverse=True, key=itemgetter(1))
    print('\n#+attr_latex: :placement [H] :center nil')
    print('#+caption: Author publication counts for {0}.'.format(label))
    print('| name | count | categories |\n|-')
    for name, count, identifier in view[:20]:
        cats = ', '.join(['{} ({})'.format(cat[0], cat[1])
                          for cat in get_subject_docs(identifier, refresh)[0:3]])
        print('| {} | {} | {} |'.format(name, count, cats))

    # Journal information
    jour_url = '[[https://www.scopus.com/source/sourceInfo.url?sourceId={}][{}]]'
    jview = [(jour_url.format(k[1], k[0][0:50]), k[1], k[2], v)
             for k, v in j_counts.items()]
    jview.sort(reverse=True, key=itemgetter(3))
    print('\n\n#+attr_latex: :placement [H] :center nil')
    print('#+caption: Journal publication counts for {}.'.format(label))
    print('| Journal | count |\n|-')
    for journal, sid, issn, count in jview[0:12]:
        print('| {} | {} |'.format(journal, count))

    # Top cited papers
    pview = [('[[{}][{}]]'.format(k[1], k[0][0:60]), int(v))
             for k, v in paper_cites.items()]
    pview.sort(reverse=True, key=itemgetter(1))
    h_index = hindex([p[1] for p in pview])
    print('\n\n#+attr_latex: :placement [H] :center nil')
    print('#+caption: Top cited publication'
          ' counts for {}. h-index = {}.'.format(label, h_index))
    print('| title | cite count |\n|-')
    for title, count in pview[0:10]:
        print('| {} | {} |'.format(title, count))

    # Plot authors per publication
    plt.figure()
    plt.hist(author_count, 20)
    plt.xlabel('# authors')
    plt.ylabel('frequency')
    plt.savefig('{}-nauthors-per-publication.png'.format(label))

    # Bibliography
    print('\n\n#+caption: Number of authors '
          'on each publication for {}.'.format(label))
    print('[[./{}-nauthors-per-publication.png]]'.format(label))
    print('''**** Bibliography  :noexport:
     :PROPERTIES:
     :VISIBILITY: folded
     :END:''')
    for i, p in enumerate(journal_res):
        abstract = AbstractRetrieval(p.eid)
        print('{}. {}\n'.format(i + 1, abstract))
