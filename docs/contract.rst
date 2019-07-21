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

-

Drop
====

``theme.conf`` settings
-----------------------

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

`basic_layout.html`
-------------------

- ` old style sidebars: using blocks -- should be deprecated``

To Do
=====

*A place to keep track of discovered-contracts which need digestion.*

``basic_layout.html``
---------------------

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


Alabaster ``layout.html``
-------------------------

- theme_touch_icon

- relbar stuff

- theme_github_banner

- genindex etc.

``alabaster.css_t``
-------------------
