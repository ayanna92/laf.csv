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
course_activity_student = {}
rooster=[]

def main ():

    import csv
    import math
    import random

    class_rooms_list = csv.reader(open('classrooms.csv'))
    course_stud_num = csv.reader(open('course_stud_num.csv'))

    lists = hoofd_main()
    course_and_activity = lists[0]
    random.shuffle(course_and_activity)


    class_rooms = []
    course_and_student = []
    student_list = []

    # ipmort the right students to the right course
    for row in course_stud_num:
        course_and_student.append(row)


    # import classrooms and put them random in a list
    for row in class_rooms_list:
        class_rooms.append(row)
    random.shuffle(class_rooms)


    #pick a room
    for row in class_rooms:
        name = row[0]
        capacity = row[1]
        room = Classrooms(name, capacity)

        #create empry week for the room
        week = room.createEmptyWeek()

        for weeks in range(20):

            course = course_and_activity[0]
            course_and_activity.pop(0)

            for row in course_and_student:

                if row[0] in course:
                    student_list = row[1:]

                    object_course = Courses(row[0], student_list)
                    amount_werkcolleges = object_course.werkcolleges(row[0])
                    amount_practica = object_course.practica(row[0])

                        # if there are more than 1 activity per course (hoorcolleges excluded), devide the students, first half in activity 1, second half in activity 2
                    if 'werkgroep 1' in course:
                        index = len(student_list)/int(amount_werkcolleges)
                        student_list = student_list[0:index]

                    if 'werkgroep 2' in course:
                        index = len(student_list)/int(amount_werkcolleges)
                        student_list = student_list[index:index+index]

                    if 'werkgroep 3' in course:
                        index = len(student_list)/int(amount_werkcolleges)
                        student_list = student_list[index+index:index+index+index]

                    if 'werkgroep 4' in course:
                        index = len(student_list)/int(amount_werkcolleges)
                        student_list = student_list[index+index+index:index+index+index+index]

                    if 'practica 1' in course:
                        index = len(student_list)/int(amount_practica)
                        student_list = student_list[0:index]

                    if 'practica 2' in course:
                        index = len(student_list)/int(amount_practica)
                        student_list = student_list[index:index+index]

                    if 'practica 3' in course:
                        index = len(student_list)/int(amount_practica)
                        student_list = student_list[index+index:index+index+index]

                    if 'practica 4' in course:
                        index = len(student_list)/int(amount_practica)
                        student_list = student_list[index+index+index:index+index+index+index]


                if course == '':
                    student_list = []
                #dictionary; key is the activity, value is the list of students for that specific activity
            course_activity_student[course] = student_list
            #print course_activity_student

            # fill the schedule with the course
            rooster = room.fillInWeek(course, week)
            zaalrooster[name] = rooster
        #print rooster

    #print course_activity_student
    #print zaalrooster
    #print course_activity_student
    return (zaalrooster, course_activity_student)

#main()
