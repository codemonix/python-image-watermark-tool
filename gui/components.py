import tkinter as tk
from tkinter import ttk
import threading
from utils.log_debug import print_cmd


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

        self.generator = self.task(self.settings_container, self.update_progress, self.is_cancelled)

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
