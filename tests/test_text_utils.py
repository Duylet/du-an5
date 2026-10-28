import pytest

from text_utils import count_words, normalize_text


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("  Xin Chào  ", "xin chào"),
        ("PYTHON", "python"),
        ("", ""),
        ("\n  Kiểm thử\t", "kiểm thử"),
    ],
)
def test_normalize_text(source, expected):
    assert normalize_text(source) == expected


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("xin chào", 2),
        ("  nhiều   khoảng   trắng ", 3),
        ("", 0),
        ("một", 1),
    ],
)
def test_count_words(source, expected):
    assert count_words(source) == expected
