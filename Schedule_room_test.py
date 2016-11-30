# trying to make a schedule for at least one room
# Lectures & roosters
#
# Ayanna, Lois, Femke
#
import csv
from class_rooms import *
from class_courses import *
zaalrooster = {}
def main ():

    import csv
    import math
    import random

    course_student_list = csv.reader(open('course_stud_num.csv'))
    class_rooms_list = csv.reader(open('classrooms.csv'))
    courses_list = csv.reader(open('vakken2.csv'))
    courses_activity_list = csv.reader(open('course_and_activity.csv'))

    courses = []
    name_course = []
    course_and_student = []
    course_and_activity = []

    for row in courses_activity_list:
        course_and_activity.append(row)
        #print course_and_activity

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

        #voor twintig tijdbokken per zaal
        for weeks in range(0, 20, 1):
            random_course = random.randint(0,28)
            course = name_course[random_course]


            # OM DEZE VROLIJKE VRIEND GAAT HET
            rooster = room.fillInWeek(course, week)
            zaalrooster[room.room] = rooster

            #dit is wanneer we echt per werkgroep en student gaan kijken
            for students in course_and_student:
                if students[0] == course:
                   student_list = students[1:]
                   courses = Courses(course, student_list)

        #print rooster
    #print zaalrooster
    return zaalrooster
main()
