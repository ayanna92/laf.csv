# trying to make a schedule for at least one room
# Lectures & roosters
#
# Ayanna, Lois, Femke
#

from class_rooms import *
from class_courses import *

def main ():

    import csv
    import math

    course_student_list = csv.reader(open('course_stud_num.csv'))
    class_rooms_list = csv.reader(open('classrooms.csv'))
    courses_list = csv.reader(open('vakken2.csv'))


    for row in courses_list:
        courses.append(row)

    for row in courses:
        name_course.append(row[0])

    for row in class_rooms_list:

        name = row[0]
        capacity = row[1]
        room = Classrooms(name, capacity)
        print name

        week = room.createEmptyWeek()

        for row in courses_list:
            for weeks in range(0, 19, 1):

        print room.createEmptyWeek()

main()
