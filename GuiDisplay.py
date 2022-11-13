from tkinter import *
from tkinter import ttk, filedialog

from ExcelMain import ExcelMain
from ShowExcel import ShowExcel
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Create an object of Style widget
style = ttk.Style()
style.theme_use('clam')

# Create a Frame
frame = Frame(win)
frame.pack(pady=20)

excelDisplay = ShowExcel(win, frame)
excelmain = ExcelMain()

# Add a Menu
m = Menu(win)
win.config(menu=m)

# Add Menu Dropdown
file_menu = Menu(m, tearoff=False)

m.add_cascade(label="Datei", menu=file_menu)
file_menu.add_command(label="Excel öffnen", command=excelDisplay.open_file)
file_menu.add_command(label="Exel to ics", command=excelmain.create_ics)

# Add a Label widget to display the file content

win.mainloop()