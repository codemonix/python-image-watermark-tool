import os
import json
from tkinter import filedialog, messagebox
from PIL import Image


def save_settings(settings_container):
    filename = filedialog.asksaveasfile(confirmoverwrite=True)
    try:
        if filename :
            json.dump(settings_container.to_dict(), filename, indent=4)
            return True
        return None
    except Exception as e:
        print(f"file_handling.py 15 -> {e}")
        return False

def load_settings(settings_container):
    filename = filedialog.askopenfile("r")
    try:
        if filename :
            settings_dict = dict(json.load(filename))
            settings_container.set_settings(settings_dict)
    except Exception as e:
        print(f"file_handling 25 -> {e}")
        

        # return settings_dict

def image_save(image, file_path):
    
    image = image.convert('RGB')
    print(f"file_handling.py 26 -> {file_path} ")
    if os.path.exists(file_path):
        if messagebox.askokcancel("Caution", "Do you want to overwrite it?"):
            image.save(file_path)
    else:
        print(f"file_handling.py 33 -> image save else")
        try:
            image.save(file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Could not save the file {e}")

def list_files_dir(dir_path, extensions):
    file_list = []
    if dir_path:
        if os.path.exists(dir_path):
            for root, dir, files in os.walk(dir_path):
                for file in files:
                    if file.endswith(tuple(extensions)):
                        file_list.append(os.path.join(root, file))

            return file_list
    else:
        return False