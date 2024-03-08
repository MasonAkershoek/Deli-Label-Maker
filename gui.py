import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog, END
from main import tk_interface
import os
import json

def on_submit():
    chef_name = chef_name_entry.get()
    dish_title = dish_title_entry.get()
    weight = weight_entry.get()
    blank = label_type.get()
    ingredients = ingredients_entry.get('1.0', tk.END)
    save_to_json(chef_name, dish_title, weight, ingredients)
    tk_interface(chef_name, dish_title, weight, blank, ingredients)
    result_label.config(text="Lables Created.")

def save_to_json(chef_name, dish_title, weight, ingredients):
    x = {
        "chef_name" : chef_name,
        "dish_title" : dish_title,
        "weight" : weight,
        "ingredients" : ingredients
    }

    json_object = json.dumps(x, indent=4)

    if os.name == "posix":
        filepath = os.path.expanduser("~/Desktop") + "/saved_labels/" + dish_title + "_" + chef_name + ".json"
    elif os.name == "nt":
        filepath = os.environ['USERPROFILE'] + "\\Desktop\\saved_lables\\" + dish_title + "_" + chef_name + ".json" 
    else:
        messagebox.showerror("Error", "Unsupported Operating System.")
        exit(0)

    with open(filepath, "a") as outfile:
        outfile.write(json_object)

def load_from_json():
    if os.name == "posix":
        filepath = filedialog.askopenfilename(
            initialdir = os.path.expanduser("~/Desktop") + "/saved_labels", 
            title = "Select a File", 
            filetypes = (("Json files", "*.json"), ("All files", "*.*")))
    elif os.name == "nt":
        filepath = filedialog.askopenfilename(
            initialdir = os.environ['USERPROFILE'] + "\\Desktop\\saved_lables", 
            title = "Select a File", 
            filetypes = (("Json files", "*.json"), ("All files", "*.*")))
    else:
        messagebox.showerror("Error", "Unsupported Operating System.")
        exit(0)

    with open(filepath, 'r') as openfile:
        j_object = json.load(openfile)
    
    chef_name_entry.delete(0, END)
    chef_name_entry.insert(0, j_object["chef_name"])
    dish_title_entry.delete(0, END)
    dish_title_entry.insert(0, j_object["dish_title"])
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
        if not os.path.isdir(os.environ['USERPROFILE'] + "\\Desktop\\blanks"):
            if messagebox.askyesno("Error", "The Directory containing the blanks does not exist, would you like to create one?"):
                os.mkdir(os.environ['USERPROFILE'] + "\\Desktop\\blanks")
            else:
                messagebox.showerror("Error", "blanks folder not found please create and fill one before trying again.")
                exit(0)
        if not os.path.isdir(os.environ['USERPROFILE'] + "\\Desktop\\saved_labels"):
            os.mkdir(os.environ['USERPROFILE'] + "\\Desktop\\saved_labels")
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
    

# Create the main window
root = tk.Tk()
root.title("Deli Lable Maker")


check_dirs()
blanks = get_blanks()

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=load_from_json)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
root.config(menu=menubar)

# Create and place the text fields
chef_name_label = tk.Label(root, text="Chefs Name: ")
chef_name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

chef_name_entry = tk.Entry(root)
chef_name_entry.grid(row=0, column=1, padx=10, pady=10)


dish_title_label = tk.Label(root, text="Dish Title: ")
dish_title_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

dish_title_entry = tk.Entry(root)
dish_title_entry.grid(row=1, column=1, padx=10, pady=10)


weight_label = tk.Label(root, text="Weight: ")
weight_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

weight_entry = tk.Entry(root)
weight_entry.grid(row=2, column=1, padx=10, pady=10)

label_type_label = tk.Label(root, text="Label Type: ")
label_type_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

label_type = ttk.Combobox( state=blanks[0], values=blanks)
label_type.grid(row=3, column=1, padx=10, pady=10)

ingredients_label = tk.Label(root, text="Ingredients: ")
ingredients_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

ingredients_entry = tk.Text(root)
ingredients_entry.grid(row=4, column=1, padx=10, pady=10)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=5, column=0, columnspan=2, pady=10)

# Create and place a label for displaying the result
result_label = tk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()