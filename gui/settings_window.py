
# This file is responsible for generating and handling events in whole setting menues chain

import tkinter as tk
from tkinter import filedialog, colorchooser, ttk
from PIL import Image
# from core.test_img import print_setting_test_img
from gui.components import DragDropWidget
from gui.ui_updater import update_main_window, update_text_settings_menu
from core.image_processor import GetPic, get_scaled_image
from file_handling.log_debug import print_cmd
from utils.color_utils import color_add_trans_lvl
from file_handling.file_handling import file_manager
from utils.list_util import ListMover





class TopSetting(tk.Toplevel):
    def __init__(self, main_window, parent, settings_container):
        super().__init__(parent)
        # self.root = root
        self.main_window = main_window
        self.parent = parent
        self.setting = settings_container
        self.file_manager = file_manager
        # settings_container.text_to_write = self.parent..w_text.get()
        self.create_widget()


    def create_widget(self):
        # self.setting_menu = tk.Toplevel(self.parent)
        self.title("Settings")
        self.minsize(width=150, height=50)
        self.out_set_btn = tk.Button(
            self, text="Out Setting", command=self.out_setting)
        self.out_set_btn.pack(fill="both", expand=True)
        self.in_set_btn = tk.Button(
            self, text="In Setting", command=self.in_setting)
        self.in_set_btn.pack(fill="both", expand=True)
        

    def out_setting(self):
        if not hasattr(self, 'out_setting_mnu'):
            self.out_setting_mnu = OutSetting(self, self.setting)
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

    def in_setting(self):
        if not hasattr(self, 'in_setting_menu'):
            self.in_setting_menu = InSetting(self, self.setting)
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
        self.setting = settings_container
        self.create_widget()

    def create_widget(self):
        # self.out_setting_mnu = tk.Toplevel(self.parent)
        self.title("Output Setting")
        self.geometry("150x75")
        self.out_path_btn = tk.Button(
            self, text="Output Folder ..", command=self.open_folder)
        self.out_path_btn.pack(fill="both", expand=True)
        self.txt_setting_btn = tk.Button(
            self, text="Text Settings", command=self.open_txt_set_mnu)
        self.txt_setting_btn.pack(fill="both", expand=True)


    def open_folder(self):
        self.path = filedialog.askdirectory()
        print_cmd(f"self.path {self.path}")
        if self.path:
            self.setting.out_path = self.path

    def open_txt_set_mnu(self):
        if not hasattr(self, 'txt_setting_menu'):
            self.txt_setting_menu = TextSetting(self, self.setting)
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
        self.setting = settings_container
        self.create_widget()
        

    def create_widget(self):
        # self.in_setting_mnu = tk.Toplevel(self.parent)
        self.title("Input Setting")
        self.geometry("150x75")
        self.in_folder = tk.Button(
            self, text="Select Folder", command=self.open_folder)
        self.in_folder.pack(fill="both", expand=True)
        self.in_file = tk.Button(
            self, text="Select File", command=self.open_file)
        self.in_file.pack(fill="both", expand=True)

    def open_folder(self):
        self.path = filedialog.askdirectory()
        if self.setting.in_path_dir is None:
            self.setting.file_list = file_manager.get_file_list(self.path, self.setting.allowed_ext)
        else:
            self.setting.file_list = file_manager.set_directory(self.path, self.setting.allowed_ext)
            print_cmd(f"open_folder {self.setting.file_list}")

        self.setting.in_path_dir = self.path
        if self.setting.file_list is not None:
            self.parent.list_mover = ListMover(self.setting.file_list)
            self.setting.in_path_file = self.parent.list_mover.element
            
            

        # self.files = list_files_dir(self.path, self.setting.allowed_ext)
        # self.file_list = ListMover(self.files)
        # print_cmd(f"number of files = {len(self.files)}")
        # if len(self.files) != 0:
        #     self.setting.in_path_file = self.file_list.element
        update_main_window(self.parent.main_window, self.setting)
        # settings_container.in_path_txt = settings_container.in_path
        print_cmd({self.setting.in_path_dir})
        return self.path

    def open_file(self):
        self.path = filedialog.askopenfile()
        if self.path:
            print_cmd(f"{self.path.name}")
            self.setting.in_path_file = self.path.name
        update_main_window(self.parent.main_window, self.setting)
        # self.parent.main_window.path_text.config(text=settings_container.in_path) -- > updating the UI moved to ui_updater.py
        print_cmd({self.setting.in_path_file})


class TextSetting(tk.Toplevel):
    def __init__(self, parent, settings_container):
        super().__init__(parent)
        # self.root = root
        self.setting = settings_container
        # self.main_window = parent.parent.parent
        self.parent = parent
        self.create_widget()
        update_text_settings_menu(self,self.setting)

        # self.txt_setting_mnu = tk.Toplevel(self.parent)

    def create_widget(self):
        self.title("Text Settings")
        self.geometry("500x200")

        # ----- Font Select Combobox -------
        self.fnt_label = ttk.Label(self, text="Select Font:")
        self.fnt_label.grid(column=5, row=7, padx=10, pady=5)
        self.n = tk.StringVar()
        self.fnt_choose = ttk.Combobox(self, width=25, textvariable=self.n)
        self.fnt_choose['values'] = [item[1] for item in self.setting.font_list]
        self.fnt_choose.grid(column=6, row=7, columnspan=3, sticky="w")
        # self.fnt_choose.current(0)
        
        # -----------fire event to set the value of selected font ----
        self.fnt_choose.bind("<<ComboboxSelected>>", lambda event : self.on_font_select(event))
        
        #-------- Sont size selection section --------
        self.fnt_choose_size_label = tk.Label(self, text="Font Size:")
        self.fnt_choose_size_label.grid(column=5, row=8)
        self.fnt_size_spin_var = tk.IntVar(value=self.setting.font_size)
        self.fnt_choose_size_spin = tk.Spinbox(self, from_=10, to=300, width=3, textvariable=self.fnt_size_spin_var,
                                                command=self.font_size_spin_change)
        self.fnt_choose_size_spin.grid(column=6, row=8, sticky="w")

        #----------fire event for set the font size value -------------
        self.fnt_choose_size_spin.bind('<<SpinboxSelected>>', lambda event : self.font_size_spin_change(event))

        # ---- BG and DG color selection and preview section
        self.choos_txt_color = tk.Button(self, text="Choose Text Color",
                                         command=lambda: self.choose_color("Choose Text Color"))
        self.choos_txt_color.grid(column=5, row=11, padx=10, pady=5)
        self.txt_color_label = tk.Label(
            self, text="Sample Text", bg=self.setting.txt_bg_color[1], 
            fg=self.setting.txt_color[1], width=13, height=1)
        self.txt_color_label.grid(column=6, row=11)
        # self.grid_rowconfigure(11, weight=1)
        # self.grid_columnconfigure(7, weight=1)
        self.choos_txt_bg_color = tk.Button(self, text="Choose Background Color", command=lambda: self.choose_color("Choose Background color"))
        self.choos_txt_bg_color.grid(column=8, row=11, padx=10, pady=5)

        # ------------Transparency selection (does not reflected to sample text)
        self.trans_select_label = tk.Label(self, text="Select Transparency Lavel:") 
        self.trans_select_label.grid(column=5, columnspan=3, row=14, padx=10, pady=5)
        self.trans_lvl_var = tk.IntVar(value=self.setting.txt_trans_lvl)
        self.trans_select_spin = tk.Spinbox(self, from_=0, to=255, width=3, textvariable=self.trans_lvl_var,
            command=self.trans_select_spin_change)
        self.trans_select_spin.grid(column=8, row=14, padx=10, pady=5, sticky="w")
        self.pos_button = tk.Button(self, text="Place Text", command=self.drag_drop_text_pos)
        self.pos_button.grid(column=5, row=12)
        update_text_settings_menu(self, self.setting)

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
            '<Control-p>', lambda event: self.prnt_setting(event))
        # update_text_settings_menu(self.parent.txt_setting_menu, settings_container)


    def on_font_select(self, event):
        font_index = self.fnt_choose.current()
        self.setting.choosen_font = self.setting.font_list[font_index][0]
        update_text_settings_menu(self, self.setting)
        
    def choose_color(self, text):
        # color = colorchooser.askcolor("#ffee00" , title=text)
        if "Background" in text:
            color = colorchooser.askcolor(self.setting.txt_bg_color[1], title=text)
            if color[1] != None:
                self.txt_color_label.config(bg=color[1])
                self.setting.txt_bg_color = color
        elif "Text" in text:
            color = colorchooser.askcolor(self.setting.txt_color[1], title=text)
            if color[1] != None:
                self.txt_color_label.config(fg=color[1])
                self.setting.txt_color = color
        self.lift()

    def close_window(self, event=None):
        # self.parent.lift()
        self.parent.close_txt_set_mnu()



    def trans_select_spin_change(self):
        # transparency = self.trans_select_spin.get()
        # print(transparency)
        self.setting.txt_trans_lvl = self.trans_lvl_var.get()

    def font_size_spin_change(self):
        self.setting.font_size = self.fnt_size_spin_var.get()

    def drag_drop_text_pos(self):
        self.drag_drop_window = tk.Toplevel(self)
        self.drag_drop_window.title("Select Text Position")
        self.drag_drop_window.protocol('WM_DELETE_WINDOW', self.close_drag_drop_window)
        self.drag_drop_window.bind("<Escape>", self.close_drag_drop_window)
        fg_color = color_add_trans_lvl(self.setting.txt_color, self.setting.txt_trans_lvl)
        bg_color = color_add_trans_lvl(self.setting.txt_bg_color, self.setting.txt_trans_lvl)
        bg_image = Image.open(self.setting.in_path_file)
        txt_image = GetPic(self.setting.text_to_write, self.setting.choosen_font, 
                           self.setting.font_size, fg_color, bg_color).create_image_from_txt()[0]
        self.scl = 1
        if bg_image.size[0] > 800 or bg_image.size[1] > 600 :
            scaled_image = get_scaled_image(bg_image, 600, sc=True)
            bg_image , self.scl = scaled_image
            print_cmd(f"{bg_image}, {self.scl}")
            txt_image = txt_image.resize((txt_image.size[0] // self.scl, txt_image.size[1] // self.scl))
        self.select_pos_drag_drop = DragDropWidget(self.drag_drop_window, txt_image, bg_image )
        print_cmd(f"drag drop pos is{self.select_pos_drag_drop.position}")
        

    def close_drag_drop_window(self, event=None):
        if hasattr(self, 'drag_drop_window'):
            if self.select_pos_drag_drop.position:
                self.setting.txt_poz = (int(self.select_pos_drag_drop.position[0] * self.scl), int(self.select_pos_drag_drop.position[1] * self.scl))
                print_cmd(f" setting position set to {self.setting.txt_poz}")
            self.drag_drop_window.destroy()
            self.parent.lift()

    def prnt_setting(self, event):
        print_cmd("---------ctrl+p output -------")
        # print(f"text color:{settings_container.txt_color}")
        # print(f"text bg color:{settings_container.txt_bg_color}")
        # print(f"txt trans lvl: {settings_container.txt_trans_lvl}")
        # print(f"font type set to: {settings_container.choosen_font}")
        # print(f"font list 12: {settings_container.font_list[12].lower()+'.ttf'}")
        # print(f"n parameter:{self.n.get()}")
        print_cmd(self.setting)
        # print_cmd(f"{txt_image_watermark(settings_container.in_path_file, settings_container).show()}")
        print_cmd(self.select_pos_drag_drop.position)
        # print(f"font size setting: {settings_container.font_size}")
        print_cmd("-"*10)
        # print_setting_test_img(settings_container)