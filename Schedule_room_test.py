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

    course_student_list = csv.reader(open('course_stud_num.csv'))
    class_rooms_list = csv.reader(open('classrooms.csv'))
    courses_list = csv.reader(open('vakken2.csv'))


    courses = []
    name_course = []
    course_and_student = []

    lists2 = hoofd_main()
    course_and_activity = lists2[0]
    class_rooms_list = lists2[1]
    random.shuffle(course_and_activity)
    print "random shuffle"
    print course_and_activity

    for row in course_student_list:
        course_and_student.append(row)


    for row in courses_list:
        courses.append(row)

    for row in courses:
        name_course.append(row[0])


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


        print rooster
    #print zaalrooster
    return zaalrooster
main()
