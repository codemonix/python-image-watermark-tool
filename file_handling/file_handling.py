""" This module handles all file related functionalities including save
, load, get file list from a directory and ..."""

import os
import json
from tkinter import filedialog, messagebox
from file_handling.log_debug import print_cmd

class FileManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FileManager, cls).__new__(cls)
            cls._instance._file_list = None
        return cls._instance
    
    def get_file_list(self, dir_path, extensions):
        if self._file_list is None:
            self._create_file_list(dir_path, extensions)
            
        return self._file_list
    def set_directory(self,dir_path, extensions):
        self._file_list= self._create_file_list(dir_path, extensions)
        return self._file_list

    def _create_file_list(self, dir_path, extensions):
        self._file_list = []
        if dir_path:
            if os.path.exists(dir_path):
                for root, dir, files in os.walk(dir_path):
                    for file in files:
                        if file.endswith(tuple(extensions)):
                            self._file_list.append(os.path.join(root, file))

                return self._file_list
            self._file_list = None
            return self._file_list
        else:
            return False

    def save_settings(self, settings_container):
        filename = filedialog.asksaveasfile(confirmoverwrite=True)
        try:
            if filename :
                json.dump(settings_container.to_dict(), filename, indent=4)
                return True
            return None
        except Exception as e:
            print_cmd(e)
            return False

    def load_settings(self, settings_container):
        filename = filedialog.askopenfile("r")
        try:
            if filename :
                settings_dict = dict(json.load(filename))
                print_cmd("inside load_setting")
                settings_container.set_settings(settings_dict)
                return True
        except Exception as e:
            print_cmd(f" -> {e}")
            return e
        
    def image_save(self, image, file_path):
        image = image.convert('RGB')
        print_cmd(f"file_handling.py 26 -> {file_path} ")
        if os.path.exists(file_path):
            if messagebox.askokcancel("Caution", "Do you want to overwrite it?"):
                image.save(file_path)
        else:
            print_cmd("image save else")
            try:
                image.save(file_path)
            except Exception as e:
                messagebox.showerror("Error", f"Could not save the file {e}")


file_manager = FileManager()

  