#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from sphinx_bulma.skeleton import fib

__author__ = "Paul Everitt"
__copyright__ = "Paul Everitt"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
