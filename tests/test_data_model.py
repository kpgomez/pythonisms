import pytest
from data_model_package.data_model_module import Dog, Cat, Queue


#@pytest.mark.skip()
def test_dog_repr():
    dog = Dog("georgina")
    actual = hasattr(dog, "__repr__")
    expected = True
    assert actual == expected


#@pytest.mark.skip()
def test_dog_mult():
    dog = Dog("georgina")
    actual = hasattr(dog, "__mul__")
    expected = True
    assert actual == expected


#@pytest.mark.skip()
def test_dog_call():
    dog = Dog("georgina")
    actual = hasattr(dog, "__call__")
    expected = True
    assert actual == expected


#@pytest.mark.skip()
def test_cat_len():
    cat = Cat("reese")
    actual = len(cat)
    expected = 5
    assert actual == expected


#@pytest.mark.skip()
def test_queue():
    queue = Queue()
    queue + 9
    queue + 3
    queue - None
    actual = queue.__repr__()
    expected = 'Queue(1)'
    assert actual == expected
