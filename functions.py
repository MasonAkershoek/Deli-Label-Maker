import json
from tkinter import messagebox, filedialog
import os

def save_to_json(chef_name, dish_title, price, weight, ingredients):
    x = {
        "chef_name" : chef_name,
        "dish_title" : dish_title,
        "price" : price,
        "weight" : weight,
        "ingredients" : ingredients
    }

    json_object = json.dumps(x, indent=4)

    if os.name == "posix":
        filepath = os.path.expanduser("~/Desktop") + "/saved_labels/" + dish_title + "_" + chef_name + ".json"
    elif os.name == "nt":
        filepath = os.environ['USERPROFILE'] + "\\DeliLabelMaker\\saved_labels\\" + dish_title + "_" + chef_name + ".json" 
    else:
        messagebox.showerror("Error", "Unsupported Operating System.")
        exit(0)
    
    print(filepath)
    if os.path.isfile(filepath):
        os.remove(filepath)

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
            initialdir = os.environ['USERPROFILE'] + "\\DeliLabelMaker\\saved_labels", 
            title = "Select a File", 
            filetypes = (("Json files", "*.json"), ("All files", "*.*")))
    else:
        messagebox.showerror("Error", "Unsupported Operating System.")
        exit(0)

    with open(filepath, 'r') as openfile:
        j_object = json.load(openfile)
    
    return j_object

def format_title(title_text):
    pass

def format_weight(weight_text):
    pass

def format_price(price_text):
    if '$' in price_text:
        price_text.replace("$", "")

def format_ingredients(ingredients_text):
    pass

def spell_check(to_check):
    pass