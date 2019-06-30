import pytest
from bs4.element import Tag

# The default values for all theme options, knobs, templates, etc.
# Nothing customized in conf.py or anywhere else.

pytestmark = pytest.mark.sphinx('html', testroot='alabaster-sidebars')


# *** NOTE: We are using ``hellopage.html`` to get some of the navigation
# in the sidebars.
@pytest.mark.parametrize('page', ['hellopage.html', ], indirect=True)
class TestAlabasterSidebars:
    """ Turn on the Alabaster-recommended html_sidebars """

    def test_about_logo(self, page):
        logo: Tag = page.select_one('p.logo')
        assert logo

        # The href on the link
        assert 'index.html' == logo.find('a')['href']

        # img path
        assert '_static/python-logo.png' == logo.find('img')['src']

        # heading
        assert 'Goku Sidebars' == logo.find('h1').text

    def test_about_description(self, page):
        assert 'description1' == page.select_one('p.blurb').text

    def test_github(self, page):
        github: Tag = page.find('iframe', attrs=dict(width='200px'))
        assert 'github_user1' in github['src']
        assert 'github_repo1' in github['src']
        assert 'github_type1' in github['src']
        assert 'github_count1' in github['src']

    def test_about_travis(self, page):
        travis: Tag = page.select('a.badge')[0]
        assert 'travis-ci.org' in travis['href']
        assert 'github_user1' in travis['href']
        assert 'badge_branch1' in travis.select_one('img')['alt']
        assert 'badge_branch1' in travis.select_one('img')['src']

    def test_about_codecov(self, page):
        travis: Tag = page.select('a.badge')[1]
        assert 'codecov.io' in travis['href']
        assert 'github_user1' in travis['href']
        assert 'badge_branch1' in travis.select_one('img')['alt']
        assert 'badge_branch1' in travis.select_one('img')['src']

    def test_donate_heading(self, page):
        heading: Tag = page.select_one('h3.donation')
        assert heading

    def test_donate_url(self, page):
        link: Tag = page.find('a', attrs=dict(href='donate_url1'))
        assert link
        assert 'shields.io' in link.select_one('img')['src']

    def test_donate_opencollective(self, page):
        url = 'https://opencollective.com/opencollective1/donate'
        link: Tag = page.find('a', attrs=dict(href=url))
        assert link

        assert 'opencollective.com' in link.select_one('img')['src']

    def test_donate_tidelift(self, page):
        link: Tag = page.find('a', attrs=dict(href='tidelift_url1'))
        assert link

        assert 'Tidelift Subscription' in link.text

