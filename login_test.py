import pytest

def func(x):
    return x+1

def test_01():
    assert func(2) == 3

def test_02():
    assert func(2) == 4
