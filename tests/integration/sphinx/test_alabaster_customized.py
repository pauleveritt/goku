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
