import pytest
from bs4.element import Tag

# The default values for all theme options, knobs, templates, etc.
# Nothing customized in conf.py or anywhere else.

pytestmark = pytest.mark.sphinx('html', testroot='alabaster-customized')


@pytest.mark.parametrize('page', ['subdir/subfile.html', ], indirect=True)
class TestAlabasterCustomized:
    """ Twiddle a bunch of knobs """

    def test_touch_icon(self, page):
        icon: Tag = page.find('link', attrs=dict(rel='apple-touch-icon'))
        assert '../_static/touch_icon1' == icon['href']

    def test_canonical_url(self, page):
        link: Tag = page.find('link', attrs=dict(rel='canonical'))
        assert 'canonical_url1subdir/subfile.html' == link['href']

    def test_footer_github_banner(self, page):
        """ Display "fork me", off by default """

        github: Tag = page.select_one('a.github')
        assert 'https://github.com/github_user1/github_repo1' == github['href']
