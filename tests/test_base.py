# -*- coding: utf-8 -*-

import pytest
from pyhy.base import hydrograph

__author__ = "lboutin"
__copyright__ = "lboutin"
__license__ = "mit"


def test_hydrograph():
    #Test string
    instance = hydrograph("test")
    assert instance.run() == 'test'
    #Test float to string
    instance = hydrograph(5.56)
    assert instance.run() == '5.56'


    #with pytest.raises(AssertionError):
    #    fib(-10)
