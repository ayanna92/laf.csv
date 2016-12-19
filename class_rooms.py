# class for classrooms
# Lectures & roosters
#
# Ayanna, Lois, Femke
#

from class_courses import *

class Classrooms(object):
    """
    Object that will contain the classrooms and their capacity
    """

    def __init__(self, room, capacity):
        """
        Initialize classroom number and capacity of the classroom
        """

        self.room = room
        self.capacity = capacity
        self.week = [[]]
        self.days = [1, 2, 3, 4, 5]
        self.hours = [1, 2, 3, 4]

    def roomCapacity(self):

        return self.capacity

    def createEmptyWeek(self):

        week = [[0 for i in range(4)] for j in range(5)]
        return week

    def emptyTimeSlot(self, day, hour, week):
        self.day = day
        self.hour = hour
        self.week = week

        if week[self.day][self.hour] == 0:
            return True
        else:
            return False

    def fillInWeek(self, course, week):
        self.course = course
        self.week = week

        import random

        random_day = random.randint(0,4)
        random_hour = random.randint(0,3)

        if self.emptyTimeSlot(random_day, random_hour, week) == True:
            week[random_day][random_hour] = (self.course)

        else:
            self.fillInWeek(course, week)

        return week
