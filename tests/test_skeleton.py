#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from ttb_allan.skeleton import fib

__author__ = "NavchetanKaur"
__copyright__ = "NavchetanKaur"
__license__ = "gpl3"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
