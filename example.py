from DateEntry import *
from Form import Form
import tkinter as tk


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.form = Form(self)
        self.form.set_items({
            "Date of birth": DateEntry(self.form)
        })
        self.form.pack()
        tk.Button(self, text="Get Form", command=lambda: print(
            self.form.getAll())).pack()


App().mainloop()
