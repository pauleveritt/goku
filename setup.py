from setuptools import setup, find_packages


def readfile(name):
    with open(name) as f:
        return f.read()


readme = readfile('README.rst')
changes = readfile('CHANGELOG.rst')

docs_require = [
]

tests_require = [
    'pytest',
    'pytest-cov',
    'beautifulsoup4',
]

setup(
    name='goku',
    version='0.0.1',
    description=(
        'Bulma theme for Sphinx with special powers'
    ),
    long_description=readme + '\n\n' + changes,
    author='Paul Everitt',
    author_email='pauleveritt@me.com',
    url='https://github.com/pauleveritt/goku',
    license='MIT',
    packages=find_packages('src', exclude=['tests']),
    package_dir={'': 'src'},
    include_package_data=True,
    python_requires='>=3.7',
    install_requires=[
        'Sphinx'
    ],
    extras_require={
        'docs': docs_require,
        'testing': tests_require,
    },
    entry_points={"sphinx.html_themes": ["goku = goku"]},
    zip_safe=False,
    keywords='sphinx',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
)
