import tkinter as tk
from tkinter import font
from utils.font_utils import get_font_list
from file_handling.log_debug import print_cmd






class DataContainer:
    _instance = None

    default_settings = {
        "In Path Dir": "",
        "File List": None ,
        "In Path File": "./resources/img/600x500.jpg",
        "Out Path": "./resources/temp",
        "Font List" : get_font_list(),
        "Choosen Font": get_font_list()[0],
        "Font Size": 150 ,
        "Text Pos.": (50, 100),
        "Watermarked Text": "",
        "Allowed Filetypes": ["jpg", "png"],
        "Text Color": ((0, 0, 0), '#000000'),
        "Text Background Color": ((255, 255, 255), '#ffffff'),
        "Transparency Level": 255


    }
    # singleton pattern for setting as it should be same accross the software
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.in_path_dir = cls.default_settings["In Path Dir"]
            cls.file_list = cls.default_settings["File List"]
            cls.in_path_file = cls.default_settings["In Path File"]
            cls.out_path = cls.default_settings["Out Path"]
            cls.font_list = get_font_list()
            cls.choosen_font = cls.font_list[0][0]
            cls.font_size = cls.default_settings["Font Size"]
            cls.txt_poz = cls.default_settings["Text Pos."]
            cls.text_to_write = cls.default_settings["Watermarked Text"]
            cls.allowed_ext = cls.default_settings["Allowed Filetypes"]
            cls.txt_color = cls.default_settings["Text Color"]
            cls.txt_bg_color = cls.default_settings["Text Background Color"]
            cls.txt_trans_lvl = cls.default_settings["Transparency Level"]
        return cls._instance

    def __init__(self):
        pass

    def set_settings(self, settings_dict):
        self.in_path_dir = settings_dict["In Path Dir"]
        self.file_list = settings_dict["File List"]
        self.in_path_file = settings_dict["In Path File"]
        self.out_path = settings_dict["Out Path"]
        self.font_list = get_font_list()
        self.choosen_font = settings_dict["Choosen Font"]
        self.font_size = settings_dict["Font Size"]
        self.txt_poz = tuple(settings_dict["Text Pos."])
        self.text_to_write = settings_dict["Watermarked Text"]
        self.allowed_ext = settings_dict["Allowed Filetypes"]
        self.txt_color = (tuple(settings_dict["Text Color"][0]), settings_dict["Text Color"][1])
        self.txt_bg_color = (tuple(settings_dict["Text Background Color"][0]), settings_dict["Text Background Color"][1])
        self.txt_trans_lvl = settings_dict["Transparency Level"]
        print_cmd("End of set settings")
        return True

    def to_dict(self) -> dict:
                
        self.current_setting ={"In Path Dir": self.in_path_dir,
        "File List": self.file_list,
        "In Path File": self.in_path_file,
        "Out Path": self.out_path,
        "Choosen Font" : self.choosen_font,
        "Font Size": self.font_size ,
        "Text Pos.": self.txt_poz,
        "Watermarked Text": self.text_to_write,
        "Allowed Filetypes": self.allowed_ext,
        "Text Color": self.txt_color,
        "Text Background Color": self.txt_bg_color,
        "Transparency Level": self.txt_trans_lvl,}

        return self.current_setting

    def __str__(self) -> str:
        self.current_setting ={"In Path Dir": self.in_path_dir,
            "File List": self.file_list,
            "In Path File": self.in_path_file,
            "Out Path": self.out_path,
            "Choosen Font" : self.choosen_font,
            "Font Size": self.font_size ,
            "Text Pos.": self.txt_poz,
            "Watermarked Text": self.text_to_write,
            "Allowed Filetypes": self.allowed_ext,
            "Text Color": self.txt_color,
            "Text Background Color": self.txt_bg_color,
            "Transparency Level": self.txt_trans_lvl,}
        
        return str(self.current_setting)
