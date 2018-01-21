# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)
import copy

from mkdocs.plugins import BasePlugin
import bleach
from bleach_whitelist import markdown_tags, markdown_attrs


class SafeTextPlugin(BasePlugin):
    def __init__(self):
        self.markdown_tags = copy.deepcopy(markdown_tags)
        self.markdown_attrs = copy.deepcopy(markdown_attrs)

    def on_config(self, config):
        for cfg in config.user_configs:
            if isinstance(cfg, dict) and 'plugins' in cfg:
                self.plugin_config = cfg['plugins']

        return config

    def on_page_markdown(self, markdown, page, config, site_navigation):
        return markdown

    def on_page_content(self, html, page, config, site_navigation):
        return bleach.clean(html,
                            tags=self.markdown_tags,
                            attributes=self.markdown_attrs)

    def on_page_context(self, context, page, config, site_navigation):
        return context
