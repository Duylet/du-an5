# Demo kiểm thử tự động Python với pytest

Dự án minh họa cách dùng [pytest](https://github.com/pytest-dev/pytest) để kiểm thử các hàm Python. Đây là dự án demo nhỏ lấy cảm hứng từ quy trình sử dụng pytest, không phải bản sao mã nguồn của pytest.

## Chức năng
- Kiểm thử các phép cộng, trừ, nhân, chia.
- Kiểm tra trường hợp đầu vào không hợp lệ và ngoại lệ.
- Dùng `@pytest.mark.parametrize` để chạy một test với nhiều bộ dữ liệu.
- Dùng fixture để tái sử dụng dữ liệu kiểm thử.
- Kiểm thử hàm xử lý văn bản.
- GitHub Actions tự chạy test khi push hoặc mở pull request.

## 1. Chuẩn bị
Cần Python 3.10 trở lên và VS Code. Mở thư mục dự án trong VS Code, chọn **Terminal → New Terminal**.

Tạo môi trường ảo trên Windows:
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

Nếu PowerShell chặn kích hoạt môi trường, có thể chạy trực tiếp bằng:
```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m pytest
```

## 2. Cài thư viện
```powershell
python -m pip install -r requirements.txt
```

## 3. Chạy toàn bộ test
```powershell
python -m pytest -v
```

Kết quả thành công sẽ hiển thị các test ở trạng thái PASSED và tổng số test đã chạy.

## 4. Chạy riêng một file hoặc test
```powershell
python -m pytest tests/test_calculator.py -v
python -m pytest tests/test_text_utils.py -v
python -m pytest -k divide -v
```

## 5. Thử xem pytest báo lỗi như thế nào
Mở `calculator.py`, tạm thời sửa hàm `add` thành `return a - b`, rồi chạy:
```powershell
python -m pytest -v
```
pytest sẽ báo test nào thất bại và chỉ ra giá trị thực tế so với giá trị mong đợi. Sau khi thử, hãy sửa hàm về đúng `return a + b`.

## Cấu trúc dự án
```text
du-an5/
├── calculator.py
├── text_utils.py
├── requirements.txt
├── pyproject.toml
├── .gitignore
├── README.md
├── .github/
│   └── workflows/
│       └── tests.yml
└── tests/
    ├── conftest.py
    ├── test_calculator.py
    └── test_text_utils.py
```

## Kiến thức chính
- **Test function:** hàm có tên bắt đầu bằng `test_`.
- **assert:** xác nhận kết quả thực tế đúng như mong đợi.
- **Parametrize:** kiểm tra nhiều bộ dữ liệu mà không phải viết lặp nhiều hàm.
- **Fixture:** tạo dữ liệu hoặc tài nguyên dùng chung cho test.
- **pytest.raises:** xác nhận một đoạn mã phát sinh ngoại lệ như mong đợi.

Tài liệu chính thức: [pytest Getting Started](https://pytest.org/en/latest/getting-started.html).
