# Here is the main entry point of software

import tkinter as tk
from gui.ui_builder import UIBuilder
from utils.settings import DataContainer

def main():
    """ This will bildup the main elemnts of the app"""
    #Create main element of tkinter to build the main UI
    root = tk.Tk()
    # Create Data Container which carry the settings data throu the software                        
    settings_container = DataContainer()
    # Create instance of UI builder
    builder = UIBuilder(root)
    # Calling UI builder creator method and passing required setting data
    builder.buil_main_window(settings_container)    
    root.mainloop()


if __name__ == "__main__":
    main()
