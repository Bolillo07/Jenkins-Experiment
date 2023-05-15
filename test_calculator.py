import calculator
#12
def test_add():
    assert calculator.add(1, 2) == 3
    assert calculator.add(-1, 1) == 8

def test_subtract():
    assert calculator.subtract(3, 1) == 2
    assert calculator.subtract(0, 0) == 0

def test_multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-2, 4) == -8

def test_divide():
    assert calculator.divide(6, 2) == 3

