# coding=utf-8
"""
Quote `a` and `img` tags. Eg. <a href=index.html> to <a href="index.html">

`href` and `src` attribute of `a` and `img` tags respectively do not have
quoted values, so html2rest does not pick them up.
"""

import re
import os
from os.path import exists, join as pathjoin, dirname, basename

rx_href = re.compile(r'(?P<top><(a|img) .*?)(?P<attr>href|src)=(?P<href>[^"].+?)(?P<tail>[>\s])')
def on_href_match(m):
    return '%s%s="%s"%s' % (m.group('top'), m.group('attr'), m.group('href'), m.group('tail'))

for f in os.listdir('.'):
    if f.endswith('.html'):
        tmp_name = f + '.tmp'
        with open(f) as orig:
            with open(tmp_name, 'wb') as update:
                for line in orig:
                    update.write(rx_href.sub(on_href_match, line))
        os.rename(tmp_name, f)

