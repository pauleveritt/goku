===================
Write Initial Tests
===================

*I resumed work on this 2019/06/29*

Sphinx doesn't really have good tests (I don't believe) for theming.
Based on prior work, I learned a lot about pytest and Sphinx fixtures.
Before re-implementing the universe, let's write a bunch of tests.

This document will be....long.


Clean Out Some Crud
===================

I've been away from goku for months.
Now that I care again, I need to do some chores on things whose untidiness bugs me:

- The `docs/conf.py` file has all the standard Sphinx noise in it.
  Clean out the noise (e.g. latex) but leave in the parts related to Alabaster and HTML theming.

- `sphinx_bulma.css_t` was still in static, change its name to `goku.css_t`

Failed: Speed Up Tests
======================

I wanted to have the "page" fixture only run once per test *class*.
I could then make each contract into a different test *method* for better granularity and pass/fail, without paying the price of parsing a page on every test.
Alas, no dice: the `app` fixture from sphinx is defined at function scope.
I could re-implement that, but it then depended on some other function-scoped fixtures, etc.

PyCharm Template Folder
=======================

I used "Mark As" to make `src/goku` a templates folder.


Basic, Seen Through Alabaster
=============================

The plan is for ``goku`` to fulfill the Alabaster contract.
Saying "the Alabaster contract" is actually saying "Alabaster extending Sphinx's basic theme", since Alabaster extends Basic.
As such, I'll start by examining ``sphinx.themes.basic`` and writing tests for all of its HTML, Jinja2 macros and blocks, conditionals, etc. but *as Alabaster uses those*.

Doctype test
============

Changed to be a standalone method, just testing one thing.
No testing at this point of replacement, just the `else` in the Jinja2 `if`.

``reldelim``
============

Hooray, it gets tricky.
My basic test root in ``tests/integration/sphinx/roots/test-basic-theme`` didn't generate any related things.
Why?
Because there was only one page.
How did I know that?
I fired up the "serve sphinx docs" http server and browsed to that magic directory.

Turns out my test root's ``conf.py`` wasn't using ``html_theme = 'goku'``.

Even funnier...Alabaster doesn't have a relbar by default.

CSS
===

The `css` macro inserts 3 ``<link>`` nodes in ``<head>``.
First is for the theme, second is for ``custom.css``, last is for pygments.

How I Do My TDD
===============

I develop Sphinx stuff a little differently: I use TDD. Not just because
tests are good. Rather, because it's a faster velocity of development.
Also, I tend to break things a lot and I can't keep too much in my head.
Having tests that I trust is a relief.

Here's how I do it:

- I use "integration" tests with the Sphinx fixture for generating a
  Sphinx site into a directory in ``var``.

- I added some extra fixtures to (a) speed things up and (b) wrap the
  output in beautifulsoup4 with CSS selectors.

- I get some grouping (e.g. a file) and use PyCharm's auto test mode
  to continously run tests

- Usually I don't know much about what Sphinx generated.
  In those cases, I write a test with ``assert not node`` which will dump the html string to the test console.

- Sometimes I set a debugger breakpoint and stop in a test, then poke around.

- I use type annotations to improve my accuracy when typing and "fail faster".

- I have a run configuration that runs Python's built-in web server on the ``var`` directory.
  This lets me bring up the browser sometimes when I need to poke around.

Switching to Alabaster
======================

I'll now switch to the Alabaster ``layout.html`` and write tests for Jinja2 logic that it has, before switching back to look at ``theme.conf`` knobs for both.

Lots of Uglyisms
================

Going through this process is a reminder of why I'm going through this process:

- All these magically-appearing variables:

    - Global context?

    - Basic theme config value? Alabaster theme config value?

    - Jinja2 ``set``?

- Lots of logic, fairly complex, in a template:

    - Filters to convert values to boolean

Theme Analytics
===============

Alabaster's ``layout.html`` has a theme configuration knob for ``theme_analytics_id``.
If set, then a ``<script>`` gets added to the footer with some Google Analytics info.
To make it more testable, I *added a class*.

Theme Customization Options
===========================

Sphinx uses a customization approach where a theme package supplies a ``theme.conf`` file defining all the customization options.
This file is in an INI format and can "extend" another theme, thus inheriting those options.
Each knob can supply a default value.

While clever, it is another case of Sphinx machinery that could be better done with modern Python:

- The custom ``extends`` approach to inheritance is wonky

- Everything is a string (INI file), so converting into types is something often done in Jinja2 (!!)

- No real validation

- No way to have computed values

Sidebars
========

Alabaster recommends turning on a set of sidebars.
I did so, then made a test root for sidebars and a test file.

About
-----

This sidebar is one that Alabaster recommends as mandatory.
I included it (along with the others) then set ``html_static_path``, made a ``_static`` directory in the test root with the Python logo, and added an ``html_theme_options`` with the logo filename.

Donate
------

Kind of sucks that these sidebars aren't enclosed in a ``<div>`` with a unique class or something else for CSS and for test writing...as noted in the template comment at the top.

I'm not testing all 3 variations (donate_url, opencollective, tidelift) on the heading.

As an aside, about ``alabaster.support``...look, it's yet another little framework.

Fixed Sidebar
=============

No matter what I did, I couldn't get the theme option's ``if`` to fail.
It was always executing.
Likely a simple thing, so I skipped it.

Gratipay
========

Looks like this is removed but still in the ``theme.conf``.
Ignoring.

Indices
=======

Sphinx has a number of common automatically-generated "index" pages: ``genindex``, ``modindex``, ``search``, ``glossary``.
I set up a test root that enabled all of these, then wrote some tests.
Setting this up included the ``sys.path`` dance needed for Sphinx to see local source directories.
As it turned out, doing tests for ``sphinx-apidoc`` stuff was going to require figuring out how to get the fixture to run it.
Since I don't need it for M1 (using on my own blog) I decided to postpone this.

``data-testid``
===============

Kent Dodd's `Testing Library <https://testing-library.com/>`_ has an interesting convention: use a ``data-testid`` attribute on all the places you are testing.
It makes it clear what is part of the test contract.
You don't put weird classes or ids in just for testing, nor rely on a node structure that might change.
And finally, BeautifulSoup makes it easy to find on these.

I decided to switch to this pattern starting here, with tests for ``analytics_id`` and finishing the ``alabaster/theme.conf`` contract.

``toctree``
===========

It could use some tests.
But it probably already has some tests, and it isn't affected by anything in alabaster (except perhaps CSS.)

``html5``
=========

This line in ``basic/layout.html`` is fun::

    {%- block doctype -%}{%- if html5_doctype %}
        <!DOCTYPE html>

Where does ``html5_doctype`` come from?
It's not a ``theme.conf`` value.
Fortunately it's an easy grep away, in ``StandaloneHTMLBuilder``::

            html5_doctype = self.config.html_experimental_html5_writer and html5_ready,

Dang, the ol' Sphinx headfake again.
And can't use my IDEs "goto declaration" since ``self.config`` is a head-fake, plus there's two choices.
Turns out it is related to a ``docutils`` version being 0.13 or higher.
Doesn't matter, though, it is ``False`` by default and deprecated in Sphinx 2.0, thus for Alabaster, it's always going to be the old XHTML doctype, unless you fill the ``doctype`` *block*, instead of changing it by configuration.

Still, Sphinx has some mega-fossils internally with all this HTML5 noise.