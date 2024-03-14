import json
from tkinter import messagebox, filedialog
import os

def save_to_json(chef_name, dish_title, price, weight, ingredients, saved_label_folder):
    x = {
        "chef_name" : chef_name,
        "dish_title" : dish_title,
        "price" : price,
        "weight" : weight,
        "ingredients" : ingredients
    }

    json_object = json.dumps(x, indent=4)

    filepath = saved_label_folder + dish_title + "_" + chef_name + ".json"
    
    if os.path.isfile(filepath):
        os.remove(filepath)

    with open(filepath, "a") as outfile:
        outfile.write(json_object)

def load_from_json(saved_labels_folder):
    filepath = filedialog.askopenfilename(
            initialdir = saved_labels_folder, 
            title = "Select a File", 
            filetypes = (("Json files", "*.json"), ("All files", "*.*")))

    with open(filepath, 'r') as openfile:
        j_object = json.load(openfile)
    
    return j_object

def format_title(title_text):
    pass

def format_weight(weight_text, wtype):
    newString = ""
    for char in weight_text:
        for x in range(10):
            if char == str(x):
                newString += char
    return newString + " " + wtype

def format_price(price_text):
    newString = ""
    for char in price_text:
        if char == ".":
            newString += char
        for x in range(10):
            if char == str(x):
                newString += char
    if newString[-1] == "0" and newString[-2] == "0":
        newString = newString.replace(".00", "")
    
    return "$" + newString

def format_ingredients(ingredients_text):
    newtext = ingredients_text.capitalize()
    if "Ingredients" not in newtext:
        newtext = "Ingredients: " + newtext
    return newtext.strip()

def format_date(date):
    date_parts = date.split("-")
    year = date_parts[0]
    year = year[2] + year[3]
    month = date_parts[1]
    if month[0] == "0":
        month = month.replace("0", "")
    day = date_parts[2]
    if day[0] == "0":
        day = day.replace("0", "")
    
    newdate = "exp: " + month + "/" + day + "/" + year

    return newdate

def spell_check(to_check):
    pass

def get_root_path():
    if os.name == "posix":
        blanks_folder = os.path.expanduser("~/Desktop") + "/blanks/"
        saved_labels_folder = os.path.expanduser("~/Desktop") + "/saved_labels/"
        desktop = os.path.expanduser("~/Desktop") + "/"
    elif os.name == "nt":
        blanks_folder = os.environ['USERPROFILE'] + "\\AppData\\Local\\Programs\\Deli Label Maker\\blanks\\"
        saved_labels_folder = os.environ['USERPROFILE'] + "\\AppData\\Local\\Programs\\Deli Label Maker\\saved_labels\\"
        desktop = os.environ['USERPROFILE'] + "\\Desktop"
    else:
        messagebox.showerror("Error", "Unsupported Operating System.")
        exit(0)

    return blanks_folder, saved_labels_folder, desktop

