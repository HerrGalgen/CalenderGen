from datetime import datetime

import pandas as pd

from Lesson import Lesson


class ExcelReader:

    def __init__(self):
        self.days = {}

    def get_days(self):
        return self.days

    def read_file(self):

        data = pd.read_excel(r'C:\Users\kreuz\Desktop\Stundenplan.xlsx')
        mon_date = data.keys()[1]
        tue_date = data.keys()[5]
        wed_date = data.keys()[9]
        thu_date = data.keys()[13]
        fri_date = data.keys()[17]

        data = pd.read_excel(r'C:\Users\kreuz\Desktop\Stundenplan.xlsx', skiprows=1)
        df = pd.DataFrame(data)

        monday = df.iloc[:, 0:4]
        tuesday = df.iloc[:, 4:8]
        wednesday = df.iloc[:, 8:12]
        thursday = df.iloc[:, 12:16]
        friday = df.iloc[:, 16:20]

        day_lessons = []

        for lesson in monday.iterrows():
            room = lesson[1][0]
            teacher = lesson[1][2]
            subject = lesson[1][1]
            hour = lesson[1][3]
            day_lessons.append(Lesson(room, subject, teacher, hour))

        self.days[mon_date] = day_lessons
        day_lessons = []

        for lesson in tuesday.iterrows():
            room = lesson[1][0]
            teacher = lesson[1][2]
            subject = lesson[1][1]
            hour = lesson[1][3]
            day_lessons.append(Lesson(room, subject, teacher, hour))

        self.days[tue_date] = day_lessons
        day_lessons = []

        for lesson in wednesday.iterrows():
            room = lesson[1][0]
            teacher = lesson[1][2]
            subject = lesson[1][1]
            hour = lesson[1][3]
            day_lessons.append(Lesson(room, subject, teacher, hour))

        self.days[wed_date] = day_lessons
        day_lessons = []

        for lesson in thursday.iterrows():
            room = lesson[1][0]
            teacher = lesson[1][2]
            subject = lesson[1][1]
            hour = lesson[1][3]
            day_lessons.append(Lesson(room, subject, teacher, hour))

        self.days[thu_date] = day_lessons
        day_lessons = []

        for lesson in friday.iterrows():
            room = lesson[1][0]
            teacher = lesson[1][2]
            subject = lesson[1][1]
            hour = lesson[1][3]
            day_lessons.append(Lesson(room, subject, teacher, hour))

        self.days[fri_date] = day_lessons
        day_lessons = []

    def get_lessons(self):
        return self.days
