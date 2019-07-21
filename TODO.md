# TODO

## Now

## Next

- Fix names generated in _build/_static e.g. sphinx_bulma.css -> goku.css

    - Write a test to ensure that is generated
    
- Switch to pyproject.toml

## Soon

- .css_t contracts

- Write tests for:

  - All the blocks here: http://www.sphinx-doc.org/en/stable/templating.html
  
  - All the knobs here: https://alabaster.readthedocs.io/en/latest/customization.html

- Get rid of all the ``theme.conf`` knobs for adjusting style colors etc.

## Eventually

- Tests and support for ``autodoc`` stuff...punted on this because it requires running an extra command (``sphinx-apidoc``) which isn't supported by the Sphinx pytest fixtures

- Instead of inheriting ``theme.conf`` settings (from either alabaster or basic), flatten the universe

- Put the theme templates in a `templates` directory

- Digest the Sphinx move to html5 templates and use those

- Code quality tools integrated into IDE/hooks/CI:

    - HTML, CSS, JS, Python (black, mypy)

## Done

- Start a diary

