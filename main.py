from Calender import Calender
from ExcelReader import ExcelReader
from Lesson import Lesson

cal = Calender()
reader = ExcelReader()

#Read excel:

reader.read_file()
#
# monday = [Lesson("E114", "PuG", "WaMa", 1,),
#           Lesson("E114", "ITaG", "MaMa", 2),
#           Lesson("O014", "ITP", "ReEv", 3),
#           Lesson("O014", "ITP", "ReEv", 4),
#           Lesson("O014", "ITP", "ReEv", 5),
#           Lesson("O014", "ITP", "ReEv", 6),
#           Lesson("O014", "ITP", "ReEv", 7),
#           Lesson("O014", "ITP", "ReEv", 8),
#           Lesson("O014", "ITP", "ReEv", 9)
#           ]
#
# monday = Lesson.calc_times(monday)
# cal.add_day(monday)
#

days = reader.get_days()

for key in days:
    cal.add_day(Lesson.calc_times(days.get(key), key))

cal.gen_cal()
