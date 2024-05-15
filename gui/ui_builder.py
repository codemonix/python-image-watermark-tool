import tkinter as tk
from gui.main_window import MainWindow



class UIBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("Water Marker")
        self.root.minsize(width=510, height=565)


    def buil_main_window(self, settings_container):
        self.main_window = MainWindow(self.root, settings_container)