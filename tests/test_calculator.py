import pytest

from calculator import add, divide, multiply, subtract


def test_add(sample_numbers):
    a, b = sample_numbers
    assert add(a, b) == 12


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (8, 3, 5),
        (3, 8, -5),
        (5, 5, 0),
        (-2, -4, 2),
    ],
)
def test_subtract_multiple_cases(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (2, 3, 6),
        (-2, 3, -6),
        (0, 9, 0),
        (1.5, 2, 3),
    ],
)
def test_multiply_multiple_cases(a, b, expected):
    assert multiply(a, b) == expected


def test_divide(sample_numbers):
    a, b = sample_numbers
    assert divide(a, b) == 5


def test_divide_returns_float():
    assert divide(5, 2) == 2.5


def test_divide_by_zero_raises_error():
    with pytest.raises(ZeroDivisionError, match="Không thể chia cho 0"):
        divide(10, 0)


def test_add_negative_numbers():
    assert add(-3, -7) == -10
