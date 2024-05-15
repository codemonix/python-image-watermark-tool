# Here is the main entry point of software

import tkinter as tk
from gui.ui_builder import UIBuilder
from utils.settings import DataContainer



def main():
    root = tk.Tk()                              #Create main element of tkinter to build the main UI
    settings_container = DataContainer()            # Create Data Container which carry the settings data throu the software
    builder = UIBuilder(root)                   # Create instance of UI builder
    builder.buil_main_window(settings_container)    # Calling UI builder creator method and passing required setting data
    root.mainloop()


if __name__ == "__main__":
    main()