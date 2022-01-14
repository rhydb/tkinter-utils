# tkinter-utils

Simple classes to help with tkinter.

- Table with scrollbar
- Excel-style table (hacky scrollbar)
- Tab manager
- Form widget
- DateEntry widget
- SQL Database (sqlite3)

## Examples

### Tabs

```py
tabman = TabManager(root)
tabman.tabs = {
  # internal name      text     constructor
  "first": Tab(tabman, "First Tab", first_tab)
}
tabman.construct()

def login_tab():
  def change_tab():
      # remove current tabs
      tabman.clear()
      tabman.tabs = {
          "second": Tab(tabman, "Second Tab"", main_tab)
      }
      tabman.construct()
  # can use [] (or tabman.tabs[]) with internal name
  tk.Button(tabman["first"], text="Load second tab", command=change_tab).pack()

def second_tab():
  tk.Label(tabman.tabs["second"], text="Another tab").pack()
```

### Insert into table using a form

```py
# Create a form with input
form = Form(root)
# for the option menu
option_var = tk.StringVar()
form_items = {
    # Label      Widget
    "Fist Name": tk.Entry(form),
    "Last Name": tk.Entry(form),
    "Date of brith": DateEntry(form),
    # OptionMenu must be a tuple of (OptionMenu, StringVar.get)
    "Gender": (tk.OptionMenu(form, option_var, "Male", "Female"), option_var.get)
}
form.set_items(form_items)
form.pack(fill="both")

table = Table(root, cols=tuple(form_items.keys()))
table.push("John", "Doe", "01/02/03", "F")
table.push("Jane", "Doe", "04/05/06", "M")
table.push("Foo", "Bar", "04/05/06", "Baz")
table.pack(fill="both")
```
