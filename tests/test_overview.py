import pytest
from overview_package.overview_module import make_class, inner_function, func


#@pytest.mark.skip()
def test_make_class():
    cls = make_class(10)
    d = cls("Tim")
    actual = isinstance(d, cls)
    expected = True
    assert actual == expected


#@pytest.mark.skip()
def test_func_2():
    new_func = func(2)
    expected = "x is not 1"
    actual = new_func()
    assert actual == expected


#@pytest.mark.skip()
def test_func_1():
    another_func = func(1)
    expected = "x is equal to 1"
    actual = another_func()
    assert actual == expected