from tkinter import *
from tkinter.ttk import *
import sqlite3
import sys
from tkinter import messagebox
import os

_DEV_MODE = False

version = 1.5

OS = sys.platform.lower()


# Application Data
blanks = []
previews = []
kitchenLabs = []
bakeryLabs = []
misLabs = []

if not _DEV_MODE:
    database = sqlite3.connect(os.getenv('APPDATA') + "\\Deli Label Maker\\labels.db")
else:   
    database = sqlite3.connect("labels.db")
cursor = database.cursor()

# Frame Data
loadLabel = ""
currentFrame = 0
frames = []

blanks_folder = ""

# Data folders
if not _DEV_MODE:
    if OS == "win32":
        blanks_folder = "C:\\Program Files (x86)\\Deli Label Maker\\Blanks\\"
    elif OS == "linux" or OS == "darwin":
        blanks_folder = "/usr/share/DeliLabelMaker/"
    else:
        messagebox.showerror("Error", "Unsupported operating system. Please run this application on Windows, Linux, or MacOS.")
        exit()
else:
    blanks_folder = "blanks/"
# Styles
# buttonStyle = Style()
# recentsButtonStyle = Style()

