from dataclasses import dataclass
from importlib import resources
import pytest
from jinja2 import DictLoader, Environment, Template
from bs4 import BeautifulSoup


@dataclass
class Renderer:
    env: Environment

    def __call__(self, template: str, **kwargs) -> BeautifulSoup:
        template: Template = self.env.from_string(template)
        result = template.render(**kwargs)
        soup = BeautifulSoup(result, 'html.parser')
        return soup


@pytest.fixture(scope='session')
def env():
    with resources.open_text('sphinx_bulma', 'basic_layout.html') as f:
        basic_layout = f.read()
    loader = DictLoader({
        'basic_template.html': basic_layout
    }
    )
    environment = Environment(loader=loader)
    yield environment


@pytest.fixture
def renderer(env) -> Renderer:
    r = Renderer(env=env)
    yield r
