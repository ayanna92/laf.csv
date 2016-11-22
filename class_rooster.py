# Main file classes
# Lectures & roosters
#
# Ayanna, Lois, Femke
#

import math
import random
import pylab
import studentenvakken.csv

# === Provide classes

class RoomSchedule(object):
    """
    Representeert een rooster voor de lokalen
    """
    def __init__(self, Classroom):

        self.classroom = Classroom.room
        self.capacity = room.capacity
        self.tijd_slot = []
        self.day = ("monday", "tuesday", "wednesday", "thursday", "Friday")
        self.hour = ("9.00", "11.00", "13.00", "15.00", "17.00")

    def classification(self):
        """
        return a list where each day and each hour is represented
        """
        schedulelist[]
        day_hour = []
            for time.slot in self.timeslot:
                day_hour.append(self.day)
                day_hour.append(self.hour)
                schedulelist.append(day_hour)

        return schedulelist

class StudentSchedule(object):
    """
    representeert een rooster voor de studenten.
    """
    def __init__(self, students):
        import random
        self.student_id = students.stud_num
        self.amountOfCourses = students.vakNumber()
        self.tijd_slot = []
        self.day = random.choice(["monday", "tuesday", "wednesday", "thursday", "Friday"])
        self.hour = random.choice(["9.00", "11.00", "13.00", "15.00", "17.00"])

    def classificationStudent(self):

        schedule_list = []
        for time_slot in self.tijd_slots:
            day_hour = []
            day_hour.append(tijd_slots.day)
            day_hour.append(tijd_slots.hour)
            schedule_list.append(day_hour)

        return schedule_list
