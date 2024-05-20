"""This module provides tools to create and manage list of available fonts 
on the system and creates a list of valid fonts to use"""
import matplotlib.font_manager
from PIL import ImageFont
from file_handling.log_debug import print_cmd

def get_font_list():
   
    font_list = []
    for filename in matplotlib.font_manager.findSystemFonts():
        if not 'Emoji' in filename:
            font = ImageFont.truetype(filename)
            name, weight = font.getname()
            font_list.append((filename, name + "(" + weight + ")"))
    return font_list


def get_system_fonts():
    font_list = []
    for filename in matplotlib.font_manager.findSystemFonts():
        if  'Emoji' not in filename:   
            try:
                font = ImageFont.truetype(filename)
                name, weight = font.getname()
                font_list.append((filename, name + "(" + weight + ")"))
            except Exception as e:
                print_cmd(f"{filename} has encountered error {e}")
                continue
    return font_list

