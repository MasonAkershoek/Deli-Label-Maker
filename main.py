import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, Toplevel, END
from tkcalendar import DateEntry
#from pdf_writer import tk_interface
from functions import *
import os
import globs
import screens


def main():
    # Create the main window
    root = tk.Tk()
    globs.root = root
    root.title("Deli Lable Maker")
    root.iconbitmap("icon.ico")
    root.resizable(False, False)

    # Setup Menu Bar
    menubar = tk.Menu(root)
    menubar.add_command(label="About")
    menubar.add_command(label="Main Menu", command=lambda: switch_screen(0))
    menubar.add_command(label="Exit", command=root.quit)
    root.config(menu=menubar)

    # Create screens
    globs.frames.append(screens.MainMenu(root))
    globs.frames.append(screens.LabelManager(root))
    globs.frames.append(screens.LabelMaker(root))

    # Show the main menu
    globs.frames[globs.currentFrame].pack()
    center_window()
    root.mainloop()

main()