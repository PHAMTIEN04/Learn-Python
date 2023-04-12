# Event hook requests trong Python là một cơ chế hoạt động cho phép ghi nhận các sự kiện xảy ra trong quá trình thực thi mã của chương trình và thực thi các hàm được đăng ký (được gọi là "hook functions") để xử lý các sự kiện này.

# Một số ví dụ về event hook requests trong python bao gồm:

# Hook vào trình xử lý ngoại lệ (Exception handler): cho phép bạn thực thi một hàm nào đó khi một exception xảy ra
# Copy
# Insert
# New
# import sys

# def my_exception_handler(exception_type, value, traceback):
#     # Do something useful here.
#     print("An exception was raised:", exception_type, value, traceback)

# sys.excepthook = my_exception_handler
# Hook vào việc thêm/sửa/xoá file: cho phép bạn thực hiện một hành động nào đó khi một hoạt động thay đổi file xảy ra
# Copy
# Insert
# New
# import os

# def my_file_changed_event_handler(event_type, filename):
#     if event_type == 'created':
#         print(f'File {filename} was created')
#     elif event_type == 'modified':
#         print(f'File {filename} was modified')
#     elif event_type == 'deleted':
#         print(f'File {filename} was deleted')

# path_to_monitor = '.'  # monitor the whole folder
# os.system(f'inotifywait -e create,delete,modify -m -r {path_to_monitor} | while read line; do python my_script.py $line; done')
# Hook vào đoạn code được thực thi: cho phép bạn gi