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
from mkdocs.plugins import BasePlugin
import bleach
from .config import (SAFE_PLUGIN_CONFIG_SCHEME,
                     SafeTextPluginConfig)


class SafeTextPlugin(BasePlugin):
    config_scheme = SAFE_PLUGIN_CONFIG_SCHEME

    def on_config(self, config):
        self.plugin_config = SafeTextPluginConfig(self.config)

        return config

    def on_page_content(self, html, **kwargs):
        return bleach.clean(html,
                            tags=self.plugin_config.markdown_tags,
                            attributes=self.plugin_config.markdown_attrs)
