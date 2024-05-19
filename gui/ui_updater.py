
from PIL import Image, ImageTk, ImageFont
from core.image_processor import get_scaled_image, txt_image_watermark
from tkinter import font
import tkinter as tk
from file_handling.log_debug import print_cmd


def update_main_window(main_window, settings_container):
    # image = Image.open(settings_container.in_path_file)
    image = txt_image_watermark(settings_container.in_path_file, settings_container)
    photo = ImageTk.PhotoImage(get_scaled_image(image, 600))
    # path_text_style = font.Font(family=settings_container.choosen_font, 
    #                             size=settings_container.font_size)
    main_window.path_text.config(text=settings_container.in_path_file.rsplit('/', 1)[1])
    # main_window.path_text.config(font=path_text_style)
    main_window.pic_label.configure(image=photo)
    main_window.image = photo
    print_cmd(f"{main_window.w_text.get()}, {main_window.placeholder_text}")
    if main_window.w_text.get() != main_window.placeholder_text:
        main_window.w_text.delete(0, tk.END)
    print_cmd(settings_container)
    if settings_container.text_to_write != "":
        main_window.w_text.delete(0, tk.END)
        main_window.w_text.insert(0, settings_container.text_to_write)
        main_window.w_text.config(fg='black')
        print_cmd("Entry text black")
    # elif settings_container.text_to_write == "":
    #     main_window.w_text.delete(0, tk.END)

def update_text_settings_menu(text_setting_menu, settings_container):
    my_font = ImageFont.truetype(settings_container.choosen_font)
    font_list = [t[0] for t in settings_container.font_list]
    my_font_index = font_list.index(settings_container.choosen_font)
    text_setting_menu.fnt_choose.current(my_font_index)
    font_name , weight = my_font.getname()
    # sample_text_style = font.Font(family=settings_container.choosen_font)
    text_setting_menu.txt_color_label.config(font=(font_name, 14), fg=settings_container.txt_color[1], 
                                             bg=settings_container.txt_bg_color[1])
    
def next_pic(files, settings_container):
    pass

def previous_pic(files, settings_container):
    pass