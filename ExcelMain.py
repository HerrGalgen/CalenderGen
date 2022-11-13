from tkinter import filedialog

from Calender import Calender
from ExcelReader import ExcelReader
from Lesson import Lesson

class ExcelMain:

    def __init__(self):
        self.cal = Calender()
        self.reader = ExcelReader()

#Read excel:

    def create_ics(self):

        filename = filedialog.askopenfilename(title="Open a File",
                                              filetype=(("xlxs files", ".*xlsx"), ("All Files", "*.")))
        self.reader.set_filepath(filename)
        self.reader.read_file()

        days = self.reader.get_days()

        for key in days:
            self.cal.add_day(Lesson.calc_times(days.get(key), key))

        self.cal.gen_cal()
