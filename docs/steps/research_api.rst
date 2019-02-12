============
Template API
============

- Investigate

    - Web page with options (which is in built docs)

    - theme.conf

    - layout.html is pretty nasty

    - Inherits from basic/layout and basic/theme.conf which is nasty

    - All the places in StandaloneHTMLBuilder where
      values/functions/filters/etc. can come from

- Write initial tests

    - Ensure everything in basic/layout.html and theme.conf is in
      integration test output

    - Ditto for alabaster

- Make a new builder that overrides handlepage to make a new
  dataclass and render with it

    - Start putting everything in until tests pass

- Switch to pydantic to enforce it

- Make a new API that puts things in different piles

    - Fork basic/layout into local directory and point layout at it

    - Start moving the values to better locations

