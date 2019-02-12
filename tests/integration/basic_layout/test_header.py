"""

Global Context
==============

- Values from StandaloneHTMLBuilder class attributes
- Values from basic/theme.conf
- Values from alabaster/theme.conf
- Values from self.config.html_context (which means pydantic has to allow
  arbitrary values)

Page Context
============

- Values from StandaloneHTMLBuilder.get_doc_context::
    parents = parents,
    prev = prev,
    next = next,
    title = title,
    meta = meta,
    body = body,
    metatags = metatags,
    rellinks = rellinks,
    sourcename = sourcename,
    toc = toc,
    # only display a TOC if there's more than one item to show
    display_toc = (self.env.toc_num_entries[docname] > 1),
    page_source_suffix = source_suffix,
- Values from StandaloneHTMLBuilder.handle_page::
    ctx['pagename']
    ctx['encoding']
    ctx['pageurl']
    ctx['pathto']
    ctx['css_tag']
    ctx['hasdoc']
    ctx['warn']
    ctx['toctree']
    self.add_sidebars
    self.update_page_context


basic/theme.conf
==================

[theme]
inherit = none
stylesheet = basic.css
pygments_style = none
sidebars = localtoc.html, relations.html, sourcelink.html, searchbox.html

[options]
nosidebar = false
sidebarwidth = 230
body_min_width = 450
body_max_width = 800
navigation_with_keys = False

Sphinx global context
=====================

embedded = self.embedded,
release = return_codes_re.sub('', self.config.release),
last_updated = self.last_updated,
file_suffix = self.out_suffix,
script_files = self.script_files,
css_files = self.css_files,
sphinx_version = __display_version__,
style = stylename,
rellinks = rellinks,
builder = self.name,
parents = [],
logo = logo,
favicon = favicon,


project = self.config.project,
version = self.config.version,
copyright = self.config.copyright,
master_doc = self.config.master_doc,
use_opensearch = self.config.html_use_opensearch,
docstitle = self.config.html_title,
shorttitle = self.config.html_short_title,
show_copyright = self.config.html_show_copyright,
show_sphinx = self.config.html_show_sphinx,
has_source = self.config.html_copy_source,
show_source = self.config.html_show_sourcelink,
sourcelink_suffix = self.config.html_sourcelink_suffix,
language = self.config.language,
html5_doctype = self.config.html_experimental_html5_writer and html5_ready,


"""
from bs4.element import Tag


def test_foo(renderer):
    template = '''\
{%- extends "basic_layout.html" %}
{% block body %}
<p id="foo">Hello world</p>
{% endblock %}
'''
    values = dict(msg='world')
    element: Tag = renderer(template, **values).select_one('#foo')
    result = element.get_text().strip()
    assert 'Hello world' == result
