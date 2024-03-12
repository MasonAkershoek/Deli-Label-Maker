import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, Toplevel, END
from pdf_writer import tk_interface
from functions import *
import os

def on_submit():
    chef_name = chef_name_entry.get()
    dish_title = dish_title_entry.get()
    price = price_entry.get()
    format_price(price)
    weight = weight_entry.get().upper()
    blank = label_type.get()
    ingredients = ingredients_entry.get('1.0', tk.END)
    save_to_json(chef_name, dish_title, price, weight, ingredients)
    tk_interface(chef_name, dish_title, price, weight, blank, ingredients)
    result_label.config(text="Lables Created.")

def load_json():
    j_object = load_from_json()
    
    chef_name_entry.delete(0, END)
    chef_name_entry.insert(0, j_object["chef_name"])

    dish_title_entry.delete(0, END)
    dish_title_entry.insert(0, j_object["dish_title"])

    price_entry.delete(0, END)
    price_entry.insert(0, j_object["price"])

    weight_entry.delete(0, END)
    weight_entry.insert(0, j_object["weight"])
    
    ingredients_entry.delete("1.0", END)
    ingredients_entry.insert("1.0", j_object["ingredients"])

def check_dirs():
    if os.name == "posix":
        if not os.path.isdir(os.path.expanduser("~/Desktop") + "/blanks"):
            if messagebox.askyesno("Error", "The Directory containing the blanks does not exist, would you like to create one?"):
                os.mkdir(os.path.expanduser("~/Desktop") + "/blanks")
            else:
                messagebox.showerror("Error", "blanks folder not found please create and fill one before trying again.")
                exit(1)
        if not os.path.isdir(os.path.expanduser("~/Desktop") + "/saved_labels"):
            os.mkdir(os.path.expanduser("~/Desktop") + "/saved_labels")
    elif os.name == "nt":
        if not os.path.isdir(os.environ['USERPROFILE'] + "\\DeliLabelMaker\\blanks"):
            if messagebox.askyesno("Error", "The Directory containing the blanks does not exist, would you like to create one?"):
                os.mkdir(os.environ['USERPROFILE'] + "\\DeliLabelMaker\\blanks")
            else:
                messagebox.showerror("Error", "blanks folder not found please create and fill one before trying again.")
                exit(0)
        if not os.path.isdir(os.environ['USERPROFILE'] + "\\DeliLabelMaker\\saved_labels"):
            os.mkdir(os.environ['USERPROFILE'] + "\\DeliLabelMaker\\saved_labels")
    else:
        messagebox.showerror("Error", "Unsupported Operating System.")
        exit(0)

def get_blanks():
    blanks = []
    if os.name == "posix":
        if len(os.listdir(os.path.expanduser("~/Desktop/blanks"))) == 0:
            messagebox.showerror("Error", "The blanks folder is empty, please fill it with blanks before trying again.")

        for blank in os.listdir(os.path.expanduser("~/Desktop/blanks")):
            blanks.append(blank)
    elif os.name == "nt":
        if len(os.listdir(os.environ['USERPROFILE'] + "\\Desktop\\blanks")) == 0:
            messagebox.showerror("Error", "The blanks folder is empty, please fill it with blanks before trying again.")

        for blank in os.listdir(os.environ['USERPROFILE'] + "\\Desktop\\blanks"):
            blanks.append(blank)

    return blanks

def open_template_editor_window():
    template_editor = Toplevel(root)
    template_editor.title("Template Editor")
    template_editor.grab_set()

    label_toedit_label = tk.Label(template_editor, text="Label Type: ")
    label_toedit_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

    label_type_toedit = ttk.Combobox(template_editor, state=blanks[0], values=blanks)
    label_type_toedit.grid(row=1, column=1, padx=10, pady=10)

    title_options_label = tk.Label(template_editor, text="Title Options: ")
    title_options_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

    v = tk.IntVar()
    v.set(1)

    t1_label = tk.Label(template_editor, text="Capitalizaton")
    t1_label.grid(row=2, column=1, padx=10, pady=10)

    t1 = tk.Radiobutton(template_editor, text="All Caps", variable=v)
    t1.grid(row=3, column=1, padx=10, pady=10)

    t2 = tk.Radiobutton(template_editor, text="Every first letter capitalized", variable=v)
    t2.grid(row=3, column=1, padx=10, pady=10)

    t3 = tk.Radiobutton(template_editor, text="No caps", variable=v)
    t3.grid(row=3, column=1, padx=10, pady=10)

print(__file__)

# Create the main window
root = tk.Tk()
root.title("Deli Lable Maker")

# Check to make sure all required directorys exsist
check_dirs()

# Get the current templates available in the templates folder
blanks = get_blanks()

# Weight types
weights = ["OZ", "LB", "G"]

# Setting up the menu bar
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Load", command=load_json)
#filemenu.add_separator()
#filemenu.add_command(label="Import Template", command=None)
#filemenu.add_command(label="Edit Templates", command=open_template_editor_window)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
root.config(menu=menubar)

# Label and Entry for Chefs Name
chef_name_label = tk.Label(root, text="Chefs Name: ")
chef_name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

chef_name_entry = tk.Entry(root)
chef_name_entry.grid(row=0, column=1, padx=10, pady=10)

# Label and Entry for Dish Title
dish_title_label = tk.Label(root, text="Dish Title: ")
dish_title_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

dish_title_entry = tk.Entry(root)
dish_title_entry.grid(row=1, column=1, padx=10, pady=10)

# Label and Entry for Price
price_label = tk.Label(root, text="Price: ")
price_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

price_entry = tk.Entry(root)
price_entry.grid(row=2, column=1, padx=10, pady=10)

# Label and Entry for Weight
weight_label = tk.Label(root, text="Weight: ")
weight_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

weight_entry = tk.Entry(root)
weight_entry.grid(row=3, column=1, padx=10, pady=10)

# Entry for Weight Type
#weight_type = ttk.Combobox(state="OZ", values=weights)
#weight_type.grid(row=3, column=2, padx=10, pady=10)

# Label and Entry for Template
label_type_label = tk.Label(root, text="Label Type: ")
label_type_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

label_type = ttk.Combobox( state=blanks[0], values=blanks)
label_type.grid(row=4, column=1, padx=10, pady=10)

# Label and Entry for Ingredients
ingredients_label = tk.Label(root, text="Ingredients: ")
ingredients_label.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)

ingredients_entry = tk.Text(root)
ingredients_entry.grid(row=5, column=1, padx=10, pady=10)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10)

# Confirm submit label
result_label = tk.Label(root, text="")
result_label.grid(row=7, column=0, columnspan=2, pady=10)

# Tkinter event loop
root.mainloop()