
from PIL import Image, ImageFont, ImageDraw, ImageOps, ImageTk
from file_handling.log_debug import print_cmd
from utils.color_utils import color_add_trans_lvl



class ImageComposer:
    def __init__(self) -> None:
        pass

def txt_image_watermark(file, settings_container) -> Image.Image:
    image = Image.open(file).convert('RGBA')
    image = ImageOps.exif_transpose(image)
    print_cmd(f"{settings_container.font_size}")

    font = ImageFont.truetype(font=settings_container.choosen_font, size=settings_container.font_size)

    base_img = Image.new("RGBA", image.size, (255, 255, 255, 0))

    draw = ImageDraw.Draw(base_img)

    bbox = draw.textbbox(settings_container.txt_poz, 
                            settings_container.text_to_write, font=font)
    print_cmd(color_add_trans_lvl(settings_container.txt_bg_color, settings_container.txt_trans_lvl))
    fill_bg = settings_container.txt_bg_color[0] + (settings_container.txt_trans_lvl,)
    print_cmd(fill_bg)
    draw.rectangle(bbox, fill=fill_bg)
    fill_fg = settings_container.txt_color[0] + (settings_container.txt_trans_lvl,)
    draw.text(settings_container.txt_poz, settings_container.text_to_write,font=font, fill=fill_fg)

    final_image = Image.alpha_composite(image, base_img)

    # image_save(image, settings_container)
    return final_image



class GetPic():
    def __init__(self, text, font, size, fg=None, bg=None) -> None:
        self.text = text
        self.font = font
        self.size = size
        self.text_color = fg
        self.text_bg_color = bg

    def create_image_from_txt(self) -> tuple[Image.Image, tuple[int,int]]:
        font = ImageFont.truetype(font=self.font, size=self.size)
        dummy_immage = Image.new('RGBA', (1,1))
        draw = ImageDraw.Draw(dummy_immage)
        
        #Get the text image size
        # text_size = draw.textsize(self.text, font=self.font )
        bbox = draw.textbbox((0,0), text=self.text, font=font)

        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] + bbox[1]

        print_cmd(f"{text_width}, {text_height}")

        #create an image with calculated text size
        image = Image.new('RGBA', (text_width, text_height), self.text_bg_color)
        draw = ImageDraw.Draw(image)

        #Draw the text on the image
        draw.text((0, 0), self.text, fill=self.text_color, font=font)

        return image, image.size
    



def get_scaled_image(image, max_with, sc=False):
    image = ImageOps.exif_transpose(image)
    scl = 1
    w , h = image.size
    while w > max_with or h > max_with:
        scl += 1
        w = image.size[0] // scl
        h = image.size[1] // scl
        print_cmd(f"{w} , {h}")

    print_cmd(f" {scl} ")
    image = image.resize((image.size[0] // scl, image.size[1] //scl))
    if sc :
        result = (image, scl)
    else:
        result = image


    return result
