"""This module will handle all color related operations including 
conversion separation and merging"""

def color_add_trans_lvl(color, trans_lvl) -> tuple:
    """ the method will add transparency level to color tuple """
    color_with_trans = color[0] + (trans_lvl,)

    return color_with_trans
