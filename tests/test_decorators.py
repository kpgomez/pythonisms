import pytest
from decorators_package.decorators_module import func, func2, func3


#@pytest.mark.skip
def test_func_wrapper():
    actual = func2(5, 6)
    expected = 6
    assert actual == expected


#@pytest.mark.skip
def test_func3():
    actual = func3()
    expected = "i am func3"
    assert actual == expected