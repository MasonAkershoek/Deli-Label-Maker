import tkinter as tk
from functions import *
import globs
import screens
import TKinterModernThemes as TKMT

class App(TKMT.ThemedTKinterFrame):
        def __init__(self, theme, mode, usecommandlineargs=True, usethemeconfigfile=True):
            super().__init__("TITLE", theme, mode, usecommandlineargs, usethemeconfigfile)

            # Setup Menu Bar
            menubar = tk.Menu(self.master)
            menubar.add_command(label="About")
            menubar.add_command(label="Main Menu", command=lambda: switch_screen(0))
            menubar.add_command(label="Exit", command=self.master.quit)
            self.master.config(menu=menubar)

            # Create screens
            globs.frames.append(screens.MainMenu(self.master))
            globs.frames.append(screens.LabelManager(self.master))
            globs.frames.append(screens.LabelMaker(self.master))

            # Show the main menu
            globs.frames[globs.currentFrame].pack()
            self.run()
            


if __name__ == "__main__":
        App("sun-valley", "dark")