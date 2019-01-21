from pbr.version import VersionInfo

_v = VersionInfo('scopus').semantic_version()
__version__ = _v.release_string()
version_info = _v.version_tuple()

from .report import *
