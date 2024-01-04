import tkinter
from tkinter import messagebox
from tkinter import ttk
import mysql.connector 

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="archery_equipment_ordering"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

#window = tkinter.Frame(bg='#333333')

def Total():
    
    name_label = name_entry.get()
    Phonenumber_label = Phonenumber_entry.get()
    email_label = email_entry.get()
    Address_label = Address_entry.get()
    district_label = district_combobox.get()
    Paymentmethod_label = Paymentmethod_combobox.get()
    
    print("name;", name_label)
    print("phone number;", Phonenumber_label)
    print("email;", email_label)
    print("address;", Address_label)
    print("disrict area;", district_label)
    print("payment method;", Paymentmethod_label)
    
    
    
    #selected_items = archery_listbox.curselection()
   # total_price = 0
   # for index in selected_items:
   #     item_price = int(archery_items[index].split('-')[1].strip().replace('rm', ''))
   #     total_price += item_price
   # messagebox.showinfo(title="Total Price", message=f"Total Price: RM {total_price}")
    
   # if name_entry.get() and Phonenumber_entry.get() and Address_entry.get() and email_entry.get():
   #     messagebox.showinfo(title="Order Success", message="You successfully Ordered.")
   # else:
   #     messagebox.showerror(title="Error", message="Invalid order.")
    
    
    selected_items = archery_listbox.curselection()
    total_price = 0
    selected_indices = archery_listbox.curselection()
    selected_items = [archery_items[index] for index in selected_indices]
    
    
    selected_indices = archery_listbox.curselection()
    total_price = 0

    for index in selected_indices:
        index = int(index)  # Ensure index is an integer
        item_price = int(archery_items[index].split('-')[1].strip().replace('rm', ''))
        total_price += item_price

    messagebox.showinfo(title="Total Price", message=f"Total Price: RM {total_price}")

    
    
    #for index in selected_items:
    #    item_price = int(archery_items[index].split('-')[1].strip().replace('rm', ''))
    #    total_price += item_price
    #messagebox.showinfo(title="Total Price", message=f"Total Price: RM {total_price}")
   
    if name_entry.get() and Phonenumber_entry.get() and Address_entry.get() and email_entry.get():
        messagebox.showinfo(title="Order Success", message="You successfully Ordered.")
    else:
        messagebox.showerror(title="Error", message="Invalid order.")
    

# ... (other parts of your code)
    sql = "INSERT INTO archery_ordering (name_label, Phonenumber_label, email_label, Address_label, district_label, Paymentmethod_label, selected_items, total_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (name_label, Phonenumber_label, email_label, Address_label, district_label, Paymentmethod_label, str(selected_items), total_price)
    mycursor.execute(sql, val)
    mydb.commit()




# Creating widgets
window = tkinter.Tk()
window.title("archery equipment ordering in Pahang area ")
window.geometry('500x500')
window.configure(bg='#333333')

Title_label = tkinter.Label(window, text="archery equipment ordering in Pahang area", bg='#333333', fg="#FF3399", font=("Arial", 30))
Title_label.pack(pady=30, padx=20)

name_label = tkinter.Label(window, text="Name", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
name_label.pack(pady=0, padx=10)
name_entry = tkinter.Entry(window, font=("Arial", 16))
name_entry.pack(pady=0, padx=10)

Phonenumber_label = tkinter.Label(window, text="Phone number", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
Phonenumber_label.pack(pady=0, padx=10)
Phonenumber_entry = tkinter.Entry(window, font=("Arial", 16))
Phonenumber_entry.pack(pady=0, padx=10)

email_label = tkinter.Label(window, text="email", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
email_label.pack(pady=0, padx=10)
email_entry = tkinter.Entry(window, font=("Arial", 16))
email_entry.pack(pady=0, padx=10)

Address_label = tkinter.Label(window, text="Address", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
Address_label.pack(pady=0, padx=10)
Address_entry = tkinter.Entry(window, font=("Arial", 16))
Address_entry.pack(pady=0, padx=10)

district_label = tkinter.Label(window, text="District", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
district_label.pack(pady=0, padx=10)
district_combobox = ttk.Combobox(window, values=("Lipis", "Raub", "Jerantut", "Cameron Highland", "Bentong", "Temerloh", "Jengka", "Kuantan", "Maran", "Rompin", "Bera", "Pekan"))
district_combobox.pack(pady=0, padx=10)

archery_label = tkinter.Label(window, text="Archery Set List", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
archery_label.pack(pady=0, padx=10)
archery_listbox = tkinter.Listbox(window, selectmode=tkinter.MULTIPLE, font=("Arial", 12))
archery_listbox.pack(pady=0, padx=10)

# Adding items to the Archery Set list
archery_items = ["bow 25lbs- rm150", "bow 30lbs- rm200", "bow 35lbs- rm250", "bow 40lbs- rm300", "Arrow 500spine- rm20", "Arrow 600spine- rm30", "Arrow 700spine- rm40", "Arrow 800spine- rm50"]
for item in archery_items:archery_listbox.insert(tkinter.END, item)

Paymentmethod_label = tkinter.Label(window, text="Payment method", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
Paymentmethod_label.pack(pady=0, padx=10)
Paymentmethod_combobox = ttk.Combobox(window, values=("Payment in store", "Cash on delivery"))
Paymentmethod_combobox.pack(pady=0, padx=10)

Total_button = tkinter.Button(window, text="ORDER", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=Total)
Total_button.pack(pady=20, padx=10)

#Order_button = tkinter.Button(window, text="Order now", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=Order)
#Order_button.pack(pady=0, padx=10)


window.mainloop()