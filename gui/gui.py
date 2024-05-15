import tkinter as tk

class MainApp:
    def __init__(self, root, data_container):
        self.root = root
        # super().__init__()
        self.root.title("Water Marker")
        self.root.minsize(width=510, height=565)
        self.text_frame = tk.Frame(self.root)
        self.text_frame.place(relx=0.01, rely=0.01, width=300, height=25)
        self.w_text = tk.Entry(self.text_frame).pack(fill="x", expand=True, side="left")
        self.butt_frame = tk.Frame(self.root, bd=2)
        self.butt_frame.place(x=310, rely=0.01, width=200, height=25)
        self.all_button = MyButton(
            self.butt_frame, text="All", command=lambda: self.all_button.clicked(self.do_nothing))
        self.all_button.pack(fill="both", expand=True, side="left")
        self.one_button = MyButton(
            self.butt_frame, text="1", command=lambda: self.do_nothing())
        self.one_button.pack(fill="both", expand=True, side="left")
        self.path_frame = tk.Frame(self.root, bd=2)
        self.path_frame.place(relx=0.01, y=30, width=500, height=25)
        self.path_text = tk.Label(self.path_frame, textvariable=data_container.in_path_txt)
        self.path_text.pack(fill="both", expand=True, side="left")
        self.pic_frame = tk.Frame(self.root, bg="gray")
        self.pic_frame.place(relx=0.01, y=60, width=500, height=500)
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Settings", command=lambda: self.open_settings(data_container))
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Save Settings", command=lambda: self.do_nothing())
        self.filemenu.add_command(label="Load Settings", command=lambda: self.do_nothing())
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.root.destroy)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.root.config(menu=self.menubar)

    def do_nothing(self):
        print("I am doing nothing.")


class MyButton(tk.Button):
    def __init__(self, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self.data = None

    def clicked(self, func, *args, **kwargs):
        self.data = func(*args, **kwargs)
        return self.data
