from tkinter import ttk, filedialog, Label, RIGHT, BOTH, BOTTOM
import ctypes
from tkinter.ttk import Scrollbar

import pandas as pd

class ShowExcel:

    def __init__(self, win, frame):
        self.tree = ttk.Treeview(frame)

        self.treeScroll = Scrollbar(frame)
        self.treeScroll.configure(command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.treeScroll.set)
        self.treeScroll.pack(side=RIGHT, fill=BOTH)
    # Define a function for opening the file
    def open_file(self):
        filename = filedialog.askopenfilename(title="Open a File",
                                              filetype=(("xlxs files", ".*xlsx"), ("All Files", "*.")))

        if filename:
            try:
                filename = r"{}".format(filename)
                df = pd.read_excel(filename)
            except Exception:
                ctypes.windll.user32.MessageBox(0, "Fehler beim öffnen der Datei!", "FEHLER", 0)

        # Clear all the previous data in tree
        self.clear_treeview()

        # Add new data in Treeview widget
        self.tree["column"] = list(df.columns)
        self.tree["show"] = "headings"

        # For Headings iterate over the columns
        for col in self.tree["column"]:
            self.tree.heading(col, text=col)

        # Put Data in Rows
        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            self.tree.insert("", "end", values=row)

        self.tree.pack()

    # Clear the Treeview Widget
    def clear_treeview(self):
        self.tree.delete(*self.tree.get_children())