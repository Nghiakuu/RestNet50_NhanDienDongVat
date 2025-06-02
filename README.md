# Ứng dụng Nhận diện Động vật

Ứng dụng này sử dụng mô hình ResNet50 đã được huấn luyện sẵn để nhận diện các loài động vật trong hình ảnh.

## Cài đặt

1. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

## Chạy ứng dụng

1. Chạy lệnh sau để khởi động ứng dụng:
```bash
streamlit run app.py
```

2. Mở trình duyệt web và truy cập địa chỉ được hiển thị trong terminal (thường là http://localhost:8501)

## Sử dụng

1. Nhấn vào nút "Browse files" để tải lên hình ảnh động vật
2. Sau khi tải lên, nhấn nút "Nhận diện" để xem kết quả
3. Kết quả sẽ hiển thị tên loài động vật và độ chính xác của dự đoán

## Lưu ý

- Ứng dụng có thể nhận diện được nhiều loại động vật khác nhau
- Kết quả sẽ hiển thị bằng tiếng Anh
- Hỗ trợ các định dạng ảnh: JPG, JPEG, PNG 