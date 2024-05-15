import tkinter as tk
from gui.gui import MainApp
from utils.settings import DataContainer


root = tk.Tk()
data_container = DataContainer()
main_app = MainApp(root,data_container)
# print(main_app.settings.in_setting_menu.path)
root.mainloop()