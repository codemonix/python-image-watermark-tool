
from PIL import Image, ImageFont, ImageDraw, ImageOps, ImageTk
from file_handling.log_debug import print_cmd



class ImageComposer:
    def __init__(self) -> None:
        pass

def txt_image_watermark(file, settings_container) -> Image:
    image = Image.open(file).convert('RGBA')
    image = ImageOps.exif_transpose(image)
    print_cmd(f"{settings_container.font_size}")

    font = ImageFont.truetype(font=settings_container.choosen_font, size=settings_container.font_size)

    base_img = Image.new("RGBA", image.size, (255, 255, 255, 0))

    draw = ImageDraw.Draw(base_img)

    bbox = draw.textbbox(settings_container.txt_poz, 
                            settings_container.text_to_write, font=font)
    print_cmd(f"{settings_container.txt_bg_color[0] + (settings_container.txt_trans_lvl,)}")
    fill_bg = settings_container.txt_bg_color[0] + (settings_container.txt_trans_lvl,)
    print_cmd(fill_bg)
    draw.rectangle(bbox, fill=fill_bg)
    fill_fg = settings_container.txt_color[0] + (settings_container.txt_trans_lvl,)
    draw.text(settings_container.txt_poz, settings_container.text_to_write,font=font, fill=fill_fg)

    final_image = Image.alpha_composite(image, base_img)

    # image_save(image, settings_container)
    return final_image

        



def get_scaled_image(image, max_with):
    image = ImageOps.exif_transpose(image)
    scl = 1
    w , h = image.size
    while w > max_with or h > max_with:
        scl += 1
        w = image.size[0] // scl
        h = image.size[1] // scl
        print_cmd(f"{w} , {h}")

    print_cmd(f" {scl} ")
    return image.resize((image.size[0] // scl, image.size[1] //scl))
