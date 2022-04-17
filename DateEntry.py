import tkinter as tk


class DateEntry(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        delim = kwargs.get("delim", "/")
        show_names = kwargs.get("names", True)

        if show_names:
            tk.Label(self, text="Day").grid(row=0, column=0)
            tk.Label(self, text="Month").grid(row=0, column=2)
            tk.Label(self, text="Year").grid(row=0, column=4)

        # StringVar stores the actual data
        self.day = tk.StringVar()
        # entry box, kept to move onto next item
        day = tk.Entry(self, width=2, textvariable=self.day)
        day.grid(row=1, column=0)
        # limit character count
        self.limit_char_count(self.day, 2, day)

        tk.Label(self, text=delim).grid(row=1, column=1)

        self.month = tk.StringVar()
        month = tk.Entry(self, width=2, textvariable=self.month)
        month.grid(row=1, column=2)
        self.limit_char_count(self.month, 2, month)

        tk.Label(self, text=delim).grid(row=1, column=3)

        self.year = tk.StringVar()
        year = tk.Entry(self, width=4, textvariable=self.year)
        year.grid(row=1, column=4)
        self.limit_char_count(self.year, 4, year)

    def limit_char_count(self, variable, n, entry):
        def limit(*_):
            value = variable.get()
            if len(value) >= n:
                variable.set(value[:n])  # remove extra data
                entry.tk_focusNext().focus()  # move onto the next item automatically
        variable.trace('w', limit)  # add callback

    def get(self):
        return (self.day.get(), self.month.get(), self.year.get())
