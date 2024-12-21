import tkinter as tk
from tkinter import ttk, END
from tkcalendar import DateEntry
from functions import *

# Main Menu
class MainMenu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padx=10,pady=10)
        self.title = tk.Label(self, text="Deli Label Maker", font=("Arial", 24), width=20)
        self.title.pack(padx=10,pady=10)

        self.newLabelButton = tk.Button(self, text="New Label", command=lambda: switch_screen(2))
        self.newLabelButton.pack(padx=10,pady=10)

        self.labelManagerButton = tk.Button(self, text="Label Manager", command=lambda: switch_screen(1))
        self.labelManagerButton.pack(padx=10,pady=10)

        self.maker = tk.Label(self, text=f"Made by Mason Akershoek: Version {globs.version}")
        self.maker.pack(padx=10,pady=10)
    
    def onEnter(self):
        pass

    def onLeave(self):
        pass

# Label Maker
class LabelMaker(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.top = tk.Frame(self)
        self.f1 = ttk.LabelFrame(self.top, text="Who made it and Dish Title")
        self.f2 = ttk.LabelFrame(self.top, text="Food Alergens")
        self.f3 = ttk.LabelFrame(self.top, text="Weight and Price")
        self.f4 = ttk.LabelFrame(self.top, text="Template and Date")
        self.f5 = ttk.LabelFrame(self, text="Dish Description")
        self.f6 = ttk.LabelFrame(self, text="Actions")

        # Chef Name
        self.chefLab = tk.Label(self.f1, text="Chef: ")
        self.chefLab.grid(column=0,row=0,sticky=tk.W, padx=10,pady=10)
        self.chefEntry = tk.Entry(self.f1, width=30)
        self.chefEntry.grid(column=1,row=0, padx=10,pady=10)

        # Dish Title
        self.titleLabel = tk.Label(self.f1, text="Dish Name: ")
        self.titleLabel.grid(column=0, row=1, padx=10, pady=10)
        self.titleEntry = tk.Entry(self.f1, width=30)
        self.titleEntry.grid(column=1,row=1, padx=10, pady=10)

        # Department Selector
        self.departmentVar = tk.StringVar()
        self.departmentVar.set("Kitchen")
        self.departmentLab = tk.Label(self.f1, text="Department: ")
        self.departmentLab.grid(column=0,row=2,sticky=tk.W, padx=10, pady=10)
        self.departmentBox = ttk.Combobox(self.f1, textvariable=self.departmentVar, values=('Kitchen', 'Bakery', 'Misc'), state="readonly")
        self.departmentBox.grid(column=1,row=2, padx=10, pady=10)

        # Food Allergens
        self.veganCheckVar = tk.StringVar()
        self.GFCheckVar = tk.StringVar()
        self.dairyCheckVar = tk.StringVar()
        self.veganCheck = ttk.Checkbutton(self.f2, text="Vegan", variable=self.veganCheckVar)
        self.veganCheck.grid(column=0,row=0,padx=10,pady=10, sticky=tk.W)
        self.GFCheck = ttk.Checkbutton(self.f2, text="GF", variable=self.GFCheckVar)
        self.GFCheck.grid(column=0,row=1,padx=10,pady=10, sticky=tk.W)
        self.dairyCheck = ttk.Checkbutton(self.f2, text="Dairy Free", variable=self.dairyCheckVar)
        self.dairyCheck.grid(column=0,row=2,padx=10,pady=10, sticky=tk.W)

        # Weight and price
        self.priceLab = tk.Label(self.f3, text="Price: ").grid(column=0,row=0,padx=10,pady=10,sticky=tk.W)
        self.priceEntry = tk.Entry(self.f3, width=20)
        self.priceEntry.grid(column=1,row=0, padx=10,pady=10)
        self.weightLab = tk.Label(self.f3, text="Weight: ").grid(column=0, row=1, padx=10,pady=10, sticky=tk.W)
        self.weightEntry = tk.Entry(self.f3, width=20)
        self.weightEntry.grid(column=1, row=1, padx=10,pady=10)
        self.weightTypeLab = tk.Label(self.f3, text="Weight Type: ").grid(column=0,row=2,padx=10,pady=10,sticky=tk.W)
        self.weightTypeVar = tk.StringVar()
        self.weightTypeVar.set("NONE")
        self.weightTypeEntry = ttk.Combobox(self.f3, values=('NONE', 'OZ', 'LB', 'G'), textvariable=self.weightTypeVar, state="readonly")
        self.weightTypeEntry.grid(column=1,row=2,padx=10,pady=10)

        # Template and Date
        self.templateVar = tk.StringVar()
        self.templateVar.set("blank1")
        self.noDateVar = tk.StringVar()
        self.templateLabel = tk.Label(self.f4, text="Template: ").grid(column=0,row=0, padx=10, pady=10, sticky=tk.W)
        self.templateEntry = ttk.Combobox(self.f4, values=('blank1', 'blank2', 'blank3', 'blank4', 'blank5', 'blank6'), textvariable=self.templateVar, state="readonly")
        self.templateEntry.grid(column=1,row=0,padx=10,pady=10)
        self.noDate = ttk.Checkbutton(self.f4, text="No Date", variable=self.noDateVar, state="readonly")
        self.noDate.grid(column=0,row=2,padx=10,pady=10)
        self.dateEntryLab = tk.Label(self.f4, text="Exp Date: ").grid(column=0 , row=1 , padx=10, pady=10, sticky=tk.W)
        self.dateEntry = DateEntry(self.f4, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.dateEntry.grid(column=1, row=1, padx=10, pady=10)

        # Dish Description
        self.dishDescription = tk.Text(self.f5)
        self.dishDescription.grid(column=0,row=0, padx=10, pady=10)


        #Buttons
        self.createLabelButton = tk.Button(self.f6, text="Create Label", command=lambda: create_label(self.getData()))
        self.createLabelButton.grid(column=0,row=0,padx=10,pady=10)
        self.saveLabelButton = tk.Button(self.f6, text="Save Label", command=lambda: save_label(self.getData()))
        self.saveLabelButton.grid(column=0,row=1,padx=10,pady=10)
        self.clearButton = tk.Button(self.f6, text="Clear", command=self.clear)
        self.clearButton.grid(column=0,row=2,padx=10,pady=10)


        self.top.grid(column=0,row=0, padx=10,pady=10, columnspan=15)
        self.f1.grid(column=0,row=0,padx=10,pady=10)
        self.f2.grid(column=1,row=0,padx=10, pady=10)
        self.f3.grid(column=2,row=0,padx=10,pady=10)
        self.f4.grid(column=3,row=0, padx=10,pady=10)
        self.f5.grid(column=0,row=1, padx=10,pady=10)
        self.f6.grid(column=5,row=1,padx=10,pady=10)

    def clear(self):
        self.chefEntry.delete(0, END)
        self.titleEntry.delete(0, END)
        self.departmentBox.set("")
        self.veganCheckVar.set(0)
        self.GFCheckVar.set(0)
        self.dairyCheckVar.set(0)
        self.priceEntry.delete(0, END)
        self.weightEntry.delete(0, END)
        self.weightTypeEntry.set("")
        self.templateEntry.set("")
        self.noDateVar.set(0)
        self.dishDescription.delete(1.0, END)

    def getData(self):
        tmp = {}
        tmp["chef"] = self.chefEntry.get().strip()
        tmp["dish title"] = self.titleEntry.get().strip()
        tmp["department"] = self.departmentVar.get().strip()
        tmp["vegan"] = self.veganCheckVar.get().strip()
        tmp["GF"] = self.GFCheckVar.get().strip()
        tmp["dairyFree"] = self.dairyCheckVar.get().strip()
        tmp["price"] = self.priceEntry.get().strip()
        tmp["weight"] = self.weightEntry.get().strip()
        tmp["weightType"] = self.weightTypeVar.get().strip()
        tmp["template"] = self.templateVar.get().strip()
        tmp["date"] = str(self.dateEntry.get_date()).strip()
        tmp["noDate"] = self.noDateVar.get().strip()
        tmp["description"] = self.dishDescription.get(1.0, END).strip()
        print(tmp)
        return tmp
    
    def setFields(self):
        if len(globs.loadLabel) > 0:
            label = fetch_label(globs.loadLabel)
            self.chefEntry.insert(0, label["chef"])
            self.titleEntry.insert(0, label["dish title"])
            self.departmentBox.set(label["department"])
            self.veganCheckVar.set(label["vegan"])
            self.GFCheckVar.set(label["GF"])
            self.dairyCheckVar.set(label["dairyFree"])
            self.priceEntry.insert(0, label["price"])
            self.weightEntry.insert(0, label["weight"])
            self.weightTypeEntry.set(label["weightType"])
            self.templateEntry.set(label["template"])
            self.dishDescription.insert(1.0, label["description"])
    
    def onLeave(self):
        self.clear()
    
    def onEnter(self):
        self.setFields()
        globs.loadLabel = ""

# Label Manager
class LabelManager(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padx=10,pady=10)

        self.makeFrames()

        self.makeKitchenTab()

        self.makeBakeryTab()

        self.makeFavoritesTab()
        
        self.makeMiscTab()

        self.makeSearchTab()

        # Add To Frame
        self.kitchenListBox.grid(column=0, row=0, padx=10,pady=10)
        self.kitchenActions.grid(column=1, row=0, padx=10,pady=10)
        self.bakeryListBox.grid(column=0, row=0, padx=10,pady=10)
        self.bakeryActions.grid(column=1, row=0, padx=10, pady=10)
        self.favoriteListBox.grid(column=0, row=0, padx=10, pady=10)
        self.favoriteActions.grid(column=1, row=0, padx=10, pady=10)
        self.miscListBox.grid(column=0, row=0, padx=10, pady=10)
        self.miscActions.grid(column=1, row=0, padx=10, pady=10)
        self.searchBar.grid(column=0, row=0, padx=10, pady=10)
        self.searchButton.grid(column=1, row=0, padx=10, pady=10)
        self.searchListBox.grid(column=0, row=1, padx=10, pady=10)
        self.searchActions.grid(column=1, row=1, padx=10, pady=10)
        self.nb.add(self.page1, text="Kitchen")
        self.nb.add(self.page2, text="Bakery")
        self.nb.add(self.page3, text="Misc")
        self.nb.add(self.page4, text="Search")
        self.nb.add(self.page5, text="Favorites")
        self.nb.pack()

    def makeFrames(self):
        self.nb = ttk.Notebook(self)
        self.page1 = tk.Frame(self.nb)
        self.page2 = tk.Frame(self.nb)
        self.page3 = tk.Frame(self.nb)
        self.page4 = tk.Frame(self.nb)
        self.page5 = tk.Frame(self.nb)
        self.kitchenActions = tk.LabelFrame(self.page1, text="Actions")
        self.bakeryActions = tk.LabelFrame(self.page2, text="Actions")
        self.miscActions = tk.LabelFrame(self.page3, text="Actions")
        self.searchActions = tk.LabelFrame(self.page4, text="Actions")
        self.miscActions = tk.LabelFrame(self.page3, text="Actions")
        self.favoriteActions = tk.LabelFrame(self.page5, text="Actions")

    def makeKitchenTab(self):
        # Set up kitchen list
        self.kitchenListBox = tk.Listbox(self.page1, height=20,width=30)
        self.listBoxScroll = tk.Scrollbar(self.kitchenListBox, orient=tk.VERTICAL, command=self.kitchenListBox.yview)
        self.kitchenListBox.configure(yscrollcommand=self.listBoxScroll.set)
        self.populateList(self.kitchenListBox, "Kitchen")

        # set up kitchen action buttons
        self.kbutton1 = tk.Button(self.kitchenActions, text="Edit", command=lambda : self.edit_label(self.kitchenListBox))
        self.kbutton2 = tk.Button(self.kitchenActions, text="Create", command=lambda: self.createLabel(self.kitchenListBox)) # Maybe switch to print
        self.kbutton3 = tk.Button(self.kitchenActions, text="Delete", command=lambda: self.delete_Label(self.kitchenListBox, ))
        self.kbutton4 = tk.Button(self.kitchenActions, text="Favorite", command=lambda: self.setFavorite(self.kitchenListBox))
        self.kbutton1.pack(padx=10,pady=10)
        self.kbutton2.pack(padx=10,pady=10)
        self.kbutton3.pack(padx=10,pady=10)
        self.kbutton4.pack(padx=10,pady=10)

    def makeBakeryTab(self):
        # Set up bakery list
        self.bakeryListBox = tk.Listbox(self.page2, height=20, width=30)
        self.listBoxScroll = tk.Scrollbar(self.bakeryListBox, orient=tk.VERTICAL, command=self.bakeryListBox.yview)
        self.bakeryListBox.configure(yscrollcommand=self.listBoxScroll.set)
        self.populateList(self.bakeryListBox, "Bakery")

        # set up bakery action buttons
        self.bbutton1 = tk.Button(self.bakeryActions, text="Edit", command=lambda : self.edit_label(self.bakeryListBox))
        self.bbutton2 = tk.Button(self.bakeryActions, text="Create", command=lambda: self.createLabel(self.bakeryListBox)) # Maybe switch to print
        self.bbutton3 = tk.Button(self.bakeryActions, text="Delete", command=lambda: self.delete_Label(self.bakeryListBox, "Bakery"))
        self.bbutton4 = tk.Button(self.bakeryActions, text="Favorite", command=lambda: self.setFavorite(self.bakeryListBox))
        self.bbutton1.pack(padx=10,pady=10)
        self.bbutton2.pack(padx=10,pady=10)
        self.bbutton3.pack(padx=10,pady=10)
        self.bbutton4.pack(padx=10,pady=10)

    def makeMiscTab(self):
        # Set up misc list
        self.miscListBox = tk.Listbox(self.page3, height=20, width=30)
        self.listBoxScroll = tk.Scrollbar(self.miscListBox, orient=tk.VERTICAL, command=self.miscListBox.yview)
        self.miscListBox.configure(yscrollcommand=self.listBoxScroll.set)
        self.populateList(self.miscListBox, "Misc")

        # set up misc action buttons
        self.mbutton1 = tk.Button(self.miscActions, text="Edit", command=lambda : self.edit_label(self.miscListBox))
        self.mbutton2 = tk.Button(self.miscActions, text="Create", command=lambda: self.createLabel(self.miscListBox)) # Maybe switch to print
        self.mbutton3 = tk.Button(self.miscActions, text="Delete", command=lambda: self.delete_Label(self.miscListBox))
        self.mbutton4 = tk.Button(self.miscActions, text="Favorite", command=lambda: self.setFavorite(self.miscListBox))
        self.mbutton1.pack(padx=10,pady=10)
        self.mbutton2.pack(padx=10,pady=10)
        self.mbutton3.pack(padx=10,pady=10)
        self.mbutton4.pack(padx=10,pady=10)

    def makeFavoritesTab(self):
        # Set up favorites list
        self.favoriteListBox = tk.Listbox(self.page5, height=20, width=30)
        self.listBoxScroll = tk.Scrollbar(self.favoriteListBox, orient=tk.VERTICAL, command=self.favoriteListBox.yview)
        self.favoriteListBox.configure(yscrollcommand=self.listBoxScroll.set)
        self.populateList(self.favoriteListBox, "Favorites")

        # Set up favorites action buttons
        self.fbutton1 = tk.Button(self.favoriteActions, text="Edit", command=lambda : self.edit_label(self.favoriteListBox))
        self.fbutton2 = tk.Button(self.favoriteActions, text="Create", command=lambda: self.createLabel(self.favoriteListBox)) # Maybe switch to print
        self.fbutton3 = tk.Button(self.favoriteActions, text="Delete", command=lambda: self.delete_Label(self.favoriteListBox))
        self.fbutton4 = tk.Button(self.favoriteActions, text="Unfavorite", command=lambda: self.setFavorite(self.favoriteListBox))
        self.fbutton1.pack(padx=10,pady=10)
        self.fbutton2.pack(padx=10,pady=10)
        self.fbutton3.pack(padx=10,pady=10)
        self.fbutton4.pack(padx=10,pady=10)
    
    def makeSearchTab(self):
        # set up search favorites list
        self.searchListBox = tk.Listbox(self.page4, height=20, width=30)
        self.listBoxScroll = tk.Scrollbar(self.searchListBox, orient=tk.VERTICAL, command=self.searchListBox.yview)
        self.searchListBox.configure(yscrollcommand=self.listBoxScroll.set)
        self.searchListBox.bind("<<ListboxSelect>>", lambda e: self.handleListPress(self.searchListBox))

        # set up search bar
        self.searchBar = tk.Entry(self.page4, width=30)
        self.searchButton = tk.Button(self.page4, text="Search", command=lambda: self.search())

        # set up search action buttons
        self.sbutton1 = tk.Button(self.searchActions, text="Edit", command=lambda : self.edit_label(self.searchListBox))
        self.sbutton2 = tk.Button(self.searchActions, text="Create", command=lambda: self.createLabel(self.searchListBox))
        self.sbutton3 = tk.Button(self.searchActions, text="Delete", command=lambda: self.delete_Label(self.searchListBox))
        self.sbutton4 = tk.Button(self.searchActions, text="Favorite", command=lambda: self.setFavorite(self.searchListBox))
        self.sbutton1.pack(padx=10,pady=10)
        self.sbutton2.pack(padx=10,pady=10)
        self.sbutton3.pack(padx=10,pady=10)
        self.sbutton4.pack(padx=10,pady=10)

    def search(self):
        self.searchListBox.delete(0, tk.END)
        for item in search_labels(self.searchBar.get()):
            self.searchListBox.insert(tk.END, item)

    def populateList(self, listbox, department):
        listbox.pack()
        if department == "Favorites":
            for item in fetch_favorites():
                listbox.insert(tk.END, item)
        else:
            for item in fetch_dish_titles("dishTitle", department):
                listbox.insert(tk.END, item)
        listbox.bind("<<ListboxSelect>>", lambda e: self.handleListPress(listbox))

    def setFavorite(self, listbox):
        set_favorite(listbox.get(listbox.curselection()))
        self.handleListPress(listbox)
        self.refrechAll()

    def handleListPress(self, listbox):
        if listbox.curselection() != ():
            if check_favorite(listbox.get(listbox.curselection())):
                self.bbutton4.config(text="Unfavorite")
                self.kbutton4.config(text="Unfavorite")
                self.mbutton4.config(text="Unfavorite")
                self.sbutton4.config(text="Unfavorite")
            else:
                self.bbutton4.config(text="Favorite")
                self.kbutton4.config(text="Favorite")
                self.mbutton4.config(text="Favorite")
                self.sbutton4.config(text="Favorite")

    def refreshList(self, listbox, department):
        listbox.delete(0, tk.END)
        if department == "favorites":
            for item in fetch_favorites():
                listbox.insert(tk.END, item)
        else:
            for item in fetch_dish_titles("dishTitle", department):
                listbox.insert(tk.END, item)
    
    def refrechAll(self):
        self.refreshList(self.kitchenListBox, "Kitchen")
        self.refreshList(self.bakeryListBox, "Bakery")
        self.refreshList(self.favoriteListBox, "favorites")
        self.refreshList(self.miscListBox, "Misc")

    def delete_Label(self, listBox):
        if listBox.curselection() != ():
            selection = listBox.get(listBox.curselection())
            delete_label(selection)
            self.refrechAll()
    
    def edit_label(self, listBox):
        if listBox.curselection() != ():
            globs.loadLabel = listBox.get(listBox.curselection())
            switch_screen(2)

    def createLabel(self, listBox):
        create_label(fetch_label(listBox.get(listBox.curselection())))
    
    def onEnter(self):
        self.refrechAll()

    def onLeave(self):
        pass
            

