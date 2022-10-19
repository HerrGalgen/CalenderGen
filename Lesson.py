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

        self.calcTime()

    def getRoom(self):
        return self.room

    def getSubject(self):
        return self.subject

    def getTeacher(self):
        return self.teacher

    def getHour(self):
        return self.hour

    def getDuration(self):
        return self.dur

    def calcTime(self):

        now = datetime.now(pytz.timezone('Europe/Berlin'))

        if self.hour == '1':
            self.start = datetime(now.year, now.month, now.day, 7, 55, 0, tzinfo=pytz.timezone('Europe/Berlin'))
            self.end = self.start + timedelta(hours=0, minutes=45, seconds=0)
        else:
            self.start = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second, tzinfo=pytz.timezone('Europe/Berlin'))
            self.end = self.start
