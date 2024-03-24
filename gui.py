import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, Toplevel, END
from tkcalendar import DateEntry
from pdf_writer import tk_interface
from functions import *
import os

def on_submit():
    # Get Values From Entrys
    chef_name = chef_name_entry.get()
    dish_title = dish_title_entry.get()
    price = price_entry.get()
    weight = weight_entry.get()

    price = format_price(price)
    weight = format_weight(weight, weight_type.get())
    experation = format_date(str(experation_entry.get_date()))
    blank = label_type.get()
    ingredients = format_ingredients(ingredients_entry.get('1.0', tk.END))

    save_to_json(chef_name, dish_title, price, weight, ingredients, saved_labels_folder)
    printpath = tk_interface(chef_name, dish_title, price, weight, experation, blank, ingredients, desktop, blanks_folder)
    result_label.config(text="Lables Created.")
    os.startfile(printpath)

def load_json():
    j_object = load_from_json(saved_labels_folder)
    
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

def get_blanks():
    blanks = []
    if len(os.listdir(blanks_folder)) == 0:
            messagebox.showerror("Error", "The blanks folder is empty, please fill it with blanks before trying again.")

    for blank in os.listdir(blanks_folder):
        blanks.append(blank)
    
    blanks.sort()
    return blanks

def open_template_editor_window():
    template_editor = Toplevel(root)
    template_editor.title("Template Editor")
    template_editor.grab_set()

    label_toedit_label = tk.Label(template_editor, text="Label Type: ")
    label_toedit_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

    label_type_toedit = ttk.Combobox(template_editor, state=blanks[0], values=blanks, width=10)
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
    t2.grid(row=3, column=2, padx=10, pady=10)

    t3 = tk.Radiobutton(template_editor, text="No caps", variable=v)
    t3.grid(row=3, column=3, padx=10, pady=10)

def launch_window():
    welcome = Toplevel(root)
    welcome.title("Welcome!")
    welcome.grab_set()

    deli = tk.PhotoImage(file=(rootFolder + "dinnerbell.png"))
    deliLogo = tk.Label(welcome, image=deli)
    deliLogo.deli = deli
    deliLogo.pack()

    lab1 = tk.Label(welcome, text="WELCOME TO DELI LABEL MAKER!", font=("League Gothic Regular", 20))
    lab1.pack()

    lab2 = tk.Label(
         welcome, 
         text=""
    )

def previews():
    preview = Toplevel(root)
    preview.title("Label Previews")

    p1 = tk.PhotoImage(file=(preview_folder + "template_1.png"))
    p2 = tk.PhotoImage(file=(preview_folder + "template_2.png"))
    p3 = tk.PhotoImage(file=(preview_folder + "template_3.png"))
    p4 = tk.PhotoImage(file=(preview_folder + "template_4.png"))
    p5 = tk.PhotoImage(file=(preview_folder + "template_5.png"))

    l1 = tk.Label(preview, text="Label 1")
    l1.grid(row=0, column=0)
    p1Label = tk.Label(preview, image=p1, text="Label 1" )
    p1Label.grid(row=1, column=0, padx=10, pady=10)
    p1Label.p1 = p1

    l2 = tk.Label(preview, text="Label 2")
    l2.grid(row=0, column=1)
    p2Label = tk.Label(preview, image=p2)
    p2Label.grid(row=1, column=1, padx=10, pady=10)
    p1Label.p2 = p2

    l3 = tk.Label(preview, text="Label 3")
    l3.grid(row=2, column=0)
    p3Label = tk.Label(preview, image=p3)
    p3Label.grid(row=3, column=0, padx=10, pady=10)
    p1Label.p3 = p3

    l4 = tk.Label(preview, text="Label 4")
    l4.grid(row=2, column=1)
    p4Label = tk.Label(preview, image=p4)
    p4Label.grid(row=3, column=1, padx=10, pady=10)
    p1Label.p4 = p4

    l5 = tk.Label(preview, text="Label 5")
    l5.grid(row=4, column=0)
    p5Label = tk.Label(preview, image=p5)
    p5Label.grid(row=5, column=0, padx=10, pady=10)
    p1Label.p5 = p5


# Create the main window
root = tk.Tk()
root.title("Deli Lable Maker")

# Check OS
blanks_folder, saved_labels_folder, desktop, rootFolder, preview_folder = get_root_path()

# Get the current templates available in the templates folder
blanks = get_blanks()

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
#----------------------------------------------------------------------
chef_name_label = tk.Label(root, text="Chefs Name: ")
chef_name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

chef_name_entry = tk.Entry(root)
chef_name_entry.grid(row=0, column=1, padx=10, pady=10)
#----------------------------------------------------------------------


# Label and Entry for Dish Title
#----------------------------------------------------------------------
dish_title_label = tk.Label(root, text="Dish Title: ")
dish_title_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

dish_title_entry = tk.Entry(root)
dish_title_entry.grid(row=1, column=1, padx=10, pady=10)
#----------------------------------------------------------------------


# Label and Entry for Price
#----------------------------------------------------------------------
price_label = tk.Label(root, text="Price: ")
price_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

price_entry = tk.Entry(root)
price_entry.grid(row=2, column=1, padx=10, pady=10)
#----------------------------------------------------------------------


# Label and Entry for Weight
#----------------------------------------------------------------------
weight_label = tk.Label(root, text="Weight: ")
weight_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

weight_entry = tk.Entry(root)
weight_entry.grid(row=3, column=1, padx=10, pady=10)
#----------------------------------------------------------------------


# Label and Entry for weight type
#----------------------------------------------------------------------
weight_type_label = tk.Label(root, text="Weight Type: ")
weight_type_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

weight_type = ttk.Combobox(state="OZ", values=weights)
weight_type.grid(row=4, column=1, padx=10, pady=10)
weight_type.current(0)
#----------------------------------------------------------------------


# Label and Entry for Experation Date
#----------------------------------------------------------------------
experation_label = tk.Label(root, text="Experation Date: ")
experation_label.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)

experation_entry = DateEntry(root, width=12, background="darkblue", foreground="white", borderwidth=2)
experation_entry.grid(row=5, column=1, padx=10, pady=10)
#----------------------------------------------------------------------


# Label and Entry for Template
#----------------------------------------------------------------------
label_type_label = tk.Label(root, text="Label Type: ")
label_type_label.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)

label_type = ttk.Combobox( state=blanks[0], values=blanks)
label_type.grid(row=6, column=1, padx=10, pady=10)
label_type.current(2)
#----------------------------------------------------------------------


# Label and Entry for Ingredients
#----------------------------------------------------------------------
ingredients_label = tk.Label(root, text="Ingredients: ")
ingredients_label.grid(row=7, column=0, padx=10, pady=10, sticky=tk.W)

ingredients_entry = tk.Text(root, height=10)
ingredients_entry.grid(row=7, column=1, padx=10, pady=10)
#----------------------------------------------------------------------


# Submit Button
#----------------------------------------------------------------------
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=8, column=0, columnspan=2, pady=10)
#----------------------------------------------------------------------


# Confirm submit label
#----------------------------------------------------------------------
result_label = tk.Label(root, text="")
result_label.grid(row=9, column=0, columnspan=2, pady=10)
#----------------------------------------------------------------------

previews()
#launch_window()
# Tkinter event loop
root.mainloop()