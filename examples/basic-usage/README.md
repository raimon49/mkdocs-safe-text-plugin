# Examples: Basic usage

In this example, there is a configuration of the basic usage of the plugin.

## Plugin-less MKDocs

See [mkdocs.yml](mkdocs.yml). The following command will render MKDocs without plugin.

```console
$ mkdocs serve
```

## MKDocs with plugin

See [mkdocs\_with\_plugin.yml](mkdocs_with_plugin.yml). The following command executes MKDocs with plugin. The unwanted raw HTML tag in Markdown is escaped.

```console
$ mkdocs serve -f mkdocs_with_plugin.yml
```
