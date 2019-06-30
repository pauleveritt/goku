from typing import Optional, List

import bs4
import pytest
from bs4.element import Tag

# The default values for all theme options, knobs, templates, etc.
# Nothing customized in conf.py or anywhere else.

pytestmark = pytest.mark.sphinx('html', testroot='basic-theme')


@pytest.mark.parametrize('page', ['index.html', ], indirect=True)
class TestBasicLayoutDefaults:
    """ Structures in sphinx.themes.basic, as seen through Alabaster """

    def test_doctype(self, page):
        doctype = [item for item in page.contents if isinstance(item, bs4.Doctype)][0]
        assert 'xhtml1-transitional.dtd' in doctype

    def test_reldelim(self, page):
        node = page.select_one('.nav-item-0')
        assert node is None
        # # rdelim1
        # element: Tag = page.select_one('.nav-item nav-item-0 a')
        # content = element.get_text().strip()
        # assert 9 == content

    def test_url_root(self, page):
        """ Jinja2 variable defined at top of basic_layout """

        node: Tag = page.select_one('#documentation_options')
        assert './' == node['data-url_root']

    def test_titlesuffix(self, page):
        """ Jinja2 variable defined from docstitle global knob """

        node: Tag = page.select_one('title')
        # Nothing customized
        assert 'Hello World' == node.text

    def test_sidebar(self, page):
        """ Ensure the sidebar container exists """

        node: Tag = page.select_one('.sphinxsidebar')
        assert 'main navigation' == node['aria-label']

    def test_sidebar_logo(self, page):
        """ Ensure no logo is present """

        node: Tag = page.select_one('.sphinxsidebar p.logo')
        assert node is None

    def test_script_documentation_options(self, page):
        """ The ``pathto`` function using documention_options.js """

        node: Tag = page.select_one('#documentation_options')
        assert '_static/documentation_options.js' == node['src']

    def test_css_documentation_style(self, page):
        """ The `css` Jinja2 macro """

        nodes: List[Tag] = page.find_all('link', attrs=dict(rel='stylesheet'))
        assert '_static/goku.css' == nodes[0]['href']
        assert '_static/pygments.css' == nodes[1]['href']
        assert '_static/custom.css' == nodes[2]['href']

    def test_html_tag(self, page):
        """ Use default for top-level html node """

        node: Tag = page.select_one('html')
        assert 'http://www.w3.org/1999/xhtml' == node['xmlns']
        assert node.get('lang') is None

    def test_meta_http_equiv(self, page):
        """ The meta http equiv is driven by a flag with a default  """

        node: Optional[Tag] = page.find('meta', attrs={'http-equiv': 'X-UA-Compatible'})
        assert 'IE=Edge' == node['content']

    def test_meta_charset(self, page):
        """ The meta charset is driven by a flag with a default to not display  """

        # Don't do this
        nodes: List[Tag] = page.find_all('meta')
        for node in nodes:
            assert 'charset' not in node.attrs

        # Instead, do this
        node: Optional[Tag] = page.find('meta', attrs={'http-equiv': 'Content-Type'})
        assert 'text/html; charset=utf-8' == node['content']

    def test_not_embedded(self, page):
        """ A number of nodes in <head> if embedded is false (the default is true) """

        # link rel="canonical" is embedded but wrapped in a pageurl so not used
        assert not page.find('link', attrs=dict(rel='canonical'))

        # opensearch should *NOT* be there, use_opensearch is false
        search: Tag = page.find('link', attrs=dict(rel='search'))
        assert 'Search' == search['title']
        assert 'search.html' == search['href']

        # favicon
        assert not page.find('link', attrs=dict(rel='shortcut icon'))

    def test_linktags(self, page):
        """ The block for filling in link tags is UNUSED """

        # The basic theme defines a block linktags which alabaster
        # appears to not use

        assert not page.find('link', attrs=dict(rel='author'))
        assert not page.find('link', attrs=dict(rel='copyright'))

    def test_body_block(self, page):
        """ By default the body node should have no attributes on it """

        assert {} == page.find('body').attrs

    def test_empty_header_relbar_sidebar(self, page):
        """ Alabaster does not fill the header, relbar1, or sidebar1 blocks """

        body: Tag = page.find('body')
        # Skip over the text node
        first_child = body.contents[1]
        assert 'div' == first_child.name

    def test_document_block(self, page):
        """ The basic theme has a block with some logic in it """

        # render_sidebar is Jinja2 var derived from configuration, defaults to false """
        assert not page.select('div.bodywraper')

        # A div with class and role
        assert 'main' == page.find('div', attrs={'class': 'body'})['role']

    def test_footer(self, page):
        """ The footer block """

        footer: Tag = page.find('div', attrs={'class': 'footer'})
        assert footer

        # See if some of the text nodes and children are present and translated
        assert '©' in footer.contents[0]
        assert 'http://sphinx-doc.org/' == footer.contents[1]['href']
        assert 'Sphinx' in footer.contents[1].text

        # Project name and link should be next
        assert 'https://github.com/pauleveritt/goku' == footer.contents[3]['href']
        assert 'Goku' in footer.contents[3].text

        # Page source
        assert '_sources/index.rst.txt' == footer.contents[5]['href']
        assert 'Page source' == footer.contents[5].text


@pytest.mark.parametrize('page', ['hellopage.html', ], indirect=True)
class TestBasicLayoutPageDefaults:
    """ A sub-page, not the index page """

    pass
