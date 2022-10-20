from icalendar import Calendar, Event, vText
import os
from pathlib import Path


class Calender:

    def __init__(self):
        self.cal = Calendar()

    def add_day(self, lessons):
        for lesson in lessons:
            event = Event()

            event.add('summary', str(int(lesson.get_hour())) + ": " + str(lesson.get_subject()) + "_" + str(lesson.get_teacher()))
            event.add('dtstart', lesson.get_start())
            event.add('dtend', lesson.get_end())

            event['location'] = vText(lesson.room)

            self.cal.add_component(event)

    def gen_cal(self):

        directory = str(Path(__file__).parent.parent) + "/"
        print("ics file will be generated at ", directory)
        f = open(os.path.join(directory, 'example.ics'), 'wb')
        f.write(self.cal.to_ical())
        f.close()
