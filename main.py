from Calender import Calender
from ExcelReader import ExcelReader
from Lesson import Lesson

cal = Calender()
reader = ExcelReader()

#Read excel:

reader.read_file()

days = reader.get_days()

for key in days:
    cal.add_day(Lesson.calc_times(days.get(key), key))

cal.gen_cal()
