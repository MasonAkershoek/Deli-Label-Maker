from tkinter import *
from tkinter.ttk import *
import sqlite3

_DEV_MODE = True

version = 1.5

OS = ""

# Application Data
blanks = []
previews = []
kitchenLabs = []
bakeryLabs = []
misLabs = []
database = sqlite3.connect("labels.db")
cursor = database.cursor()

# Frame Data
loadLabel = ""
currentFrame = 0
frames = []

# Data folders
blanks_folder = "blanks/"

# Styles
# buttonStyle = Style()
# recentsButtonStyle = Style()

