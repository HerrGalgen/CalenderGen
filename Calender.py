import icalendar
from icalendar import Calendar, Event, vCalAddress, vText
import pytz
import os
from pathlib import Path

# Adding events to calendar




class Calender:

    def __init__(self):
        self.cal = Calendar()

    def add_event(self, lesson):

        event = Event()

        event.add('summary', lesson.subject + "_" + lesson.teacher)
        event.add('dtstart', lesson.start)
        event.add('dtend', lesson.end)

        event['location'] = vText(lesson.room)

        self.cal.add_component(event)

    def gen_cal(self):

        directory = str(Path(__file__).parent.parent) + "/"
        print("ics file will be generated at ", directory)
        f = open(os.path.join(directory, 'example.ics'), 'wb')
        f.write(self.cal.to_ical())
        f.close()


