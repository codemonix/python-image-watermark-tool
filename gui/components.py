
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading
from file_handling.log_debug import print_cmd



class ProgressBar:
    def __init__(self, master, task_function, settings_container=None, maximum=100, title_text=None) -> None:
        self.masetr = master
        self.maximum = maximum
        self.settings_container = settings_container
        # self.master.title(text)
        self.task = task_function
        self.title_text = title_text

       
        self.canceled = False

    def start_progress(self):

        self.progress_window = tk.Toplevel(self.masetr)
        self.progress_window.title(self.title_text)

        self.progress_var = tk.DoubleVar()
        self.progress_var.set(0)


        self.progressbar = ttk.Progressbar(self.progress_window, orient='horizontal', 
                                           length=300, mode='determinate',maximum=self.maximum,  variable=self.progress_var)
        self.progressbar.pack(padx=5, pady=10)
        self.cancel_button = tk.Button(self.progress_window, text="Cancel", command=self.cancel)
        self.cancel_button.pack(pady=5)

        self.generator = self.task(self.update_progress, self.is_cancelled)

        self.cancelled = False
        self.progress_var.set(0)
        self.thread = threading.Thread(target=self.run_task)
        self.thread.start()

    def run_task(self):
        try:
            for _ in self.generator:
                if self.canceled:
                    break
        except Exception as e:
            print_cmd(f"Error in task {e}")
        finally:
            self.progress_window.destroy()

    def update_progress(self, value):
        self.progress_var.set(value)

    def cancel(self):
        self.canceled= True

    def is_cancelled(self):
        return self.canceled



class DragDropWidget:
    def __init__(self, parent, drag_image : Image, bg_image : Image) -> tk.Canvas:
        self.parent = parent
        self.bg_image = bg_image
        # canvas backround image
        # self.bg_image = Image.open(backgroung_image)
        self.background_image = ImageTk.PhotoImage(bg_image)

        # Image which is going to be dragged over background image
        self.image = ImageTk.PhotoImage(drag_image)
        # Keep track of pointer
        self.drag_data = {"item": None, "x": 0, "y": 0}
        self.position = None
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

    def on_token_release(self, event):
        coords = self.canvas.coords("token")
        print_cmd(coords)
        print_cmd(self.drag_data)
        self.drag_data["item"] = None
        self.position = coords
        print_cmd(self.position)
        return coords


    def on_token_motion(self, event):
        if self.drag_data["item"]:
            delta_x = event.x - self.drag_data["x"]
            delta_y = event.y - self.drag_data["y"]
            self.canvas.move(self.drag_data["item"], delta_x, delta_y)
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y