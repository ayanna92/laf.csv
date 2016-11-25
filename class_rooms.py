# class for classrooms
# Lectures & roosters
#
# Ayanna, Lois, Femke
#

from class_courses import *
import numpy as np

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

    # zaal.roomCapacity() gives capacity of room
    def roomCapacity(self):

        return self.capacity

    def createEmptyWeek(self):

        # week2 = np.empty(shape=[0, self.days])
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

        return week

# testing for the class
A104 = Classrooms("A1.04", 41)

#maak een lege week voor object (zaal) A1.04
A104.week = A104.createEmptyWeek()

# for loop maken waar die de vakken in het rooster vult en opslaat in week
A104.week1 = A104.fillInWeek("heuristieken", A104.week)
A104.week2 = A104.fillInWeek("Programmeren 1", A104.week1)
A104.week3 = A104.fillInWeek("Programmeren 2", A104.week2)

# test of die goed checkt wann zaal leeg is 1 staat voor dag(dinsdag) 2 voor tijdslot 11-13
print A104.emptyTimeSlot(1, 2, A104.week)
print A104.week
