# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)
import copy

from mkdocs.config import config_options
from bleach_whitelist.bleach_whitelist import (
    markdown_tags as whitelist_markdown_tags,
    markdown_attrs as whitelist_markdown_attrs
)


SAFE_PLUGIN_CONFIG_SCHEME = (
    ('append_allowed_tags', config_options.Type(list, default=[])),
    ('remove_allowed_tags', config_options.Type(list, default=[])),
    ('allowed_attrs', config_options.Type(dict, default={})),
)


class SafeTextPluginConfig(object):
    markdown_tags = copy.deepcopy(whitelist_markdown_tags)
    markdown_attrs = copy.deepcopy(whitelist_markdown_attrs)

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
