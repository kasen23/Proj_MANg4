from src.math_utils import add, multiply, add_then_multiply

# Unit tests
def test_add():
    assert add(2, 3) == 5

def test_multiply():
    assert multiply(2, 3) == 6

# Integration test
def test_add_then_multiply():
    assert add_then_multiply(2, 3, 4) == 20  # (2+3)*4 = 20