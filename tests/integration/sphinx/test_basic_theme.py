import bs4
from bs4.element import Tag
import pytest

pytestmark = pytest.mark.sphinx('html', testroot='basic-theme')


@pytest.mark.parametrize('page', ['index.html', ], indirect=True)
class TestBasicLayoutDefaults:

    def test_all(self, page):
        element: Tag = page.select('.footer a')[1]
        content = element.contents[0].strip()
        assert 'Alabaster' in content

        # Doctype support
        # TODO fillable block for doctype
        doctype = [item for item in page.contents if isinstance(item, bs4.Doctype)][0]
        assert doctype == 'html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n  ' \
                          '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"'

        # rdelim1
        element: Tag = page.select_one('.nav-item nav-item-0 a')
        content = element.get_text().strip()
        assert 9 == content