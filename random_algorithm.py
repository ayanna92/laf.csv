# trying to make a schedule for at least one room
# Lectures & roosters
#
# Ayanna, Lois, Femke
#
import csv
import copy
from class_rooms import *
from class_courses import *
from main import *
from visualize import *
from scoringsfunctie import *

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

                # finding the students following the course and activity
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

            rooster = room.fillInWeek(course, week)
            zaalrooster[name] = rooster

    #print "The random schedule is:", zaalrooster
    #print "The score of the random schedule is: ", scoringsfunctie(zaalrooster, course_activity_student)

    #to visualize a schedule of a classroom of the random algorithm
    key = ['A1.04', 'A1.06', 'A1.08', 'A1.10', 'B0.201', 'C0.110', 'C1.112']

    for i in range(len(key)):
        Visualization(key[i]).fillSchedule(zaalrooster)
    Visualization(key).done()
        #Visualization('fill in classroom').fillSchedule(zaalrooster)

    return (zaalrooster, course_activity_student)

main()
