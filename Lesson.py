from datetime import datetime, timedelta

import pytz


class Lesson:
    def __init__(self, room, subject, teacher, hour):
        self.room = room
        self.subject = subject
        self.teacher = teacher
        self.hour = hour
        self.end = hour
        self.start = 0
        self.end = 0
        self.start_h_normal = [7, 8, 9, 10, 11, 12, 13, 14, 15, 15]
        self.start_m_normal = [55, 40, 25, 10, 15, 00, 30, 15, 00, 45]

    def get_room(self):
        return self.room

    def get_subject(self):
        return self.subject

    def get_teacher(self):
        return self.teacher

    def get_hour(self):
        return self.hour

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    @staticmethod
    def calc_times(lessons, date):
        now = datetime.now(pytz.timezone('Europe/Berlin'))

        cleaned_lessons = [x for x in lessons if x.subject == x.subject]

        lesson_count = len(cleaned_lessons)

        for i in range(len(cleaned_lessons)):
            print(len(cleaned_lessons))

            if Lesson.isNan(cleaned_lessons[i].subject):
                cleaned_lessons.remove(cleaned_lessons[i])
                continue

            cleaned_lessons[i].start = datetime(date.year, date.month, date.day,
                                                cleaned_lessons[i].start_h_normal[int(cleaned_lessons[i].hour) - 1],
                                                cleaned_lessons[i].start_m_normal[int(cleaned_lessons[i].hour) - 1], 0,
                                                tzinfo=pytz.timezone('Europe/Berlin'))

            if lesson_count > 4 and i == 2 and cleaned_lessons[2].subject == cleaned_lessons[3].subject and \
                    cleaned_lessons[2].teacher == cleaned_lessons[3].teacher:
                cleaned_lessons[2].start += timedelta(hours=0, minutes=20, seconds=0)

            elif lesson_count > 3 and i == 3:
                cleaned_lessons[3].start += timedelta(hours=0, minutes=20, seconds=0)

            cleaned_lessons[i].end = cleaned_lessons[i].start + timedelta(hours=0, minutes=45, seconds=0)

        return cleaned_lessons

    @staticmethod
    def isNan(num):
        return num != num
