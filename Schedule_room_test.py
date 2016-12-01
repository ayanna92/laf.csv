# trying to make a schedule for at least one room
# Lectures & roosters
#
# Ayanna, Lois, Femke
#
import csv
from class_rooms import *
from class_courses import *
from main import *

zaalrooster = {}
def main ():

    import csv
    import math
    import random

    class_rooms_list = csv.reader(open('classrooms.csv'))
    course_and_activity = hoofd_main()
    random.shuffle(course_and_activity)

    #making a list for each activity
    for row in class_rooms_list:
        name = row[0]
        capacity = row[1]
        room = Classrooms(name, capacity)

        #print name
        week = room.createEmptyWeek()

        #voor twintig tijdsbokken per zaal
        for weeks in range(20):

            # print empty string when list is empty
            if len(course_and_activity) == 0:
                course = ''
            else:
                course = course_and_activity[0]
                course_and_activity.pop(0)

            rooster = room.fillInWeek(course, week)
            zaalrooster[room.room] = rooster


        #print rooster

        print rooster
    #print zaalrooster
    return zaalrooster
main()
