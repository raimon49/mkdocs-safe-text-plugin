# mkdocs-safe-text-plugin

[![Build Status](https://travis-ci.org/raimon49/mkdocs-safe-text-plugin.svg?branch=master)](https://travis-ci.org/raimon49/mkdocs-safe-text-plugin) [![PyPI version](https://badge.fury.io/py/mkdocs-safe-text-plugin.svg)](https://badge.fury.io/py/mkdocs-safe-text-plugin) [![Codecov](https://codecov.io/gh/raimon49/mkdocs-safe-text-plugin/branch/master/graph/badge.svg)](https://codecov.io/gh/raimon49/mkdocs-safe-text-plugin) [![BSD License](http://img.shields.io/badge/license-BSD-green.svg)](LICENSE) [![Requirements Status](https://requires.io/github/raimon49/mkdocs-safe-text-plugin/requirements.svg?branch=master)](https://requires.io/github/raimon49/mkdocs-safe-text-plugin/requirements/?branch=master)

Plugin for safe text editing with [MKDocs](http://www.mkdocs.org/).

## Table of Contents

 * [How does this plugin work?](#how-does-this-plugin-work)
 * [Installation](#installation)
 * [Plugin configuration](#plugin-configuration)
 * [License](#license)

## How does this plugin work?

Markdown is a very flexible format, and raw HTML is allowed. But it is unnecessary in multiple-person text editing.

When raw HTML like `<font>` tag is used in MKDocs, it is rendered as it is.

![No escaped font](https://user-images.githubusercontent.com/221802/35481481-ac9e4894-0467-11e8-89ab-47ca5037d9d2.png)

If you use this plug-in with MKDocs, tags that are not allowed in the whitelist are escaped.

![Escaped font](https://user-images.githubusercontent.com/221802/35481484-b268e02c-0467-11e8-8b7a-c3c7232312ed.png)

## Installation

Install it via PyPI using `pip` command.

```console
$ pip install mkdocs-safe-text-plugin
```

And add it to your `mkdocs.yml` file.

```yaml
plugins:
  - mkdocs_safe_text
```

An example of use can be checked by [example/basic-usage](examples/basic-usage).

## Plugin configuration

This plugin works with the HTML tag element for Markdown defined by [bleach-whitelist](https://github.com/yourcelf/bleach-whitelist/blob/master/bleach_whitelist/bleach_whitelist.py) enabled. This implementation approach is recommended in [the Python-Markdown release notes](https://python-markdown.github.io/change_log/release-2.6/).

And user can change this setting.

```yaml
plugins:
  - mkdocs_safe_text:
      append_allowed_tags:
        - tag1
        - tag2
      remove_allowed_tags:
        - tag3
        - tag4
      allowed_attrs:
        tag5:
          - attribute1
          - attribute2
```

An example of use can be checked by [example/customization-usage](examples/customization-usage).

## License

[BSD 2-Clause License](LICENSE)
