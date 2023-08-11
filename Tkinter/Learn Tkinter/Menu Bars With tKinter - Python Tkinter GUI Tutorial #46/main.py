from tkinter import *

win = Tk()
win.title("Menu Example")
win.geometry("300x300")

# Function to create an empty menu item
def menu_empty(index):
    mn_e = Menu(tearoff=0)
    my_menu.insert_cascade(index, label=" ", menu=mn_e)

# Function to be executed when the "Very Good" menu item is clicked
def our_command():
    Label(win, text="Very Good").pack()

my_menu = Menu()
win.config(menu=my_menu)

menu_empty(0)
menu_empty(1)
menu_empty(2)
menu_empty(3)

menu_file = Menu(tearoff=0)
my_menu.insert_cascade(4, label="File", menu=menu_file)
menu_file.add_command(label="New", command=our_command)  # Command for "New" menu item
menu_file.add_command(label="Open")
menu_file.add_command(label="Exit", command=win.quit)  # Command to exit the application

menu_edit = Menu(tearoff=0)
my_menu.insert_cascade(5, label="Edit", menu=menu_edit)
menu_edit.add_command(label="Cut")
menu_edit.add_command(label="Copy")

win.mainloop()
