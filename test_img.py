from PIL import Image, ImageDraw, ImageFont
from utils.settings import DataContainer
from core.image_processor import txt_image_watermark
import tkinter as tk


# img_proc = ImageComposer

root = tk.Tk()
settings_container = DataContainer()
def print_setting_test_img(settings_container):
    # settings_container.font_type.get()
    pass

print(f"test_img.py 9 font is {settings_container.choosen_font}")

txt_image_watermark(settings_container)


