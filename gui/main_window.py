import tkinter as tk
from tkinter import messagebox
from gui.settings_window import TopSetting
from PIL import Image, ImageTk
from gui.ui_updater import update_main_window
from gui.components import ProgressBar
from file_handling.file_handling import save_settings, load_settings, list_files_dir, image_save
from core.image_processor import txt_image_watermark
from file_handling.log_debug import print_cmd


class MainWindow(tk.Frame):
    def __init__(self, master, settings_container):
        super().__init__(master)
        self.master = master
        self.settings_container = settings_container
        self.create_widget()

    def create_widget(self):
        self.text_frame = tk.Frame(self.master)
        self.text_frame.place(relx=0.01, rely=0.01, width=300, height=25)
        self.placeholder_text = "Enter your text here"
        self.w_text = tk.Entry(self.text_frame, fg="gray")
        self.w_text.insert(0, self.placeholder_text)
        self.w_text.bind('<FocusIn>', self.on_w_text_clicked)
        self.w_text.bind('<FocusOut>', self.on_w_text_leave)
        self.w_text.pack(fill="x", expand=True, side="left")
        self.butt_frame = tk.Frame(self.master, bd=2)
        self.butt_frame.place(x=310, rely=0.01, width=200, height=25)
        self.all_button = tk.Button(
            self.butt_frame, text="All", command=lambda: self.start_watermark(action='all'))
        self.all_button.pack(fill="both", expand=True, side="left")
        self.one_button = tk.Button(
            self.butt_frame, text="1", command=lambda: self.start_watermark(action=1))
        self.one_button.pack(fill="both", expand=True, side="left")
        self.path_frame = tk.Frame(self.master, bd=2)
        self.path_frame.place(relx=0.01, y=30, width=500, height=25)
        self.path_text = tk.Label(self.path_frame, bg="gray", text=self.settings_container.in_path_file.rsplit("/", 1)[1])
        print_cmd( {self.settings_container.in_path_file.rsplit('/',1)[1]})
        self.path_text.pack(fill="both", expand=True, side="left")
        self.pic_frame = tk.Frame(self.master)
        self.pic_frame.place(relx=0.01, y=60, width=500, height=500)
        self.pic_label = tk.Label(self.pic_frame)
        self.pic_label.pack(fill="both")
        self.menubar = tk.Menu(self.master)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Settings", command=self.open_settings)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Save Settings", command=self.save_setting_cmd)
        self.filemenu.add_command(label="Load Settings", command=self.load_setting_cmd)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.master.destroy)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.master.config(menu=self.menubar)

        update_main_window(self, self.settings_container)

    def on_w_text_clicked(self, event):
        if self.w_text.get() == self.placeholder_text:
            self.w_text.delete(0, tk.END)
            self.w_text.config(fg='black')
            self.settings_container.text_to_write = ""
            print_cmd("Entry text black")

    def on_w_text_leave(self, event):
        if not self.w_text.get():
            self.w_text.insert(0, self.placeholder_text)
            self.w_text.config(fg='gray')
            self.settings_container.text_to_write = ""
            print_cmd("Entry text gray")
        else:
            self.settings_container.text_to_write = self.w_text.get()



    def open_settings(self):
        if not hasattr(self, 'settings_menu'):
            self.settings_menu = TopSetting(self, self.master, 
                                            settings_container=self.settings_container)
            self.settings_menu.protocol('WM_DELETE_WINDOW', 
                                        self.close_settings_menu)
            self.settings_menu.grab_set()
            self.settings_menu.bind("<Escape>", self.close_settings_menu)
            # self.wait_window(self.settings_menu)
        elif hasattr(self, 'settings_menu'):
            self.settings_menu.lift()

    def close_settings_menu(self,event=None):
        if hasattr(self, 'settings_menu'):
            self.settings_menu.grab_release()
            self.lift()
            self.settings_menu.destroy()
            del self.settings_menu

    def start_watermark(self, action, process_callback=None, cancel_callack=None):
        if self.w_text.get() != self.placeholder_text:
            self.settings_container.text_to_write = self.w_text.get()
        if action == 1:
            final_image = txt_image_watermark(self.settings_container.in_path_file, self.settings_container)
            file_name = self.settings_container.in_path_file.rsplit("/", 1)[1]
            file_dir = self.settings_container.out_path + "/"
            file_path = file_dir + file_name
            image_save(final_image, file_path)
            

        if action == 'all':
            self.file_list = list_files_dir(self.settings_container.in_path_dir, self.settings_container.allowed_ext)
            if self.file_list:
                max_valuue = len(self.file_list)
                progress_bar = ProgressBar(self.master, self.watermark_all, settings_container=self.settings_container , maximum=max_valuue, title_text="processing Images ..." )
                progress_bar.start_progress()
            elif self.settings_container.in_path_dir == "":
                messagebox.showinfo("Check Input setting", "Please select input directory!")
            else:
                messagebox.showerror("Error", "Path not found")

    def watermark_all(self, progress_callback, cancel_callback):

        if self.file_list:
            processed_item = 0
            print_cmd( {len(self.file_list)})
            for file in self.file_list:
                final_image = txt_image_watermark(file, self.settings_container)
                file_name = file.rsplit("/", 1)[1]
                file_dir = self.settings_container.out_path + "/"
                file_path = file_dir + file_name
                image_save(final_image, file_path)
                if cancel_callback():
                    return
                processed_item += 1
                progress_callback(processed_item)
                yield

        else:
            messagebox.showerror("File Not Found", "Directory Not Found, Please check settings and try again!")
            print_cmd( "file not found!")

    def save_setting_cmd(self):
        state = save_settings(self.settings_container)
        if state:
            messagebox.showinfo("Save Settings", "Saved Successfully")
        elif state is None:
            messagebox.showwarning("Save Operation", "File is not saved Please try again")
        elif state is False:
            messagebox.showerror("Save file failed", "The disk is not ready")
        else:
            messagebox.showerror("Failed", "Something goes wrong!, please contact technical support")
        update_main_window(self, self.settings_container)

    def load_setting_cmd(self):
        load_settings(self.settings_container)
        update_main_window(self, self.settings_container)
        messagebox.showinfo("Load Setting", "Setting file loaded and set")


 