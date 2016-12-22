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
    #Visualization('fill in classroom').fillSchedule(zaalrooster)

    return (zaalrooster, course_activity_student)

#main()
starting_schedule = ({'B0.201': [['Zoeken sturen en bewegen practica 3', 'Technology for games werkgroep 2', 'Reflectie op de digitale cultuur werkgroep 1', 'Software engineering practica 2'], ['Webprogrammeren en databases hoorcollege 2', 'Heuristieken 2 hoorcollege 1', 'Data Mining practica 2', 'Data Mining practica 1'], ['Technology for games hoorcollege 2', 'Zoeken sturen en bewegen practica 1', 'Collectieve Intelligentie werkgroep 4', 'Bioinformatica practica 2'], ['Compilerbouw werkgroep 2', 'Data Mining hoorcollege 1', 'Bioinformatica hoorcollege 1', 'Databases 2 werkgroep 1'], ['Data Mining hoorcollege 2', 'Moderne Databases werkgroep 1', 'Algoritmen en complexiteit hoorcollege 1', 'Technology for games hoorcollege 1']], 'A1.08': [['Collectieve Intelligentie practica 1', 'Informatie- en organisatieontwerp practica 1', 'Collectieve Intelligentie practica 2', 'Informatie- en organisatieontwerp practica 2'], ['Technology for games werkgroep 1', 'Project Numerical Recipes practica 2', 'Programmeren in Java 2 practica 1', 'Project Genetic Algorithms practica 3'], ['Collectieve Intelligentie werkgroep 1', 'Reflectie op de digitale cultuur werkgroep 3', 'Moderne Databases practica 3', 'Webprogrammeren en databases practica 1'], ['Reflectie op de digitale cultuur werkgroep 2', 'Netwerken en systeembeveiliging practica 3', 'Informatie- en organisatieontwerp hoorcollege 1', 'Autonomous Agents 2 werkgroep 1'], ['Autonomous Agents 2 practica 2', 'Advanced Heuristics hoorcollege 1', 'Informatie- en organisatieontwerp werkgroep 1', 'Autonomous Agents 2 practica 3']], 'C0.110': [['Databases 2 hoorcollege 1', 'Bioinformatica hoorcollege 2', 'Algoritmen en complexiteit werkgroep 2', 'Data Mining werkgroep 1'], ['Compilerbouw hoorcollege 1', 'Zoeken sturen en bewegen practica 2', 'Collectieve Intelligentie hoorcollege 1', 'Calculus 2 hoorcollege 1'], ['Software engineering hoorcollege 1', 'Collectieve Intelligentie werkgroep 2', 'Kansrekenen 2 hoorcollege 1', 'Algoritmen en complexiteit practica 1'], ['Compilerbouw werkgroep 1', 'Collectieve Intelligentie hoorcollege 2', 'Lineaire Algebra hoorcollege 1', 'Kansrekenen 2 hoorcollege 2'], ['Compilerbouw hoorcollege 2', 'Collectieve Intelligentie hoorcollege 3', 'Webprogrammeren en databases werkgroep 1', 'Software engineering werkgroep 1']], 'A1.04': [['Machine Learning hoorcollege 1', 'Algoritmen en complexiteit werkgroep 1', 'Compilerbouw practica 2', 'Heuristieken 1 werkgroep 1'], ['Autonomous Agents 2 hoorcollege 2', 'Interactie-ontwerp hoorcollege 1', 'Project Genetic Algorithms practica 1', 'Netwerken en systeembeveiliging practica 2'], ['Netwerken en systeembeveiliging practica 4', 'Moderne Databases practica 1', 'Project Genetic Algorithms practica 2', 'Bioinformatica practica 1'], ['Webprogrammeren en databases hoorcollege 1', 'Autonomous Agents 2 werkgroep 3', 'Project Numerical Recipes practica 3', 'Databases 2 werkgroep 2'], ['Software engineering werkgroep 2', 'Webprogrammeren en databases werkgroep 2', 'Moderne Databases werkgroep 2', 'Calculus 2 werkgroep 3']], 'A1.06': [['Data Mining werkgroep 2', 'Webprogrammeren en databases practica 2', 'Data Mining werkgroep 3', 'Collectieve Intelligentie practica 3'], ['Netwerken en systeembeveiliging practica 1', 'Architectuur en computerorganisatie hoorcollege 2', 'Advanced Heuristics practica 2', 'Project Numerical Recipes practica 1'], ['Moderne Databases practica 2', 'Collectieve Intelligentie werkgroep 3', 'Programmeren in Java 2 practica 3', 'Programmeren in Java 2 practica 2'], ['', '', '', 'Autonomous Agents 2 werkgroep 2'], ['Moderne Databases werkgroep 3', 'Informatie- en organisatieontwerp werkgroep 2', 'Interactie-ontwerp hoorcollege 2', 'Architectuur en computerorganisatie hoorcollege 1']], 'C1.112': [['Software engineering practica 1', 'Reflectie op de digitale cultuur hoorcollege 2', 'Lineaire Algebra hoorcollege 2', 'Compilerbouw practica 1'], ['Advanced Heuristics practica 1', 'Bioinformatica werkgroep 3', '', 'Informatie- en organisatieontwerp hoorcollege 2'], ['', 'practicum_compilerbouw practica 1', '', 'Algoritmen en complexiteit practica 2'], ['Heuristieken 1 hoorcollege 1', 'Analysemethoden en -technieken hoorcollege 1', '', 'practicum_compilerbouw practica 2'], ['Autonomous Agents 2 practica 1', 'Heuristieken 2 werkgroep 1', 'Bioinformatica hoorcollege 3', 'Heuristieken 2 werkgroep 2']], 'A1.10': [['Heuristieken 1 werkgroep 2', 'Autonomous Agents 2 hoorcollege 1', 'Moderne Databases hoorcollege 1', 'Collectieve Intelligentie practica 4'], ['Data Mining practica 3', '', 'Bioinformatica werkgroep 1', 'Bioinformatica werkgroep 2'], ['Bioinformatica practica 3', 'Programmeren in Java 2 practica 4', 'practicum_compilerbouw practica 3', ''], ['', 'practicum_compilerbouw practica 4', 'Machine Learning hoorcollege 2', ''], ['Calculus 2 werkgroep 2', '', 'Reflectie op de digitale cultuur hoorcollege 1', 'Calculus 2 werkgroep 1']]})

schedule, courses = main()
print scoringsfunctie(starting_schedule, courses)
