import pytest
from calculator import add


def test_add(values):
    x = values[0]
    y = values[1]
    assert add(x, y) == x + y


def test_add_2(args_):
    x = args_[0]
    y = args_[1]
    assert add(x, y) == x + y
