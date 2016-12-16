# -*- coding: utf-8 -*-
import sys

PY2 = sys.version_info[0] == 2


if not PY2:
    from urllib.parse import urlencode
    from urllib.request import urlopen, Request
else:
    from urllib import urlencode
    from urllib2 import urlopen, Request


__all__ = ['urlencode', 'urlopen', 'Request']
