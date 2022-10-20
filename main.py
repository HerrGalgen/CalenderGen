from Calender import Calender
from Lesson import Lesson

cal = Calender()

monday = [Lesson("E114", "PuG", "WaMa", 1, 1),
          Lesson("E114", "ITaG", "MaMa", 2, 1)
          ]

monday = Lesson.calc_times(monday)
cal.add_day(monday)
cal.gen_cal()
