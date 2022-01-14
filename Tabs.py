from tkinter import ttk as ttk
from typing import Callable


class Tab(ttk.Frame):
    def __init__(self, master, text: str, construct: Callable, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.text = text
        self.construct = construct


class TabManager(ttk.Notebook):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(expand=1, fill="both")
        self.tabs = kwargs.get("tabs", {})

    def construct(self):
        for _, tab in self.tabs.items():
            tab.construct()
            self.add(tab, text=tab.text)

    def build(self):
        self.construct()

    def clear(self):
        for i in range(len(self.tabs)):
            self.forget(0)

    def __getitem__(self, key: str) -> Tab:
        return self.tabs.get(key)
