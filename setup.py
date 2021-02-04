# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et
"""
mkdocs-safe-text-plugin

BSD 2-Clause License

Copyright (c) 2018, raimon
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import os
from setuptools import setup, find_packages

from mkdocssafetext import (__version__ as VERSION, __author__ as AUTHOR,
                            __license__ as LICENSE)


def read_file(filename):
    basepath = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(basepath, filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    else:
        return ''


LONG_DESC = ''
try:
    from pypandoc import convert_file

    about_this = convert_file('README.md', 'rst', format='markdown_github')
    separate = '\n\n'
    change_log = convert_file('CHANGELOG.md', 'rst', format='markdown_github')

    LONG_DESC = about_this + separate + change_log
except (IOError, ImportError):
    LONG_DESC = read_file('README.md')


setup(
    version=VERSION,
    long_description=LONG_DESC,
    author=AUTHOR,
    license=LICENSE,
    entry_points={
        'mkdocs.plugins': [
            'mkdocs_safe_text = mkdocssafetext.plugin:SafeTextPlugin',
        ]
    }
)
