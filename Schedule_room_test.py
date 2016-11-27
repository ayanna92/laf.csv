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
    courses = []
    name_course = []
    course_and_student = []

    for row in course_student_list:
        course_and_student.append(row)

    for row in courses_list:
        courses.append(row)

    for row in courses:
        name_course.append(row[0])

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

                   #if courses.hoorcollege(course) != 0:
                     #  course_act = course + ' hoorcollege'
                     #  rooster = room.fillInWeek(course_act, week)

                    #print course
                    #print student_list
                    #print courses.hoorcollege(course)
        #print rooster
    return zaalrooster
main()
