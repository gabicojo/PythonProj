import pytest

# use these values in test functions: test_func(values)


@pytest.fixture(scope='module')
def values():
    x = 7
    y = 3
    return (x, y)


@pytest.fixture(scope='module')
def args_():
    args_ = (7, 13)
    yield args_
    print(">>> cleanup after yielding...")
