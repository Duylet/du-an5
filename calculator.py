"""Các hàm tính toán đơn giản dùng làm đối tượng kiểm thử."""


def add(a: float, b: float) -> float:
    """Trả về tổng của hai số."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Trả về hiệu a - b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Trả về tích của hai số."""
    return a * b


def divide(a: float, b: float) -> float:
    """Chia a cho b; không cho phép chia cho 0."""
    if b == 0:
        raise ZeroDivisionError("Không thể chia cho 0.")
    return a / b
