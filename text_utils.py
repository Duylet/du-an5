"""Một vài hàm xử lý văn bản để thực hành kiểm thử."""


def normalize_text(text: str) -> str:
    """Loại bỏ khoảng trắng ở hai đầu và chuẩn hóa thành chữ thường."""
    return text.strip().lower()


def count_words(text: str) -> int:
    """Đếm số từ, xem các chuỗi khoảng trắng liên tiếp là một dấu phân cách."""
    return len(text.split())
