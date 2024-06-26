# Ứng dụng Đăng nhập Lark

Đây là một ứng dụng Streamlit thể hiện tích hợp đăng nhập OAuth của Lark.

## Cài đặt và Thiết lập

### 1. Chuẩn bị môi trường

- Đảm bảo bạn đã cài đặt Python (phiên bản 3.7 trở lên) trên máy tính của bạn.
- Nên sử dụng môi trường ảo để quản lý dependencies. Tạo môi trường ảo bằng lệnh:
  ```
  python -m venv venv
  ```
- Kích hoạt môi trường ảo:
  - Trên Windows: `venv\Scripts\activate`
  - Trên macOS và Linux: `source venv/bin/activate`

### 2. Clone repository

- Clone repository này về máy của bạn:
  ```
  git clone [URL_của_repository]
  cd [tên_thư_mục_repository]
  ```

### 3. Cài đặt dependencies

- Cài đặt các thư viện cần thiết bằng cách chạy lệnh:
  ```
  pip install -r requirements.txt
  ```

### 4. Cấu hình ứng dụng Lark

- Đăng nhập vào [Lark Developer Console](https://open.larksuite.com/)
- Tạo một ứng dụng mới hoặc chọn ứng dụng hiện có
- Trong phần "Security Settings", cấu hình Redirect URI: `http://localhost:8501`
- Ghi nhớ App ID và App Secret của ứng dụng

### 5. Cấu hình biến môi trường

- Tạo file `.env` trong thư mục gốc của dự án
- Thêm các thông tin sau vào file `.env`:
  ```
  LARK_APP_ID=your_app_id
  LARK_APP_SECRET=your_app_secret
  LARK_REDIRECT_URI=http://localhost:8501
  ```
- Thay thế `your_app_id` và `your_app_secret` bằng thông tin thực tế của ứng dụng Lark của bạn

### 6. Chạy ứng dụng

- Trong thư mục dự án, chạy lệnh sau để khởi động ứng dụng Streamlit:
  ```
  streamlit run main.py
  ```
- Ứng dụng sẽ chạy và mở trình duyệt web tại địa chỉ `http://localhost:8501`

## Sử dụng ứng dụng

1. Khi ứng dụng khởi động, bạn sẽ thấy một nút "Login with Lark"
2. Nhấp vào nút này để bắt đầu quá trình đăng nhập
3. Bạn sẽ được chuyển hướng đến trang đăng nhập của Lark
4. Đăng nhập bằng tài khoản Lark của bạn
5. Sau khi đăng nhập thành công, bạn sẽ được chuyển hướng trở lại ứng dụng
6. Ứng dụng sẽ hiển thị thông tin người dùng của bạn
7. Để đăng xuất, nhấp vào nút "Logout"

## Cấu trúc dự án

- `main.py`: File chính chứa mã nguồn của ứng dụng Streamlit
- `requirements.txt`: Danh sách các thư viện Python cần thiết
- `.env`: File chứa các biến môi trường (không nên đưa lên git)
- `.gitignore`: Danh sách các file và thư mục không nên theo dõi bởi git
- `README.md`: File này, chứa hướng dẫn và thông tin về dự án

## Lưu ý

- Đảm bảo rằng bạn không chia sẻ hoặc công khai App ID và App Secret của ứng dụng Lark
- File `.env` đã được thêm vào `.gitignore` để tránh vô tình đưa thông tin nhạy cảm lên repository
- Nếu bạn gặp bất kỳ vấn đề nào trong quá trình cài đặt hoặc sử dụng, hãy kiểm tra lại các bước cấu hình và đảm bảo rằng tất cả các bước đều được thực hiện chính xác

## Hỗ trợ

Nếu bạn gặp bất kỳ vấn đề nào hoặc có câu hỏi, vui lòng tạo một issue trong repository GitHub của dự án.