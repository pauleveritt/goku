========
Contract
========

What promises from `alabaster` (and `sphinx.themes.basic`) does `goku` keep vs. drop?

Most of these come from automated tests but it's more convenient to write them here.

Keep
====

These all have tests asserting they should be there in goku.

- `custom.css` can be added after the theme CSS and pygments

``basic/theme.conf`` settings
-----------------------------

- html5_doctype

Basic
-----

- Everything here: https://github.com/sphinx-doc/sphinx/blob/c4073eebc358e98912c7e1263dd61b6a87bd24bd/sphinx/builders/html.py#L459

- Helper functions: www.sphinx-doc.org/en/master/templating.html#helper-functions

- Global and page variables: www.sphinx-doc.org/en/master/templating.html#global-variables

``alabaster/theme.conf`` settings
---------------------------------

- analytics_id, badge_branch, canonical_url, codecov_button, description, donate_url, extra_nav_links

- github: banner, button, count, repo, type, user

- logo and logo_name

- opencollective

- show_powered_by

- tidelift_url

- touch_icon

- travis_button

Alabaster Jinja2 blocks
-----------------------

- doctype

- extrahead

- relbar1

- relbar2

- content

- footer

Drop
====

``alabaster/theme.conf`` settings
---------------------------------

(Most things moved to SCSS)

- Litany of colors

- description_font_style

- fixed_sidebar

- gittip

- gratipay (couldn't find an actual usage of that knob)

- logo_text_align

- opencollective_button_color

- page_width

- relborder

- sidebar_width

``alabaster/layout.html`` blocks
--------------------------------

- Stuff inside ``theme_fixed_sidebar``

`basic_layout.html`
-------------------

- `` old style sidebars: using blocks -- should be deprecated``

To Do
=====

*A place to keep track of discovered-contracts which need digestion.*

``basic_layout.html``
---------------------

- Various macros for sidebars, etc.

- New-style sidebars

- js_tag()

- html_tag

- html_baseurl and pageurl -> <link rel="canonical">

- body_tag


Alabaster ``layout.html``
-------------------------

- genindex etc.

- use_opensearch


``alabaster.css_t``
-------------------
