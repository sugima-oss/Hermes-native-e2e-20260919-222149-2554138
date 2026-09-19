from Calculator import add, multiply

def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(4, 5) == 20


def test_multiply_by_zero():
    assert multiply(12, 0) == 0


def test_multiply_negative_numbers():
    assert multiply(-3, 4) == -12
