import tkinter as tk

class DragDropComponent(tk.Label):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<ButtonPress-1>", self.on_drag_start)
        self.bind("<B1-Motion>", self.on_drag_motion)
        self.bind("<ButtonRelease-1>", self.on_drag_release)
        
    def on_drag_start(self, event):
        self.start_x = event.x
        self.start_y = event.y
        
    def on_drag_motion(self, event):
        x = self.winfo_x() - self.start_x + event.x
        y = self.winfo_y() - self.start_y + event.y
        self.place(x=x, y=y)
        
    def on_drag_release(self, event):
        pass  # You can add further behavior upon releasing the mouse button

# Example usage
root = tk.Tk()

# Create a draggable label
drag_label = DragDropComponent(root, text="Drag me!", bg="lightblue")
drag_label.pack()

root.mainloop()
