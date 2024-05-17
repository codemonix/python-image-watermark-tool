
# from text_to_pic import GetPic
import tkinter as tk
from PIL import ImageTk, Image
from file_handling.file_handling import print_cmd


class DragDropWidget:
    def __init__(self, parent, drag_image, backgroung_image):
        self.parent = parent
        self.position = [0, 0]

        # canvas backround image
        self.bg_image = Image.open(backgroung_image)
        self.background_image = ImageTk.PhotoImage(self.bg_image)

        # Image which is going to be dragged over background image
        self.image = ImageTk.PhotoImage(drag_image)
        # Keep track of pointer
        self.drag_data = {"item": None, "x": 0, "y": 0}
        self.create_widget()

        
    def create_widget(self):

        # getting the size of backgroung image and create canvas accordingly
        c_width , c_height = self.bg_image.size
        self.canvas = tk.Canvas(self.parent, width=c_width, height=c_height, bg="blue")
        self.canvas.pack()
        # Adding background image to canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)
        # Adding to be dragged image to canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image, tags="token")
        # Binding actions to the image for drag and drop 
        self.canvas.tag_bind("token", "<ButtonPress-1>", self.on_token_press)
        self.canvas.tag_bind("token", "<ButtonRelease-1>", self.on_token_release)
        self.canvas.tag_bind("token", "<B1-Motion>", self.on_token_motion)


    def on_token_press(self, event):
        self.drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y
        # print_cmd("token pressed")

    def on_token_release(self, event):
        coords = self.canvas.coords("token")
        # print(coords)
        # print(self.drag_data)
        self.drag_data["item"] = None
        self.position = coords
        print_cmd(self.position)
        return coords
        # print_cmd("token released")

    def on_token_motion(self, event):
        if self.drag_data["item"]:
            delta_x = event.x - self.drag_data["x"]
            delta_y = event.y - self.drag_data["y"]
            self.canvas.move(self.drag_data["item"], delta_x, delta_y)
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y
            # print_cmd("tpken draged")

# Example usage
# if __name__ == "__main__":

#     root = tk.Tk()
#     root.title("Drag and Drop Example")
#     output = GetPic("AAAAA", "Arial.ttf", 100).create_image_from_txt()
#     image = output[0]


#     # Replace 'image_path' with the path to your image
#     widget = DragDropWidget(root, image, "test.png")
#     root.mainloop()
