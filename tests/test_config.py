# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et
from __future__ import (division, print_function,
                        absolute_import, unicode_literals)
import unittest

from bleach_whitelist.bleach_whitelist import (
    markdown_tags as whitelist_markdown_tags,
    markdown_attrs as whitelist_markdown_attrs
)
from mkdocssafetext.config import SafeTextPluginConfig


class TestSafeTextPlugin(unittest.TestCase):
    def setUp(self):
        pass

    def test_default_config_is_based_on_whitelist(self):
        config_is_nothing = {
            'append_allowed_tags': [],
            'remove_allowed_tags': [],
            'allowed_attrs': {},
        }
        plugin_config = SafeTextPluginConfig(config_is_nothing)

        self.assertEqual(plugin_config.markdown_tags,
                         whitelist_markdown_tags)
        self.assertEqual(plugin_config.markdown_attrs,
                         whitelist_markdown_attrs)

    def test_append_allowed_tags(self):
        config_append_allowed_tags = {
            'append_allowed_tags': ['video', 'audio'],
            'remove_allowed_tags': [],
            'allowed_attrs': {},
        }
        plugin_config = SafeTextPluginConfig(config_append_allowed_tags)

        self.assertIn('video', plugin_config.markdown_tags)
        self.assertIn('audio', plugin_config.markdown_tags)
        self.assertNotIn('undefined', plugin_config.markdown_tags)
        self.assertNotEqual(plugin_config.markdown_tags,
                            whitelist_markdown_tags)

    def test_remove_allowed_tags(self):
        config_remove_allowed_tags = {
            'append_allowed_tags': [],
            'remove_allowed_tags': ['ul', 'ol', 'li'],
            'allowed_attrs': {},
        }
        plugin_config = SafeTextPluginConfig(config_remove_allowed_tags)

        self.assertNotIn('ul', plugin_config.markdown_tags)
        self.assertNotIn('ol', plugin_config.markdown_tags)
        self.assertNotIn('li', plugin_config.markdown_tags)
        self.assertIn('h1', plugin_config.markdown_tags)
        self.assertNotEqual(plugin_config.markdown_tags,
                            whitelist_markdown_tags)

    def test_allowed_attrs(self):
        config_allowed_attrs = {
            'append_allowed_tags': [],
            'remove_allowed_tags': [],
            'allowed_attrs': {"img": ["src", "width", "height"]},
        }
        plugin_config = SafeTextPluginConfig(config_allowed_attrs)

        self.assertEqual(plugin_config.markdown_attrs,
                         config_allowed_attrs['allowed_attrs'])
        self.assertNotEqual(plugin_config.markdown_attrs,
                            whitelist_markdown_attrs)

    def test_str(self):
        config_is_nothing = {
            'append_allowed_tags': [],
            'remove_allowed_tags': [],
            'allowed_attrs': {},
        }
        plugin_config = SafeTextPluginConfig(config_is_nothing)

        printable_plugin = str(plugin_config)
        self.assertIn('tags:', printable_plugin)
        self.assertIn('attrs: ', printable_plugin)

    def tearDown(self):
        pass
