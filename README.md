# Mã nguồn mở (Nhóm 8)

- Nguyễn Việt Giang
- Nguyễn Đình Việt Anh
- Trần Thị Hạ
- Phạm Thị Thu Hiền

---

**Đảm bảo đã cài đặt Python và Django để chạy**

## Yêu cầu hệ thống

- Python version 3.10.4 và Django 4.2.4
- DataBase: SQLite
- Có thể dùng: (Visual Studio Code, Visual Studio, etc.)

## Hướng dẫn cài đặt

- Clone bằng git hoặc tải file zip sau đó giải nén.
- Sử dùng file vừa tải về trỏ vào BaiTapLonNhom8 và làm theo hướng dẫn bên dưới.

## Các câu lệnh dùng cho tất cả VD ở dưới đây trong terminal (thay đổi nếu đang sử dụng Python3, dùng python3 thay vì python)

## Chạy lệnh sau để tải thư viện custom giao diện admin (Trong trường hợp tải lỗi thì vào appsetting để xóa Jazzmin và setting của nó)

```
 pip install django-jazzmin
```

## Setup môi trường (nếu cần)

    ```
    python3 -m venv myenv
    ```

    ```
    pip3 install django-jazzmin
    ```

    ```
    python3 -m pip install Pillow
    ```

## Hướng dẫn chạy dự án

**Khởi chạy server**: Trong thư mục dự án (tại: BaiTapLonNhom8) mở terminal và chạy lệnh sau để khởi chạy server Django trên cổng 8888:

    ```
    python manage.py runserver 8888
    ```

## Đối với máy Linux cần chạy môi trường ảo trước

```
source myenv/bin/activate
```

-- Sau đó

    ```
    python manage.py runserver 8888
    ```

---

## Tạo một tài khoản quản trị mới thông qua

```

    python manage.py createsuperuser

```

---

## Hoặc sử dụng với tài khoản: vietgiang, mật khẩu: vip1111.

Mở trình duyệt và truy cập địa chỉ [http://localhost:8888/](http://localhost:8888/).
Mở trình duyệt và truy cập địa chỉ trang quản trị [http://localhost:8888/admin](http://localhost:8888/admin).

## Các câu lệnh cần biết để thao tác cơ bản với Django

**Tạo dự án(projectname thay bằng tên dự án)**:

```

    python -m django startproject projectname

```

---

**Tạo ứng dụng con(your_app_name thay bằng tên app)**:

```

    python manage.py startapp your_app_name

```

---

**Tạo các bảng trong cơ sở dữ liệu**:

```

    python manage.py makemigrations

```

---

```

python manage.py migrate

```

---

**Sau đó có thể chạy app như đoạn code ở trên**:

```

```
