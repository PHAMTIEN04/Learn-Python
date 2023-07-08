from tkinter import *
import os

def shutdown_computer():
    os.system("shutdown /s /t 0")

def show_dialog():
    win1.withdraw()  # Ẩn cửa sổ chính
    
    dialog = Toplevel()
    dialog.title("Love")
    dialog.geometry("200x150")
    dialog.configure(bg="#FF69B4")
    
    label = Label(dialog, text="Làm người yêu tớ nhé!!!", fg="red", font=("Arial", 10))
    label.pack(pady=10)
    
    button_frame = Frame(dialog, bg="#FF69B4")
    button_frame.pack()
    
    button_yes = Button(button_frame, text="Yes", width=6, height=2, bg="#00FA9A", command=shutdown_computer)
    button_yes.pack(side=LEFT, padx=5,pady=30)
    
    button_no = Button(button_frame, text="No", width=6, height=2, bg="#00FA9A", command=shutdown_computer)
    button_no.pack(side=LEFT, padx=5,pady=30)
    
    dialog.mainloop()

def show_main_window():
    win.deiconify()  # Hiển thị lại cửa sổ chính

def open_dialog():
    win.withdraw()  # Ẩn cửa sổ chính
    global win1
    win1 = Toplevel()
    win1.title("Love")
    win1.geometry("200x150")
    win1.configure(bg="#FF69B4")

    label = Label(win1, text="Tớ muốn nói điều này", fg="red", font=("Arial", 10))
    label.pack(pady=10)

    button_next = Button(win1, text="Next", width=6, height=2, bg="#00FA9A", command=show_dialog)
    button_next.pack(pady=30)

    win1.protocol("WM_DELETE_WINDOW", show_main_window)  # Xử lý sự kiện khi đóng cửa sổ con

def exit_program():
    win.destroy()

# # Lấy đường dẫn đến thư mục chứa file Python
# current_dir = os.path.dirname(os.path.abspath(__file__))

# # Kết hợp đường dẫn tới file icon trong thư mục chứa file Python
# icon_path = os.path.join(current_dir, "favicon.ico")

win = Tk()
win.title("LOVE")
win.geometry("200x150")
win.configure(bg="#FF69B4")

label = Label(win, text="Chào cậu!", font=("Arial", 10), border=5, fg="red")
label.pack(pady=10)

button_next = Button(win, text="Next", width=7, height=2, border=2, command=open_dialog, bg="#00FA9A")
button_next.pack(pady=30)

button_exit = Button(win, text="Exit", width=7, height=2, border=2, command=exit_program, bg="#FF4500")
button_exit.pack(pady=5)

win.mainloop()
