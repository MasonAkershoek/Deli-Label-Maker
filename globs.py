from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import sqlite3
import sys
from tkinter import messagebox
from tkinter import ttk
import pyglet

_DEV_MODE = True

version = 1.5

OS = sys.platform.lower()


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

blanks_folder = ""

# Data folders
if not _DEV_MODE:
    if OS == "win32":
        data_folder = "C:/ProgramData/DeliLabelMaker/"
    elif OS == "linux" or OS == "darwin":
        data_folder = "/usr/share/DeliLabelMaker/"
    else:
        messagebox.showerror("Error", "Unsupported operating system. Please run this application on Windows, Linux, or MacOS.")
        exit()
else:
    blanks_folder = "blanks/"
# Styles
# buttonStyle = Style()
# recentsButtonStyle = Style()

