
import matplotlib.font_manager
from PIL import ImageFont

def get_font_list():
   
    font_list = []
    # print(matplotlib.font_manager.get_font_names())
    for filename in matplotlib.font_manager.findSystemFonts():
    # print(filename)
        if not 'Emoji' in filename:
            font = ImageFont.truetype(filename)
            name, weight = font.getname()
            font_list.append((filename, name + "(" + weight + ")"))
    return font_list

# font_name = 'Arial'  # Replace with the font name you're looking for




def get_system_fonts():
    font_list = []
    # print(matplotlib.font_manager.get_font_names())
    for filename in matplotlib.font_manager.findSystemFonts():
        # print(filename)
        if  'Emoji' not in filename:  #not 
            try:
                font = ImageFont.truetype(filename)
                name, weight = font.getname()
                font_list.append((filename, name + "(" + weight + ")"))
                # print(font_list)

            except Exception as e:
                print(f"{filename} has encountered error {e}")

                continue
    return font_list

# names = [name for (_ , name) in get_system_fonts()]

# get_system_fonts()