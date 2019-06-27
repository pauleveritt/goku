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