import globs
import os
from tkinter import messagebox
import pdf_writer

def format_date(datefun):
    if datefun == "":
        return ""
    date = str(datefun)
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

def format_ingredients(newtext):
    if newtext == "":
        return ""
    if "Ingredients" not in newtext:
        newtext = "Ingredients: " + newtext
    return newtext.strip()

def format_price(price_text):
    if price_text == "":
        return ""
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

def format_weight(weight_text, wtype):
    if weight_text == "":
        return ""
    newString = ""
    for char in weight_text:
        for x in range(10):
            if char == str(x):
                newString += char
    return (newString + " " + wtype).strip()

def save_label(labelData):
    if labelData["dish title"] == "" or labelData["chef"] == "":
        messagebox.showerror("Error", "Some or all of the fields have been left empty. Please fill out the form completely.")
        return
    globs.cursor.execute("SELECT * FROM labels WHERE dishTitle is ?", (labelData["dish title"],))
    if len(globs.cursor.fetchall()) == 0:
        globs.cursor.execute("INSERT INTO labels (chef,department,dishTitle,price,weight,weightType,description,gf,v,dairyFree,template) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                (
                                    labelData["chef"],
                                    labelData["department"],
                                    labelData["dish title"],
                                    labelData["price"],
                                    labelData["weight"],
                                    labelData["weightType"],
                                    labelData["description"],
                                    labelData["GF"],
                                    labelData["vegan"],
                                    labelData["dairyFree"],
                                    labelData["template"],
                                )
                            )
        messagebox.showinfo("Label Saved", "Label has been saved.")
    else:
        if messagebox.askquestion("Overwrite Label", "This label already exists. Would you like to overwrite it?") == "yes":
            globs.cursor.execute("UPDATE labels SET chef = ?, dishTitle = ?, department = ?, v = ?, gf = ?, dairyFree = ?, price = ?, weight = ?, weightType = ?, template = ?, description = ? WHERE dishTitle = ?",
                                    (
                                        labelData["chef"],
                                        labelData["dish title"],
                                        labelData["department"],
                                        labelData["vegan"],
                                        labelData["GF"],
                                        labelData["dairyFree"],
                                        labelData["price"],
                                        labelData["weight"],
                                        labelData["weightType"],
                                        labelData["template"],
                                        labelData["description"],
                                        labelData["dish title"]
                                    )
                                )
            messagebox.showinfo("Label Saved", "Label has been saved.")
        else:
            return


    globs.database.commit()

def delete_label(label):
    if messagebox.askquestion("Delete Label", "Are you sure you want to delete this label?") == "yes":
        globs.cursor.execute("DELETE FROM labels WHERE dishTitle = ?", (label,))
        globs.database.commit()

def fetch_dish_titles(column_name, department=None):
    tmp = []
    if department:
        query = f"SELECT {column_name} FROM labels WHERE department = '{department}'"
    else:
        query = f"SELECT {column_name} FROM labels"
    globs.cursor.execute(query)
    for row in globs.cursor.fetchall():
        tmp.append(row[0])
    return tmp

def fetch_favorites():
    tmp = []
    globs.cursor.execute("SELECT dishTitle FROM labels WHERE favorite = 1")
    for row in globs.cursor.fetchall():
        tmp.append(row[0])
    return tmp

def check_favorite(label=None):
    if label:
        globs.cursor.execute("SELECT favorite FROM labels WHERE dishTitle = ?", (label,))
        if globs.cursor.fetchall()[0][0] == "1":
            return True
        else:
            return False
    globs.cursor.execute("SELECT dishTitle FROM labels WHERE favorite = 1", )
    if len(globs.cursor.fetchall()) > 0:
        return True
    else:
        return False
    
def set_favorite(label):
    globs.cursor.execute("SELECT favorite FROM labels WHERE dishTitle = ?", (label,))
    if globs.cursor.fetchall()[0][0] == "1":
        globs.cursor.execute("UPDATE labels SET favorite = 0 WHERE dishTitle = ?", (label,))
    else:
        globs.cursor.execute("UPDATE labels SET favorite = 1 WHERE dishTitle = ?", (label,))
    globs.database.commit()
    
def search_labels(search):
    tmp = []
    globs.cursor.execute("SELECT dishTitle FROM labels WHERE dishTitle LIKE ?", (f"%{search}%",))
    for row in globs.cursor.fetchall():
        tmp.append(row[0])
    return tmp

def switch_screen(new):
    globs.frames[globs.currentFrame].onLeave()
    globs.currentFrame = new
    for frame in globs.frames:
        frame.pack_forget()
    globs.frames[new].onEnter()
    globs.frames[new].pack()

def fetch_label(label):
    globs.cursor.execute("SELECT * FROM labels WHERE dishTitle = ?", (label,))
    for row in globs.cursor.fetchall():
        return {
            "chef": row[0],
            "department": row[1],
            "dish title": row[2],
            "price": row[3],
            "weight": row[4],
            "weightType": row[5],
            "description": row[6],
            "GF": row[7],
            "vegan": row[8],
            "dairyFree": row[9],
            "template": row[10],
            "noDate" : "1",
            "date" : ""
        }
    
def create_label(labDat):
    labelData = format_data(labDat)
    tmp = {}
    for x in range(10):
        tmp["t"+str(x+1)] = labelData["dish title"]

    for x in range(10):
        tmp["i"+str(x+1)] = labelData["description"]
    
    for x in range(10):
        tmp["w"+str(x+1)] = labelData["weight"]
    
    for x in range(10):
        tmp["p"+str(x+1)] = labelData["price"]
    
    for x in range(10):
        tmp["e"+str(x+1)] = labelData["date"]
    
    pdf_writer.fill_single_page_pdf(globs.blanks_folder + labelData["template"] + ".pdf", "C:\\Users\\mason\\" + labelData["dish title"] + "_" + labelData["chef"] + ".pdf", tmp)

def format_data(labDat):
    data = labDat
    if data["weightType"] == "LB":
        data["weight"] += " lbs"
    elif data["weightType"] == "OZ":
        data["weight"] += " OZ"
    elif data["weightType"] == "G":
        data["weight"] += " G"
    else:
        data["weight"] = ""
    
    if data["noDate"] == "1":
        data["date"] = ""
    else:
        data["date"] = format_date(data["date"])
    
    data["price"] = format_price(data["price"])
    
    if data["GF"] == "1" or data["vegan"] == "1" or data["dairyFree"] == "1":
        st = "\n\n"
        if data["vegan"] == "1":
            st += "V   "
        if data["GF"] == "1":
            st += "GF   "
        if data["dairyFree"] == "1":
            st += "Dairy Free"
        if len(st) > 3:
            data["description"] += st
    
    data["description"] = format_ingredients(data["description"])

    
    
    return data

def get_blanks():
    if len(os.listdir(globs.blanks_folder)) == 0:
            messagebox.showerror("Error", "The blanks folder is empty, please fill it with blanks before trying again.")

    for blank in os.listdir(globs.blanks_folder):
        globs.blanks.append(blank)