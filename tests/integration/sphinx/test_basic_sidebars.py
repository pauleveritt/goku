import pytest
from bs4.element import Tag

# The default values for all theme options, knobs, templates, etc.
# Nothing customized in conf.py or anywhere else.

pytestmark = pytest.mark.sphinx('html', testroot='basic-sidebars')


@pytest.mark.parametrize('page', ['index.html', ], indirect=True)
class TestBasicSidebars:
    """ Turn on the optional html_sidebars in the basic theme """

    def test_about_logo(self, page):
        logo: Tag = page.select_one('p.logo')
        assert logo

        # The href on the link
        assert '../index.html' == logo.find('a')['href']
