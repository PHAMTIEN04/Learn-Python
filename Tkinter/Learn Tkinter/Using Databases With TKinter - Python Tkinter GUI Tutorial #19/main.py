from tkinter import *
import sqlite3


win = Tk()

# Databases

# Create a database or connect to one 
conn = sqlite3.connect("address_book.db")

# Create cursor
c = conn.cursor()

c.execute("""CREATE TABLE addresses(
        first_text text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
    
    )""")


# Commit Changes
conn.commit()

# Close Connection
conn.close()






win.mainloop()



