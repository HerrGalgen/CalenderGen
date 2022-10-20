from datetime import datetime, timedelta

import pytz


class Lesson:
    def __init__(self, room, subject, teacher, hour, dur):
        self.room = room
        self.subject = subject
        self.teacher = teacher
        self.hour = hour
        self.dur = dur
        self.end = hour
        self.start = 0
        self.end = 0
        self.start_h_normal = [7, 8, 9, 10, 11, 12, 12, 13, 14, 15, 15]
        self.start_m_normal = [55, 40, 25, 10, 15, 00, 45, 30, 15, 00, 45]

    def get_room(self):
        return self.room

    def get_subject(self):
        return self.subject

    def get_teacher(self):
        return self.teacher

    def get_hour(self):
        return self.hour

    def get_duration(self):
        return self.dur

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    @staticmethod
    def calc_times(lessons):
        now = datetime.now(pytz.timezone('Europe/Berlin'))

        for i in range(len(lessons)):
            lessons[i].start = datetime(now.year, now.month, now.day, lessons[i].start_h_normal[lessons[i].hour - 1],
                                        lessons[i].start_m_normal[lessons[i].hour - 1], 0,
                                        tzinfo=pytz.timezone('Europe/Berlin'))

            lessons[i].end = lessons[i].start + timedelta(hours=0, minutes=(45*lessons[i].dur), seconds=0)

        return lessons
