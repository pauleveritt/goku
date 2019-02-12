===========
Preparation
===========

This is the first step in the "How we wrote Goku"

First Repo
==========

- Init a repo with a minimal setup.py

- Make src/goku/__init__.py

- Install in editable mode

First Test
==========

- Add `[test]` section in setup.py

- List pytest there

- Rerun editable

- Make tests/unit/test_setup.py

- Assert there is an importable setup function which return a dict
  having the correct values

- Write this setup function

First Docs
==========

- Add sphinx as a dependency

- Generate docs for the theme as a project

- Make a pycharm run config

- Generate docs

- Make a JavaScript debug run config to view docs

First Integration Tests
=======================

- Make a new file tests/integration/test_title.py

- Setup conftest.py which does all the fixture dance

- Add bs4 to tests dependencies

- Add a run config to serve up the /var dir
