
# This file is responsible for generating and handling events in whole setting menues chain

import tkinter as tk
from tkinter import filedialog, colorchooser, ttk
# from core.test_img import print_setting_test_img
from gui.ui_updater import update_main_window, update_text_settings_menu
from core.image_processor import txt_image_watermark
from utils.log_debug import print_cmd




class TopSetting(tk.Toplevel):
    def __init__(self, main_window, parent, settings_container):
        super().__init__(parent)
        # self.root = root
        self.main_window = main_window
        self.parent = parent
        # settings_container.text_to_write = self.parent..w_text.get()
        self.create_widget(settings_container)


    def create_widget(self, settings_container):
        # self.setting_menu = tk.Toplevel(self.parent)
        self.title("Settings")
        self.minsize(width=150, height=50)
        self.out_set_btn = tk.Button(
            self, text="Out Setting", command=lambda: self.out_setting(settings_container))
        self.out_set_btn.pack(fill="both", expand=True)
        self.in_set_btn = tk.Button(
            self, text="In Setting", command=lambda: self.in_setting(settings_container))
        self.in_set_btn.pack(fill="both", expand=True)
        

    def out_setting(self, settings_container):
        if not hasattr(self, 'out_setting_mnu'):
            self.out_setting_mnu = OutSetting(self, settings_container)
            self.out_setting_mnu.protocol(
                'WM_DELETE_WINDOW', self.close_out_setting)
            self.out_setting_mnu.bind("<Escape>", self.close_out_setting)
        elif hasattr(self, 'out_setting_mnu'):
            self.out_setting_mnu.lift()
        # print("Out Setting")
    # Destroy and close output setting menu

    def close_out_setting(self, event=None):
        if hasattr(self, 'out_setting_mnu'):
            self.out_setting_mnu.destroy()
            del self.out_setting_mnu

    def in_setting(self, settings_container):
        if not hasattr(self, 'in_setting_menu'):
            self.in_setting_menu = InSetting(self, settings_container)
            self.in_setting_menu.protocol('WM_DELETE_WINDOW', self.close_in_setting)
            self.in_setting_menu.bind("<Escape>", self.close_in_setting)
        elif hasattr(self, 'in_setting_menu'):
            self.in_setting_menu.lift()
        
    def close_in_setting(self, event=None):
        if hasattr(self, 'in_setting_menu'):
            self.lift()
            print_cmd("close_in_setting")
            self.in_setting_menu.destroy()
            del self.in_setting_menu


class OutSetting(tk.Toplevel):
    def __init__(self, parent, settings_container):
        super().__init__(parent)
        # self.root = root
        self.main_window = parent.parent
        self.parent = parent
        self.create_widget(settings_container)

    def create_widget(self, settings_container):
        # self.out_setting_mnu = tk.Toplevel(self.parent)
        self.title("Output Setting")
        self.geometry("150x75")
        self.out_path_btn = tk.Button(
            self, text="Output Folder ..", command=lambda: self.open_folder(settings_container))
        self.out_path_btn.pack(fill="both", expand=True)
        self.txt_setting_btn = tk.Button(
            self, text="Text Settings", command=lambda: self.open_txt_set_mnu(settings_container))
        self.txt_setting_btn.pack(fill="both", expand=True)


    def open_folder(self, settings_container):
        self.path = filedialog.askdirectory()
        settings_container.out_path = self.path

    def open_txt_set_mnu(self, settings_container):
        if not hasattr(self, 'txt_setting_menu'):
            self.txt_setting_menu = TextSetting(self, settings_container)
            self.txt_setting_menu.protocol('WM_DELETE_WINDOW', self.close_txt_set_mnu)
            self.txt_setting_menu.bind('<Escape>', self.close_txt_set_mnu)
        elif hasattr(self, 'txt_setting_menu'):
            self.txt_setting_menu.lift()

    def close_txt_set_mnu(self,event=None):
        self.lift()
        self.txt_setting_menu.destroy()
        del self.txt_setting_menu
        


class InSetting(tk.Toplevel):
    def __init__(self, parent, settings_container):
        super().__init__(parent)
        # self.root = root
        # self.main_window = parent.parent
        self.parent = parent
        self.create_widget(settings_container)
        

    def create_widget(self, settings_container):
        # self.in_setting_mnu = tk.Toplevel(self.parent)
        self.title("Input Setting")
        self.geometry("150x75")
        self.in_folder = tk.Button(
            self, text="Select Folder", command=lambda: self.open_folder(settings_container))
        self.in_folder.pack(fill="both", expand=True)
        self.in_file = tk.Button(
            self, text="Select File", command=lambda: self.open_file(settings_container))
        self.in_file.pack(fill="both", expand=True)

    def open_folder(self, settings_container):
        self.path = filedialog.askdirectory()
        settings_container.in_path_dir = self.path
        # settings_container.in_path_txt = settings_container.in_path
        print_cmd({settings_container.in_path_dir})
        return self.path

    def open_file(self, settings_container):
        self.path = filedialog.askopenfile()
        if self.path:
            print_cmd(f"{self.path.name}")
        # if self.path is None:
        #     settings_container.in_path_txt.set(None)
        # else:
        #     settings_container.in_file.set(self.path.name)
        # settings_container.in_path_txt.set(self.path.name)
            settings_container.in_path_file = self.path.name
        update_main_window(self.parent.main_window, settings_container)
        # self.parent.main_window.path_text.config(text=settings_container.in_path) -- > updating the UI moved to ui_updater.py
        print_cmd({settings_container.in_path_file})


class TextSetting(tk.Toplevel):
    def __init__(self, parent, settings_container):
        super().__init__(parent)
        # self.root = root
        self.main_window = parent.parent.parent
        self.parent = parent
        self.create_widget(settings_container)
        update_text_settings_menu(self,settings_container)

        # self.txt_setting_mnu = tk.Toplevel(self.parent)

    def create_widget(self, settings_container):
        self.title("Text Settings")
        self.geometry("500x200")

        # ----- Font Select Combobox -------
        self.fnt_label = ttk.Label(self, text="Select Font:")
        self.fnt_label.grid(column=5, row=7, padx=10, pady=5)
        self.n = tk.StringVar()
        self.fnt_choose = ttk.Combobox(self, width=25, textvariable=self.n)
        self.fnt_choose['values'] = [item[1] for item in settings_container.font_list]
        self.fnt_choose.grid(column=6, row=7, columnspan=3, sticky="w")
        # self.fnt_choose.current(0)
        
        # -----------fire event to set the value of selected font ----
        self.fnt_choose.bind("<<ComboboxSelected>>", lambda event,
                              arg=settings_container: self.on_font_select(event, settings_container))
        
        #-------- Sont size selection section --------
        self.fnt_choose_size_label = tk.Label(self, text="Font Size:")
        self.fnt_choose_size_label.grid(column=5, row=8)
        self.fnt_size_spin_var = tk.IntVar(value=settings_container.font_size)
        self.fnt_choose_size_spin = tk.Spinbox(self, from_=10, to=200, width=3, textvariable=self.fnt_size_spin_var,
                                                command=lambda: self.font_size_spin_change(settings_container))
        self.fnt_choose_size_spin.grid(column=6, row=8, sticky="w")

        #----------fire event for set the font size value -------------
        self.fnt_choose_size_spin.bind('<<SpinboxSelected>>', lambda event, 
                                       arg=settings_container: self.font_size_spin_change(event, settings_container))

        # ---- BG and DG color selection and preview section
        self.choos_txt_color = tk.Button(self, text="Choose Text Color",
                                         command=lambda: self.choose_color(settings_container, "Choose Text Color"))
        self.choos_txt_color.grid(column=5, row=11, padx=10, pady=5)
        self.txt_color_label = tk.Label(
            self, text="Sample Text", bg=settings_container.txt_bg_color[1], 
            fg=settings_container.txt_color[1], width=13, height=1)
        self.txt_color_label.grid(column=6, row=11)
        # self.grid_rowconfigure(11, weight=1)
        # self.grid_columnconfigure(7, weight=1)
        self.choos_txt_bg_color = tk.Button(self, text="Choose Background Color", command=lambda: self.choose_color(
            settings_container, "Choose Background color"))
        self.choos_txt_bg_color.grid(column=8, row=11, padx=10, pady=5)

        # ------------Transparency selection (does not reflected to sample text)
        self.trans_select_label = tk.Label(self, text="Select Transparency Lavel:") 
        self.trans_select_label.grid(column=5, columnspan=3, row=14, padx=10, pady=5)
        self.trans_lvl_var = tk.IntVar(value=settings_container.txt_trans_lvl)
        self.trans_select_spin = tk.Spinbox(self, from_=0, to=255, width=3, textvariable=self.trans_lvl_var,
            command=lambda: self.trans_select_spin_change(settings_container))
        self.trans_select_spin.grid(column=8, row=14, padx=10, pady=5, sticky="w")

        # self.bind("<Escape>", self.close_window)
        # self.trans_select_spin.bind(
        #     '<Configure>', lambda event, arg=settings_container: self.trans_select_spin_change(event, arg))
        # self.txt_bg_color_label = tk.Label(
        #     self.txt_setting_mnu, text="Color", bg=settings_container.txt_bg_color[1], width=4, height=1)  --> removed and displayed in same label
        # self.txt_bg_color_label.grid(column=3, row=15, padx=10, pady=10)
        # self.txt_setting_mnu.protocol(
        # "WM_DELETE_WINDOW", lambda: self.close_window())
        # self.txt_setting_mnu.
        # self.prnt_setting_btn = tk.Button(
        #     self.txt_setting_mnu, text="Print Settings", command=lambda: self.prnt_setting(settings_container))
        # self.prnt_setting_btn.grid(column=0, row=20, padx=10, pady=10)
        self.bind(
            '<Control-p>', lambda event, arg=settings_container: self.prnt_setting(event, arg))
        # update_text_settings_menu(self.parent.txt_setting_menu, settings_container)


    def on_font_select(self, event, settings_container):
        font_index = self.fnt_choose.current()
        settings_container.choosen_font = settings_container.font_list[font_index][0]
        update_text_settings_menu(self, settings_container)
        
    def choose_color(self, settings_container, text):
        # color = colorchooser.askcolor("#ffee00" , title=text)
        if "Background" in text:
            color = colorchooser.askcolor(settings_container.txt_bg_color[1], title=text)
            if color[1] != None:
                self.txt_color_label.config(bg=color[1])
                settings_container.txt_bg_color = color
        elif "Text" in text:
            color = colorchooser.askcolor(settings_container.txt_color[1], title=text)
            if color[1] != None:
                self.txt_color_label.config(fg=color[1])
                settings_container.txt_color = color
        self.lift()

    def close_window(self, event=None):
        # self.parent.lift()
        self.parent.close_txt_set_mnu()



    def trans_select_spin_change(self, settings_container):
        # transparency = self.trans_select_spin.get()
        # print(transparency)
        settings_container.txt_trans_lvl = self.trans_lvl_var.get()

    def font_size_spin_change(self, settings_container):
        settings_container.font_size = self.fnt_size_spin_var.get()

    def prnt_setting(self, event, settings_container):
        print_cmd("---------ctrl+p output -------")
        # print(f"text color:{settings_container.txt_color}")
        # print(f"text bg color:{settings_container.txt_bg_color}")
        # print(f"txt trans lvl: {settings_container.txt_trans_lvl}")
        # print(f"font type set to: {settings_container.choosen_font}")
        # print(f"font list 12: {settings_container.font_list[12].lower()+'.ttf'}")
        # print(f"n parameter:{self.n.get()}")
        print_cmd(settings_container)
        print_cmd(f"{txt_image_watermark(settings_container.in_path_file, settings_container).show()}")
        
        # print(f"font size setting: {settings_container.font_size}")
        print_cmd("-"*10)
        # print_setting_test_img(settings_container)

