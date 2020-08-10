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
import copy

from mkdocs.config import config_options
from bleach_allowlist.bleach_allowlist import (
    markdown_tags as allowlist_markdown_tags,
    markdown_attrs as allowlist_markdown_attrs
)


SAFE_PLUGIN_CONFIG_SCHEME = (
    ('append_allowed_tags', config_options.Type(list, default=[])),
    ('remove_allowed_tags', config_options.Type(list, default=[])),
    ('allowed_attrs', config_options.Type(dict, default={})),
)


class SafeTextPluginConfig(object):
    markdown_tags = copy.deepcopy(allowlist_markdown_tags)
    markdown_attrs = copy.deepcopy(allowlist_markdown_attrs)

    def __init__(self, config):
        self._update_allowed_tags(config['append_allowed_tags'],
                                  config['remove_allowed_tags'])
        self._update_allowed_attrs(config['allowed_attrs'])

    def _update_allowed_tags(self, append_allowed_tags, remove_allowed_tags):
        updated_tags = set(self.markdown_tags)
        is_updated = False

        if len(append_allowed_tags) > 0:
            [updated_tags.add(tag) for tag in append_allowed_tags]
            is_updated = True

        if len(remove_allowed_tags) > 0:
            [updated_tags.discard(tag) for tag in remove_allowed_tags]
            is_updated = True

        if is_updated:
            self.markdown_tags = list(updated_tags)

    def _update_allowed_attrs(self, allowed_attrs):
        if len(allowed_attrs) == 0:
            return

        self.markdown_attrs = allowed_attrs

    def __str__(self):
        return ('tags: ' + str(self.markdown_tags) + '\n'
                'attrs: ' + str(self.markdown_attrs))
