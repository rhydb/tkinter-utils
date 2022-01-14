import tkinter as tk
import tkinter.ttk as ttk


class Table(tk.Frame):
    def __init__(self, *args, cols=(str), **kwargs):
        super().__init__(*args, **kwargs)

        self.table = ttk.Treeview(self, columns=cols, show="headings")

        # map columns to index
        self.index = {}
        for i, j in enumerate(cols):
            self.index[j] = i

        for col in cols:
            self.table.heading(col, text=col)
            self.table.column(col, anchor="center", stretch=True)

        self.table.pack(side=tk.LEFT, fill="both", expand=True)

        # create scrollbar
        self.table_scroll = ttk.Scrollbar(
            self, orient='vertical', command=self.table.yview)
        self.table_scroll.pack(side="right", fill='y')
        # dynamic height change
        self.table['yscrollcommand'] = self.table_scroll.set

    def push(self, *args):
        # push an item to the bottom of the table
        self.table.insert('', tk.END, values=args)

    def push_dict(self, row):
        arr = [str] * len(row)
        for k, v in row.items():
            arr[self.index[k]] = v
        self.push(*arr)

    def fetch_selected(self):
        # fetch the selected rows and their values
        [self.table.item(item, option="values")
         for item in self.table.selection()]

    def delete_selected(self):
        self.table.delete(*(self.table.selection()))

    def remove_selected(self):
        self.delete_selected()
