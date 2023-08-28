import tkinter as tk
from tkinter import scrolledtext

def insert_text():
    text = entry.get()
    scrolled_text.insert(tk.END, text + "\n")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Scrollable Text")

# Tạo một thanh cuộn dọc
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Tạo một widget văn bản có thể cuộn
scrolled_text = scrolledtext.ScrolledText(root, yscrollcommand=scrollbar.set)
scrolled_text.pack(fill=tk.BOTH, expand=True)

# Liên kết thanh cuộn với widget văn bản
scrollbar.config(command=scrolled_text.yview)

# Tạo một trường văn bản để nhập dữ liệu
entry = tk.Entry(root)
entry.pack(fill=tk.BOTH, expand=True)

# Tạo một nút để chèn văn bản vào widget văn bản cuộn
insert_button = tk.Button(root, text="Insert", command=insert_text)
insert_button.pack()

root.mainloop()
