
from tkinter import *



root = Tk()
root.geometry("200x200")
def open(text):
    print(f"Text : {text}")
    

i = 0
list_a = [1,2,3,4,5]
while i <= 4 :
    text = list_a[i]
    a = Button(root,text="Mua",command=lambda x = text: open(x))
    a.grid(column=0,row=i)
    i = i + 1 





root.mainloop()
