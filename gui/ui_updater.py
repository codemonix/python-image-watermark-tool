
from PIL import Image, ImageTk, ImageFont
from core.image_processor import get_scaled_image
from tkinter import font


def update_main_window(main_window, settings_container):
    image = Image.open(settings_container.in_path_file)
    photo = ImageTk.PhotoImage(get_scaled_image(image, 500))
    # path_text_style = font.Font(family=settings_container.choosen_font, 
    #                             size=settings_container.font_size)
    main_window.path_text.config(text=settings_container.in_path_file.rsplit('/', 1)[1])
    # main_window.path_text.config(font=path_text_style)
    main_window.pic_label.configure(image=photo)
    main_window.image = photo

def update_text_settings_menu(text_setting_menu, settings_container):
    my_font = ImageFont.truetype(settings_container.choosen_font)
    font_list = [t[0] for t in settings_container.font_list]
    my_font_index = font_list.index(settings_container.choosen_font)
    text_setting_menu.fnt_choose.current(my_font_index)
    font_name , weight = my_font.getname()
    # sample_text_style = font.Font(family=settings_container.choosen_font)
    text_setting_menu.txt_color_label.config(font=(font_name, 14), fg=settings_container.txt_color[1], 
                                             bg=settings_container.txt_bg_color[1])
    
