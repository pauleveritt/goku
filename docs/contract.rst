========
Contract
========

What promises from `alabaster` (and `sphinx.themes.basic`) does `goku` keep vs. drop?

Most of these come from automated tests but it's more convenient to write them here.

Keep
====

- `custom.css` can be added after the theme CSS and pygments

Drop
====

`basic_layout.html`
-------------------

- ` old style sidebars: using blocks -- should be deprecated``

To Do
=====

*A place to keep track of discovered-contracts which need digestion.*

`basic_layout.html`
-------------------

- html5_doctype

- Various macros for sidebars, etc.

- New-style sidebars

- jstag()

- css_files

- html_tag

- html_baseurl and pageurl -> <link rel="canonical">

- use_opensearch

- Everything here: https://github.com/sphinx-doc/sphinx/blob/c4073eebc358e98912c7e1263dd61b6a87bd24bd/sphinx/builders/html.py#L459

- link prev/next

- block extrahead

- body_tag

- block header, relbar1, sidebar1

- document block

-