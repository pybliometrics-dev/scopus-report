Examples
========

report
------

This class provides a function to generate a report using results from a Scopus query.  It outputs text in `Emacs org-format <http://orgmode.org/>`_.

*reports* summarizes the results in a variety of ways, such as the number of hits, which journals they are published in, who the coauthors are, their affiliations (here *reports* makes use of potentially cached author and affiliation views), how many times the articles have been cited.

.. code-block:: python
   
    >>> from scopusreport import report
    >>> query = 'FIRSTAUTH ( kitchin  j.r. )'
    >>> report(query, 'Kitchin - first author')
    *** Report for Kitchin - first author

    #+attr_latex: :placement [H] :center nil
    #+caption: Types of documents found for Kitchin - first author.
    | Document type | count |
    |-
    | Journal | 11 |
    | Conference Proceeding | 1 |


    11 articles (1861 citations) found by 12 authors

    #+attr_latex: :placement [H] :center nil
    #+caption: Author publication counts for Kitchin - first author.
    | name | count | categories |
    |-
    | [[https://www.scopus.com/authid/detail.uri?authorId=7004212771][Kitchin J.]] | 11 | Electronic, Optical and Magnetic Materials (9), Surfaces and Interfaces (9), Physics and Astronomy (all) (9) |
    | [[https://www.scopus.com/authid/detail.uri?authorId=7005171428][Barteau M.]] | 5 | Catalysis (83), Surfaces and Interfaces (81), Condensed Matter Physics (80) |
    | [[https://www.scopus.com/authid/detail.uri?authorId=7501891385][Chen J.]] | 5 | Physics and Astronomy (miscellaneous) (9), Chemistry (all) (80), Condensed Matter Physics (80) |
    | [[https://www.scopus.com/authid/detail.uri?authorId=7007042214][Nørskov J.]] | 3 | Chemistry (miscellaneous) (9), Nuclear Energy and Engineering (9), Physics and Astronomy (all) (85) |
    | [[https://www.scopus.com/authid/detail.uri?authorId=50761335600][Van Gulick A.]] | 1 | Cognitive Neuroscience (3), Experimental and Cognitive Psychology (3), Arts and Humanities (miscellaneous) (2) |
    | [[https://www.scopus.com/authid/detail.uri?authorId=55755405700][Zilinski L.]] | 1 | Library and Information Sciences (7), Information Systems (4), Computer Science (all) (1) |
    | [[https://www.scopus.com/authid/detail.uri?authorId=35514271900][Gellman A.]] | 1 | Physical and Theoretical Chemistry (90), Biochemistry (9), Surfaces and Interfaces (74) |
    | [[https://www.scopus.com/authid/detail.uri?authorId=7006349643][Reuter K.]] | 1 | Energy (all) (8), Physics and Astronomy (all) (73), Condensed Matter Physics (64) |
    | [[https://www.scopus.com/authid/detail.uri?authorId=7102229641][Scheffler M.]] | 1 | Electronic, Optical and Magnetic Materials (93), Physical and Theoretical Chemistry (76), Hardware and Architecture (7) |
    | [[https://www.scopus.com/authid/detail.uri?authorId=7401797491][Khan N.]] | 1 | Physical and Theoretical Chemistry (7), Surfaces and Interfaces (4), Catalysis (4) |
    | [[https://www.scopus.com/authid/detail.uri?authorId=6602686751][Yakshinskiy B.]] | 1 | Applied Mathematics (9), Computer Science Applications (9), Physics and Astronomy (miscellaneous) (8) |
    | [[https://www.scopus.com/authid/detail.uri?authorId=35477902900][Madey T.]] | 1 | Process Chemistry and Technology (9), Instrumentation (8), Chemistry (all) (8) |


    #+attr_latex: :placement [H] :center nil
    #+caption: Journal publication counts for Kitchin - first author.
    | Journal | count |
    |-
    | [[https://www.scopus.com/source/sourceInfo.url?sourceId=12284][Surface Science]] | 3 |
    | [[https://www.scopus.com/source/sourceInfo.url?sourceId=11000153773][Physical Review B - Condensed Matter and Materials]] | 2 |
    | [[https://www.scopus.com/source/sourceInfo.url?sourceId=145200][International Journal on Digital Libraries]] | 1 |
    | [[https://www.scopus.com/source/sourceInfo.url?sourceId=16275][AIChE Journal]] | 1 |
    | [[https://www.scopus.com/source/sourceInfo.url?sourceId=19700188320][ACS Catalysis]] | 1 |
    | [[https://www.scopus.com/source/sourceInfo.url?sourceId=16377][Catalysis Today]] | 1 |
    | [[https://www.scopus.com/source/sourceInfo.url?sourceId=29150][Physical Review Letters]] | 1 |
    | [[https://www.scopus.com/source/sourceInfo.url?sourceId=28134][Journal of Chemical Physics]] | 1 |


    #+attr_latex: :placement [H] :center nil
    #+caption: Top cited publication counts for Kitchin - first author. h-index = 8.
    | title | cite count |
    |-
    | [[10.1063/1.1737365][Modification of the surface electronic and chemical properti]] | 732 |
    | [[10.1103/PhysRevLett.93.156801][Role of strain and ligand effects in the modification of the]] | 682 |
    | [[10.1016/j.cattod.2005.04.008][Trends in the chemical properties of early transition metal ]] | 141 |
    | [[10.1016/j.susc.2003.09.007][Elucidation of the active surface and origin of the weak met]] | 127 |
    | [[10.1103/PhysRevB.77.075437][Alloy surface segregation in reactive environments: First-pr]] | 84 |
    | [[10.1103/PhysRevB.79.205412][Correlations in coverage-dependent atomic adsorption energie]] | 50 |
    | [[10.1016/S0039-6028(02)02679-1][A comparison of gold and molybdenum nanoparticles on TiO<inf]] | 31 |
    | [[10.1021/acscatal.5b00538][Examples of effective data sharing in scientific publishing]] | 8 |
    | [[10.1002/aic.15294][High-throughput methods using composition and structure spre]] | 3 |
    | [[10.1016/j.susc.2015.05.007][Data sharing in Surface Science]] | 2 |


    #+caption: Number of authors on each publication for Kitchin - first author.
    [[./Kitchin - first author-nauthors-per-publication.png]]
    **** Bibliography  :noexport:
         :PROPERTIES:
         :VISIBILITY: folded
         :END:
    1. [[https://www.scopus.com/inward/record.uri?partnerID=HzOxMe3b&scp=85019169906&origin=inward][2-s2.0-85019169906]]  John R. Kitchin, Ana E. Van Gulick and Lisa D. Zilinski, Automating data sharing through authoring tools, International Journal on Digital Libraries, 18(2), pp. 93-98, (2017). https://doi.org/10.1007/s00799-016-0173-7, https://www.scopus.com/inward/record.uri?partnerID=HzOxMe3b&scp=85019169906&origin=inward, cited 1 times (Scopus).
      Affiliations:
       Carnegie Mellon University

    2. [[https://www.scopus.com/inward/record.uri?partnerID=HzOxMe3b&scp=84971324241&origin=inward][2-s2.0-84971324241]]  John R. Kitchin and Andrew J. Gellman, High-throughput methods using composition and structure spread libraries, AIChE Journal, 62(11), pp. 3826-3835, (2016). https://doi.org/10.1002/aic.15294, https://www.scopus.com/inward/record.uri?partnerID=HzOxMe3b&scp=84971324241&origin=inward, cited 3 times (Scopus).
      Affiliations:
       Carnegie Mellon University

    3. [[https://www.scopus.com/inward/record.uri?partnerID=HzOxMe3b&scp=84930349644&origin=inward][2-s2.0-84930349644]]  John R. Kitchin, Data sharing in Surface Science, Surface Science, 647, pp. 103-107, (2016). https://doi.org/10.1016/j.susc.2015.05.007, https://www.scopus.com/inward/record.uri?partnerID=HzOxMe3b&scp=84930349644&origin=inward, cited 2 times (Scopus).
      Affiliations:
       Carnegie Mellon University

    4. [[https://www.scopus.com/inward/record.uri?partnerID=HzOxMe3b&scp=84930616647&origin=inward][2-s2.0-84930616647]]  John R. Kitchin, Examples of effective data sharing in scientific publishing, ACS Catalysis, 5(6), pp. 3894-3899, (2015). https://doi.org/10.1021/acscatal.5b00538, https://www.scopus.com/inward/record.uri?partnerID=HzOxMe3b&scp=84930616647&origin=inward, cited 8 times (Scopus).
      Affiliations:
       Carnegie Mellon University

    5. [[https://www.scopus.com/inward/record.uri?partnerID=HzOxMe3b&scp=67449106405&origin=inward][2-s2.0-67449106405]]  John R. Kitchin, Correlations in coverage-dependent atomic adsorption energies on Pd(111), Physical Review B - Condensed Matter and Materials Physics, 79(20), (no pages found) (2009). https://doi.org/10.1103/PhysRevB.79.205412, https://www.scopus.com/inward/record.uri?partnerID=HzOxMe3b&scp=67449106405&origin=inward, cited 50 times (Scopus).
      Affiliations:
       Carnegie Mellon University

    6. [[https://www.scopus.com/inward/record.uri?partnerID=HzOxMe3b&scp=40949100780&origin=inward][2-s2.0-40949100780]]  John R. Kitchin, Karsten Reuter and Matthias Scheffler, Alloy surface segregation in reactive environments: First-principles atomistic thermodynamics study of Ag3 Pd(111) in oxygen atmospheres, Physical Review B - Condensed Matter and Materials Physics, 77(7), (no pages found) (2008). https://doi.org/10.1103/PhysRevB.77.075437, https://www.scopus.com/inward/record.uri?partnerID=HzOxMe3b&scp=40949100780&origin=inward, cited 85 times (Scopus).
      Affiliations:
       Carnegie Mellon University
       Fritz Haber Institute of the Max Planck Society

    7. [[https://www.scopus.com/inward/record.uri?partnerID=HzOxMe3b&scp=20544467859&origin=inward][2-s2.0-20544467859]]  John R. Kitchin, Jens K. Nørskov, Mark A. Barteau and Jingguang G. Chen, Trends in the chemical properties of early transition metal carbide surfaces: A density functional study, Catalysis Today, 105(1 SPEC. ISS.), pp. 66-73, (2005). https://doi.org/10.1016/j.cattod.2005.04.008, https://www.scopus.com/inward/record.uri?partnerID=HzOxMe3b&scp=20544467859&origin=inward, cited 141 times (Scopus).
      Affiliations:
       Danmarks Tekniske Universitet
       University of Delaware

    8. [[https://www.scopus.com/inward/record.uri?partnerID=HzOxMe3b&scp=13444307808&origin=inward][2-s2.0-13444307808]]  J. R. Kitchin, J. K. Nørskov, M. A. Barteau and J. G. Chen, Role of strain and ligand effects in the modification of the electronic and chemical Properties of bimetallic surfaces, Physical Review Letters, 93(15), (no pages found) (2004). https://doi.org/10.1103/PhysRevLett.93.156801, https://www.scopus.com/inward/record.uri?partnerID=HzOxMe3b&scp=13444307808&origin=inward, cited 686 times (Scopus).
      Affiliations:
       Danmarks Tekniske Universitet
       University of Delaware

    9. [[https://www.scopus.com/inward/record.uri?partnerID=HzOxMe3b&scp=2942640180&origin=inward][2-s2.0-2942640180]]  J. R. Kitchin, J. K. Nørskov, M. A. Barteau and J. G. Chen, Modification of the surface electronic and chemical properties of Pt(111) by subsurface 3d transition metals, Journal of Chemical Physics, 120(21), pp. 10240-10246, (2004). https://doi.org/10.1063/1.1737365, https://www.scopus.com/inward/record.uri?partnerID=HzOxMe3b&scp=2942640180&origin=inward, cited 733 times (Scopus).
      Affiliations:
       Danmarks Tekniske Universitet
       University of Delaware

    10. [[https://www.scopus.com/inward/record.uri?partnerID=HzOxMe3b&scp=0141924604&origin=inward][2-s2.0-0141924604]]  John R. Kitchin, Neetha A. Khan, Mark A. Barteau, Jingguang G. Chen, Boris Yakshinskiy and Theodore E. Madey, Elucidation of the active surface and origin of the weak metal-hydrogen bond on Ni/Pt(1 1 1) bimetallic surfaces: A surface science and density functional theory study, Surface Science, 544(2-3), pp. 295-308, (2003). https://doi.org/10.1016/j.susc.2003.09.007, https://www.scopus.com/inward/record.uri?partnerID=HzOxMe3b&scp=0141924604&origin=inward, cited 127 times (Scopus).
      Affiliations:
       University of Delaware
       Rutgers, The State University of New Jersey

    11. [[https://www.scopus.com/inward/record.uri?partnerID=HzOxMe3b&scp=0037368024&origin=inward][2-s2.0-0037368024]]  John R. Kitchin, Mark A. Barteau and Jingguang G. Chen, A comparison of gold and molybdenum nanoparticles on TiO2(1 1 0) 1 × 2 reconstructed single crystal surfaces, Surface Science, 526(3), pp. 323-331, (2003). https://doi.org/10.1016/S0039-6028(02)02679-1, https://www.scopus.com/inward/record.uri?partnerID=HzOxMe3b&scp=0037368024&origin=inward, cited 31 times (Scopus).
      Affiliations:
       University of Delaware


After rendering, this yields

.. include:: report_example.rst
