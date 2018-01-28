# mkdocs-safe-text-plugin

[![Build Status](https://travis-ci.org/raimon49/mkdocs-safe-text-plugin.svg?branch=master)](https://travis-ci.org/raimon49/mkdocs-safe-text-plugin)
[![PyPI version](https://badge.fury.io/py/mkdocs-safe-text-plugin.svg)](https://badge.fury.io/py/mkdocs-safe-text-plugin)
[![Codecov](https://codecov.io/gh/raimon49/mkdocs-safe-text-plugin/branch/master/graph/badge.svg)](https://codecov.io/gh/raimon49/mkdocs-safe-text-plugin)
[![BSD License](http://img.shields.io/badge/license-BSD-green.svg)](LICENSE)

Plugin for safe text editing with [MKDocs](http://www.mkdocs.org/).

## How does this plugin work?

Markdown is a very flexible format, and raw HTML is allowed. But it is unnecessary in multiple-person text editing.

When raw HTML like `<font>` tag is used in MKDocs, it is rendered as it is.

If you use this plug-in with MKDocs, tags that are not allowed in the whitelist are escaped.

## Installation

Install it via PyPI using `pip` command.

```console
$ pip install mkdocs-safe-text-plugin
```
