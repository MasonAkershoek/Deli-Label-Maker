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
        filepath = os.environ['USERPROFILE'] + "\\AppData\\Local\\Programs\\Deli Label Maker\\saved_labels\\" + dish_title + "_" + chef_name + ".json" 
    else:
        messagebox.showerror("Error", "Unsupported Operating System.")
        exit(0)
    
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
            initialdir = os.environ['USERPROFILE'] + "\\AppData\\Local\\Programs\\Deli Label Maker\\saved_labels\\", 
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
    newString = ""
    for char in weight_text:
        for x in range(10):
            if char == str(x):
                newString += char
    return newString + " OZ"

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
    return newtext

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