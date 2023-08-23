import time
import pyautogui

def login_to_app(username, password):
    # Mở ứng dụng Liên Minh Huyền Thoại (giả định ứng dụng đã được mở)
    # Vị trí các trường đăng nhập và nút đăng nhập cần được xác định trước
    login_x, login_y = 500, 300  # Vị trí nút Đăng nhập
    username_x, username_y = 400, 200  # Vị trí trường Tên đăng nhập
    password_x, password_y = 400, 250  # Vị trí trường Mật khẩu

    # Click vào trường Tên đăng nhập và nhập tên đăng nhập
    pyautogui.click(username_x, username_y)
    pyautogui.typewrite(username)

    # Click vào trường Mật khẩu và nhập mật khẩu
    pyautogui.click(password_x, password_y)
    pyautogui.typewrite(password)

    # Click nút Đăng nhập
    pyautogui.click(login_x, login_y)

    # Chờ 5 giây để đăng nhập (giả định)
    time.sleep(5)

# Thực hiện đăng nhập
login_to_app("your_username", "your_password")
