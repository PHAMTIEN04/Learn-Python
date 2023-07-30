from tkinter import *
import sqlite3

# Uncomment these lines if you need to create the table and initialize the database:
# conn = sqlite3.connect("address_book.db")

# c = conn.cursor()

# c.execute("""CREATE TABLE addresses (
#         first_name text,
#         last_name text,
#         address text,
#         city text,
#         state text,
#         zipcode integer
#     )""")




# conn.commit()

win = Tk()
win.title("Database App")
win.geometry("500x350")

def adddata():
    # Connect to the database
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()
    
    # Insert data into the 'addresses' table based on the user input from Entry widgets
    c.execute("INSERT INTO addresses VALUES(:f_name,:l_name,:address,:city,:state,:zipcode)",
              {
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
    first_name_e.delete(0,END)
    last_name_e.delete(0,END)
    address_e.delete(0,END)
    city_e.delete(0,END)
    state_e.delete(0,END)
    zipcode_e.delete(0,END)

def showdata():
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
    Format_l = Label(win,text="F_Name|L_Name|Address|City|State|Zipcode")
    Format_l.grid(column=1,row=8,sticky="W")
    
    # Loop through the fetched data and create labels to display it on the UI
    for i in range(len(res)):
        result_text = f"{res[i][0]} | {res[i][1]} | {res[i][2]} | {res[i][3]} | {res[i][4]} | {res[i][5]}"
        res_label = Label(win,text=result_text)
        res_label.grid(column=1,row=9+i,sticky="W")
        
    # Print the fetched data to the console
    print(res)
    print(len(res))


first_name_l = Label(win,text="First Name",font = ("Arial", 12))
first_name_l.grid(column=0 ,row=0,padx=20)
first_name_e = Entry(win,width=50,border=3)
first_name_e.grid(column=1, row=0)

last_name_l = Label(win,text="Last Name",font = ("Arial", 12))
last_name_l.grid(column=0,row=1)
last_name_e = Entry(win,width=50,border=3)
last_name_e.grid(column=1,row=1)

address_l = Label(win,text="Address",font = ("Arial", 12))
address_l.grid(column=0,row=2)
address_e = Entry(win,width=50,border=3)
address_e.grid(column=1,row=2)

city_l = Label(win,text="City",font = ("Arial", 12))
city_l.grid(column=0,row=3)
city_e = Entry(win,width=50,border=3)
city_e.grid(column=1,row=3)

state_l = Label(win,text="State",font = ("Arial", 12))
state_l.grid(column=0,row=4)
state_e = Entry(win,width=50,border=3)
state_e.grid(column=1,row=4)

zipcode_l = Label(win,text="Zipcode",font = ("Arial", 12))
zipcode_l.grid(column=0,row=5)
zipcode_e = Entry(win,width=50,border=3)
zipcode_e.grid(column=1,row=5)


add_data = Button(win,text="Confirm More Data",command=adddata)
add_data.grid(column=1,row=6,sticky="E",pady=5)

show_data = Button(win,text="Show Data",command=showdata)
show_data.grid(column=1,row=7,sticky="E",pady=5)




win.mainloop()


# conn.close()