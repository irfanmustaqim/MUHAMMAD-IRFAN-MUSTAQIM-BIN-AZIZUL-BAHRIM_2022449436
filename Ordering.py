import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'receipt',
}


db_connection = mysql.connector.connect(**db_config)
db_cursor = db_connection.cursor()


def insert_order_to_database(name, table_number, membership_number, code, items):
    try:
        # Insert order details into the database
        query = "INSERT INTO order_receipt (name, table_number, membership_number, code, items) VALUES (%s, %s, %s, %s, %s)"
        values = (name, table_number, membership_number, code, items)
        db_cursor.execute(query, values)
        db_connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
def submit_order(receipt_window, cart_listbox, name, table_number, membership_number, code):
    items = "\n".join(cart_listbox.get(0, tk.END))
    total = calculate_total(cart_listbox, membership_number, code)

    insert_order_to_database(name, table_number, membership_number, code, items)

    result = messagebox.showinfo("Order Submitted", "Your order has been submitted successfully!")

    if result == "ok":
        receipt_window.destroy()
 
def delete_from_cart(cart_listbox):
    selected_item_index = cart_listbox.curselection()
    if selected_item_index:
        cart_listbox.delete(selected_item_index)

def copy_to_cart(item_listbox, cart_listbox):
    selected_item_index = item_listbox.curselection()
    if selected_item_index:
        selected_item = item_listbox.get(selected_item_index)
        cart_listbox.insert(tk.END, selected_item)

def display_items(category, cart_listbox):
    menu_items = {
        "FOOD": {"Nasi goreng kampung": 5.00, "Chinese fried rice": 5.00, "Pattaya fried rice": 5.50},
        "SIDE DISH": {"Chicken Satay (per stick)": 0.60, "Chicken Soup": 10.00, "chicken curry": 10.00},
        "WESTERN": {"Lasagna": 6.00, "Chicken wrap": 6.00, "Tortilla": 6.00},
        "BEVERAGE": {"Mineral": 1.20, "Tea": 1.80, "Coffee": 2.00},
        "DESSERT": {"Ice Cream": 2.00, "Triple Ice cream special": 3.50, "Ice-cream in bread": 3.00},
        "ADD ON": {"Mushroom soup": 6.80,"Onion Ring": 6.00, "Garlic Bread": 6.50}
    }

    item_window = tk.Toplevel()
    item_window.title(f"{category} Menu")
    item_window.geometry("800x600")

    item_listbox = tk.Listbox(item_window, font=("slab serif", 15), height=20)
    item_listbox.pack()

    for item, price in menu_items[category].items():
        item_listbox.insert(tk.END, f"{item}: RM {price:.2f}")

    copy_button = tk.Button(item_window, text="Add to Cart", command=lambda: copy_to_cart(item_listbox, cart_listbox))
    copy_button.pack()

    done_button = tk.Button(item_window, text="Done", command=item_window.destroy)
    done_button.pack()

def place_order(name, table_number, membership_number, code, cart_listbox):
    receipt_window = tk.Toplevel()
    receipt_window.title("Receipt")
    receipt_window.geometry("800x600")

    receipt_label = tk.Label(receipt_window, text=f"Name: {name}\nTable Number: {table_number}\nMembership Number: {membership_number}\nCode: {code}\n\nItems:", font=("slab serif", 15))
    receipt_label.pack()

    receipt_tree = ttk.Treeview(receipt_window, columns=("Item", "Price"), show="headings")
    receipt_tree.heading("Item", text="Item")
    receipt_tree.heading("Price", text="Price")
    receipt_tree.pack()

    for item in cart_listbox.get(0, tk.END):
        item_name, item_price = item.split(":")
        receipt_tree.insert("", "end", values=(item_name.strip(), item_price.strip()))

    total = calculate_total(cart_listbox, membership_number, code)

    total_label = tk.Label(receipt_window, text=f"Total: RM {total:.2f}", font=("slab serif", 15))
    total_label.pack()

    add_more_button = tk.Button(receipt_window, text="Add More", command=lambda: add_more(receipt_window))
    add_more_button.pack()

    submit_button = tk.Button(receipt_window, text="Submit", command=lambda: submit_order(receipt_window, cart_listbox, name, table_number, membership_number, code))
    submit_button.pack()

def submit_order(receipt_window, cart_listbox, name, table_number, membership_number, code):
    total = calculate_total(cart_listbox, membership_number, code)
    items = "\n".join(cart_listbox.get(0, tk.END))

    insert_order_to_database(name, table_number, membership_number, code, items)

    result = messagebox.showinfo("Order Submitted", "Your order has been submitted successfully!")

    if result == "ok":
        receipt_window.destroy()

def add_more(receipt_window):
    receipt_window.destroy()
    start_order()

def calculate_total(cart_listbox, membership_number, code):
    total = sum([float(item.split(":")[1].strip().split(" ")[-1]) for item in cart_listbox.get(0, tk.END)])

    if membership_number == "ISLAMIC":
        total *= 0.8

    if code == "SAKSI25":
        total *= 0.9

    return total

def next_page(name_entry, table_combobox, member_entry, voucher_entry):
    name = name_entry.get()
    table_number = table_combobox.get()
    membership_number = member_entry.get()
    code = voucher_entry.get()

    registration_window.destroy()

    selection_window = tk.Toplevel()
    selection_window.title("Ordering System")
    selection_window.geometry("800x600")

    selection_title = tk.Label(selection_window, text="MENU SELECTION", font=("castellar", 30))
    selection_title.pack()

    cart_listbox = tk.Listbox(selection_window, font=("slab serif", 15), height=10, width=40)
    cart_listbox.pack()

    categories_frame = tk.Frame(selection_window)
    categories_frame.pack(pady=20)
    categories = ["FOOD", "SIDE DISH", "WESTERN", "BEVERAGE", "DESSERT", "ADD ON"]
    for category in categories:
        category_button = tk.Button(categories_frame, text=category, font=("slab serif", 15),
                                   command=lambda cat=category: display_items(cat, cart_listbox))
        category_button.pack(side="left", padx=10)

    delete_button = tk.Button(selection_window, text="Delete from Cart", command=lambda: delete_from_cart(cart_listbox))
    delete_button.pack()

    place_order_button = tk.Button(selection_window, text="Place Order", command=lambda: place_order(name, table_number, membership_number, code, cart_listbox))
    place_order_button.pack()


def start_order():

    global registration_window
    registration_window = tk.Toplevel()
    registration_window.title("Ordering System")
    registration_window.geometry("800x600")

    registration_title = tk.Label(registration_window, text="Registration", font=("castellar", 30))
    registration_title.pack()

    name_label = tk.Label(registration_window, text="Enter your name:", font=("slab serif", 25))
    name_label.pack()
    name_entry = tk.Entry(registration_window, width=50)
    name_entry.pack()

    table_label = tk.Label(registration_window, text="Select table number:", font=('slab serif', 25))
    table_label.pack()
    table_numbers = [str(i) for i in range(1, 51)]
    table_combobox = ttk.Combobox(registration_window, values=table_numbers)
    table_combobox.pack()

    member_label = tk.Label(registration_window, text="Enter your membership number:", font=('slab serif', 25))
    member_label.pack()
    member_entry = tk.Entry(registration_window, width=50)
    member_entry.pack()

    voucher_label = tk.Label(registration_window, text="Enter your code:", font=('slab serif', 25))
    voucher_label.pack()
    voucher_entry = tk.Entry(registration_window, width=50)
    voucher_entry.pack()

    order_type_label = tk.Label(registration_window, text="Select order type:", font=('slab serif', 25))
    order_type_label.pack()
    order_types = ["Dine-In", "Take Away"]
    order_type_combobox = ttk.Combobox(registration_window, values=order_types)
    order_type_combobox.pack()

    next_button = tk.Button(registration_window, text="Next", command=lambda: next_page(name_entry, table_combobox, member_entry, voucher_entry))
    next_button.pack()

# Set the window size to the computer screen
root = tk.Tk()
root.title("Ordering System")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.configure(bg="green")

name_label = tk.Label(root, text="ISLAMIC CHOICE", font=("castellar", 50), bg="green")
name_label.pack(expand=True, fill='both')

start_button = tk.Button(root, text="Start Order", command=start_order, bg="yellow")
start_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

def on_closing():
    db_cursor.close()
    db_connection.close()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
