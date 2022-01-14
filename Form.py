import tkinter as tk


class Form(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        items = kwargs.get("items", {})
        self.set_items(items)

    def set_items(self, items):
        self.items = items
        for i, (key, value) in enumerate(self.items.items()):
            tk.Label(self, text=key).grid(row=i, column=0)
            if (type(value) == tuple):
                value[0].grid(row=i, column=1)
            else:
                value.grid(row=i, column=1)

    def get(self, key):
        value = self.items.get(key)
        if value:
            if (type(value) == tuple):
                return value[1]()
            return value.get()
        return value

    def getAll(self):
        result = {}
        for key, value in self.items.items():
            if type(value) == tuple:
                result[key] = value[1]()
            else:
                result[key] = value.get()
        return result

# class App(Tk):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.form = Form(self)
#         option_var = StringVar()
#         self.form.set_items({
#             "Fist Name": Entry(self.form),
#             "Last Name": Entry(self.form),
#             "Date of brith": Entry(self.form),
#             "Gender": (OptionMenu(self.form, option_var, "b", "c", "d", "e"), option_var.get)
#         })
#         self.form.grid()
#         Button(self, text="Submit", command=lambda: print(self.form.getAll())).grid()
