import json
import os
from pathlib import Path
from shutil import rmtree

from bs4 import BeautifulSoup
import pytest
from sphinx.testing.path import path


@pytest.fixture(scope='session')
def remove_sphinx_projects(sphinx_test_tempdir):
    # Even upon exception, remove any directory from temp area
    # which looks like a Sphinx project. This ONLY runs once.
    roots_path = Path(sphinx_test_tempdir)
    for d in roots_path.iterdir():
        if d.is_dir():
            build_dir = Path(d, '_build')
            if build_dir.exists():
                # This directory is a Sphinx project, remove it
                rmtree(str(d))

    yield


@pytest.fixture()
def rootdir(remove_sphinx_projects):
    roots = path(os.path.dirname(__file__) or '.').abspath() / 'roots'
    yield roots


@pytest.fixture()
def content(app):
    app.build()
    yield app


@pytest.fixture()
def page(content, request) -> BeautifulSoup:
    pagename = request.param
    c = (content.outdir / pagename).text()

    yield BeautifulSoup(c, 'html.parser')


@pytest.fixture()
def css(content, request) -> str:
    """ Perhaps later, find some CSS Parser """
    pagename = request.param
    c = (content.outdir / pagename).text()

    yield c


@pytest.fixture()
def json_page(content, request):
    pagename = request.param
    c = (content.outdir / pagename).text()

    yield json.loads(c)
