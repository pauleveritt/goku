from bs4.element import Tag


def test_foo(renderer):
    template = '<p>Hello {{ msg }}</p>'
    values = dict(msg='world')
    element: Tag = renderer(template, **values).select_one('p')
    result = element.get_text().strip()
    assert 'Hello world' == result
