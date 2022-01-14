import tkinter as tk
from ScrolledFrame import ScrolledFrame


class Table(tk.Frame):
    def __init__(self, *args, rows=1, columns=1, show_headers=False, headers: list = [], widths=[], **kwargs):
        super().__init__(self, *args, **kwargs)

        self.widths = [10] * columns
        if widths:
            if type(widths) is int:
                self.widths = [widths] * columns
            elif type(widths) is list:
                for i in range(len(widths)):
                    self.widths[i] = widths[i]
            else:
                raise Exception(
                    f"Invalid type for widths '{type(widths)}' expted int or list")

        if show_headers is True:
            if not headers:
                raise Exception(
                    f"No headers provided, even though show_headers is set to True")
            if len(headers) != columns:
                raise Exception(
                    f"Number of headers ({len(headers)}) must be equal to nmber of columns ({columns})")
            if len(headers) != len(set(headers)):
                raise Exception(f"Header list contains duplicates")

        self.table = []
        self.headers = headers
        self.show_headers = show_headers
        self.rows = rows
        self.columns = columns

        for i in range(rows):
            self.table.append([])
            for j in range(columns):
                self.table[i].append(tk.Entry(self, width=self.widths[j]))

    def grid_headers(self):
        for i in range(len(self.headers)):
            tk.Label(self, text=self.headers[i]).grid(row=0, column=i)

    def grid_cells(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.table[i][j].grid(
                    row=i + (1 if self.headers else 0), column=j)

    def grid(self, *args, **kwargs):
        if self.show_headers:
            self.grid_headers()
        self.grid_cells()
        tk.Frame.grid(self, *args, **kwargs)

    def pack(self, *args, **kwargs):
        if self.show_headers:
            self.grid_headers()
        self.grid_cells()
        tk.Frame.pack(self, *args, **kwargs)

    def get_header_index(self, header):
        return self.headers.index(header)

    def get_row(self, row: int):
        return [cell.get() for cell in self.table[row]]

    def get_column(self, column):
        if type(column) is str:
            column = self.get_header_index(column)
        elif type(column) is not int:
            raise Exception(f"Invalid type for column '{type(column)}'")
        return [row[column].get() for row in self.table]

    def get_cell(self, column: int = 0, row: int = 0):
        return self.table[column][row].get()

    def set_cell(self, row: int, column: int, value: str):
        self.table[row][column].delete(0, END)
        self.table[row][column].insert(0, str(value))

    def set_column(self, column, value):
        if type(column) is str:
            column = self.get_header_index(column)
        elif type(column) is not int:
            raise Exception(f"Invalid type for column '{type(column)}'")
        if type(value) is list:
            if len(value) != self.rows:
                raise Exception(
                    f"Invalid number of items to set column {len(value)}/{self.rows}")
            for j, item in enumerate(value):
                self.set_cell(j, column, item)
        else:
            for i in range(self.rows):
                self.set_cell(i, column, value)

    def set_row(self, row_index, row_values):
        for i in range(min(len(row_values), self.columns)):
            self.set_cell(row_index, i, row_values[i])

    def add_row(self):
        self.table.append([])
        self.rows += 1
        for i in range(self.columns):
            self.table[-1].append(tk.Entry(self, width=self.widths[i]))
            self.table[-1][-1].grid(row=self.rows +
                                    (1 if self.headers else 0), column=i)

    def set_row_count(self, row_count):
        if (row_count < self.rows):
            for i in range(self.rows - row_count):
                for entry in self.table[-1]:
                    entry.destroy()
                self.table.pop()
        else:
            for _ in range(row_count - self.rows):
                self.add_row()
        self.rows = row_count
