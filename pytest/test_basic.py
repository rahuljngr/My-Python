import basic
import pytest
import sys

def test_calc_total():
    total = basic.calc_total(4,5)
    assert total == 9

def test_calc_multiply():
    result = basic.calc_multiply(10,3)
    assert result == 30

def test_dummy():
    assert True