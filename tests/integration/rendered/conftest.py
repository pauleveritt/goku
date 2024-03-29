from dataclasses import dataclass
from importlib import resources
import pytest
from jinja2 import DictLoader, Environment, Template
from bs4 import BeautifulSoup


# Fake Sphinx-Jinja2 filters
def dummy_callable(*args):
    return ''


dummy_context = dict(
    pathto=dummy_callable,
    style='',
    hasdoc=dummy_callable,
    gettext=dummy_callable
)


@dataclass
class Renderer:
    env: Environment

    def __call__(self, template: str, **kwargs) -> BeautifulSoup:
        template: Template = self.env.from_string(template)
        result = template.render(**dummy_context, **kwargs)
        soup = BeautifulSoup(result, 'html.parser')
        return soup


@pytest.fixture(scope='session')
def env():
    with resources.open_text('goku', 'basic_layout.html') as f:
        basic_layout = f.read()
    loader = DictLoader({
        'basic_layout.html': basic_layout
    }
    )

    environment = Environment(
        loader=loader,
        extensions=['jinja2.ext.i18n']
    )

    environment.filters['tobool'] = dummy_callable

    yield environment


@pytest.fixture
def renderer(env) -> Renderer:
    r = Renderer(env=env)
    yield r
