import tkinter as tk
from functions import *
import globs
import screens
import TKinterModernThemes as TKMT

class App(TKMT.ThemedTKinterFrame):
        def __init__(self, theme, mode, usecommandlineargs=True, usethemeconfigfile=True):
            super().__init__("Deli Label Maker", theme, mode, usecommandlineargs, usethemeconfigfile)
            self.root.iconbitmap("icon.ico")
            self.root.geometry("1158x684")

            # Setup Menu Bar
            menubar = tk.Menu(self.master)
            menubar.add_command(label="Main Menu", command=lambda: switch_screen(0))
            menubar.add_command(label="Help", command=open_help)
            menubar.add_command(label="Exit", command=self.master.quit)
            self.master.config(menu=menubar)

            # Create screens
            globs.frames.append(screens.MainMenu(self.master))
            globs.frames.append(screens.LabelManager(self.master))
            globs.frames.append(screens.LabelMaker(self.master))

            # Show the main menu
            globs.frames[globs.currentFrame].pack(fill=tk.BOTH, expand=1)
            self.run()
            


if __name__ == "__main__":
        App("sun-valley", "dark")