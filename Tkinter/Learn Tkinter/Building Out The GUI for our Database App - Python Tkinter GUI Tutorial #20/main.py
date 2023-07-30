from tkinter import *
import sqlite3
from tkinter import messagebox

# Uncomment these lines if you need to create the table and initialize the database:
# conn = sqlite3.connect("address_book.db")

# c = conn.cursor()

# c.execute("""CREATE TABLE addresses (
#         stt integer,
#         first_name text,
#         last_name text,
#         address text,
#         city text,
#         state text,
#         zipcode integer
#     )""")




# conn.commit()
# conn.close()
win = Tk()
win.title("Database App")
win.geometry("1050x390")

def adddata():
    # Connect to the database
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()
    
    # Insert data into the 'addresses' table based on the user input from Entry widgets
    c.execute("INSERT INTO addresses VALUES(:stt,:f_name,:l_name,:address,:city,:state,:zipcode)",
              {
                  'stt'    : stt_e.get(),
                  'f_name' : first_name_e.get(),
                  'l_name' : last_name_e.get(),
                  'address': address_e.get(),
                  'city'   : city_e.get(),
                  'state'  : state_e.get(),
                  'zipcode': zipcode_e.get()
                  
              })
    
    # Commit the changes and close the connection
    conn.commit()
    
    conn.close

    # Clear entry fields after adding data
    stt_e.delete(0,END)
    first_name_e.delete(0,END)
    last_name_e.delete(0,END)
    address_e.delete(0,END)
    city_e.delete(0,END)
    state_e.delete(0,END)
    zipcode_e.delete(0,END)
    
check_d = False
res_labels = []
def showdata():

    global check_d
    global res_labels
    global res
    # Connect to the database
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()
    
    # Fetch all data from the 'addresses' table
    c.execute("SELECT * FROM addresses")
    res = c.fetchall()
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    # Create a label to display the format of the data
    
    # Loop through the fetched data and create labels to display it on the UI
    for i in range(len(res)):
        result_text = f"{res[i][0]} | {res[i][1]} | {res[i][2]} | {res[i][3]} | {res[i][4]} | {res[i][5]}"
        res_label = Label(f,text=result_text)
        res_label.grid(column=0,row=1+i,sticky="W")
        if i+1 == len(res) and check_d == True:
            res_label = Label(f,text=" ",width=70)
            res_label.grid(column=0,row=2+i,sticky="W")

    if len(res) == 0:
        res_label = Label(f,text=" ",width=70)
        res_label.grid(column=0,row=1,sticky="W")
        check_d == False
        
    # Print the fetched data to the console
    print(res)
    print(len(res))


def delete():
    global check_d
    check_d = True
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()

    try:
        # Get the STT value from the Entry widget as an integer
        stt_value = int(dele_e.get())
    except ValueError:
        # If the value is not a valid integer, show an error message
        messagebox.showerror("Invalid Input", "Please enter a valid integer for STT.")
        conn.close()
        return

    # Execute the DELETE query based on the STT value
    c.execute(f"DELETE FROM addresses WHERE stt = {stt_value}")

    conn.commit()
    conn.close()

    

    # Clear the Entry field after deleting data
    dele_e.delete(0, END)


    
def deleteall():
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()
    c.execute("DELETE FROM addresses")
    
    conn.commit()
    conn.close()
    
    
add_label = Label(win,text="ADD DATA",fg="green")
add_label.grid(column=0,row=0,sticky="S")

stt_l = Label(win,text="STT",font=("Arial",12))
stt_l.grid(column=0,row=1)
stt_e = Entry(win,width=50,border=3)
stt_e.grid(column=1,row=1)

first_name_l = Label(win,text="First Name",font = ("Arial", 12))
first_name_l.grid(column=0 ,row=2,padx=20)
first_name_e = Entry(win,width=50,border=3)
first_name_e.grid(column=1, row=2)

last_name_l = Label(win,text="Last Name",font = ("Arial", 12))
last_name_l.grid(column=0,row=3)
last_name_e = Entry(win,width=50,border=3)
last_name_e.grid(column=1,row=3)

address_l = Label(win,text="Address",font = ("Arial", 12))
address_l.grid(column=0,row=4)
address_e = Entry(win,width=50,border=3)
address_e.grid(column=1,row=4)

city_l = Label(win,text="City",font = ("Arial", 12))
city_l.grid(column=0,row=5)
city_e = Entry(win,width=50,border=3)
city_e.grid(column=1,row=5)

state_l = Label(win,text="State",font = ("Arial", 12))
state_l.grid(column=0,row=6)
state_e = Entry(win,width=50,border=3)
state_e.grid(column=1,row=6)

zipcode_l = Label(win,text="Zipcode",font = ("Arial", 12))
zipcode_l.grid(column=0,row=7)
zipcode_e = Entry(win,width=50,border=3)
zipcode_e.grid(column=1,row=7)


add_data = Button(win,text="Confirm More Data",command=adddata)
add_data.grid(column=1,row=8,sticky="E",pady=5)

dele_label = Label(win,text="DELETE DATA",fg="red")
dele_label.grid(column=0,row=9,sticky="S")

dele_l = Label(win,text="Choose STT",font = ("Arial", 12))
dele_l.grid(column=0,row=10)
dele_e = Entry(win,width=50,border=3)
dele_e.grid(column=1,row=10)

delete_data = Button(win,text="Delete",command=delete)
delete_data.grid(column=1,row=11,sticky="E",pady=5)

delete_data_a = Button(win,text="Delete All",command=deleteall)
delete_data_a.grid(column=1,row=12,sticky="E",pady=5)

show_label = Label(win,text="SHOW DATA",fg="green")
show_label.grid(column=2,row=0)

show_data = Button(win,text="Show",command=showdata)
show_data.grid(column=2,row=1,sticky="N",pady=5)

f = LabelFrame(win,width=500,height=350)
f.grid(column=3,row=0,rowspan=13,padx=5)
f.grid_propagate(False)

Format_l = Label(f,text="STT|F_Name|L_Name|Address|City|State|Zipcode")
Format_l.grid(column=0,row=0,sticky="W")

win.mainloop()


# conn = sqlite3.connect("address_book.db")
# c = conn.cursor()

# c.execute("DELETE FROM addresses")
# c.execute("SELECT * FROM addresses")
# res = c.fetchall()
# print(res)

# conn.commit()
# conn.close()