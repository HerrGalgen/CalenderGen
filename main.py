from Calender import Calender
from Lesson import Lesson

mo_first = Lesson("E114", "PuG", "WaMa", "1", "1")

cal = Calender()

cal.add_event(mo_first)
cal.gen_cal()
