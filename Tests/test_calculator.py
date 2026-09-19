from Calculator import add, negate, subtract

def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_negate():
    assert negate(5) == -5
