# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)

from mkdocs.plugins import BasePlugin
import bleach
from .config import (SAFE_PLUGIN_CONFIG_SCHEME,
                     SafeTextPluginConfig)


class SafeTextPlugin(BasePlugin):
    config_scheme = SAFE_PLUGIN_CONFIG_SCHEME

    def __init__(self):
        pass

    def on_config(self, config):
        self.plugin_config = SafeTextPluginConfig(self.config)

        return config

    def on_page_markdown(self, markdown, page, config, site_navigation):
        return markdown

    def on_page_content(self, html, page, config, site_navigation):
        return bleach.clean(html,
                            tags=self.plugin_config.markdown_tags,
                            attributes=self.plugin_config.markdown_attrs)

    def on_page_context(self, context, page, config, site_navigation):
        return context
