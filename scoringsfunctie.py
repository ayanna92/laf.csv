# scoringsfunctie

# Ayanne, Femke en Lois

# functie die het aantal punten returned

#from random_algorithm import *
import csv
from class_rooms import *
from class_courses import *

fil_2 = open('vakken2.csv')
file_vakken = csv.reader(fil_2)
courses = []
fil_3 = open("classrooms.csv")
file_classrooms = csv.reader(fil_3)
classrooms = []
course_student_list = csv.reader(open('course_stud_num.csv'))
course_and_student = []
student_course_list = csv.reader(open('studentenenvakken.csv'))
Student_and_their_courses = []
all_information_courses = []

next(student_course_list)
for row in student_course_list:
    Student_and_their_courses.append(row)

for row in file_classrooms:
    classrooms.append(row)

for row in file_vakken:
    courses.append(row[0])
    all_information_courses.append(row)

for row in course_student_list:
    course_and_student.append(row)


def scoringsfunctie(schedule, students):


    schedule = schedule
    student_import_list = students

    #dict
    course_schedule_lecture_dict = {}
    course_schedule_seminars_dict = {}
    course_schedule_practicals_dict = {}
    course_schedule_dict = {}

    dag = 0
    tijdsblok = 0

    timeslot_seminar_list = []
    timeslot_practicals_list = []
    timeslot_lectures_list = []
    count  = 0

    #capacity_classroom_list = []
    points = 1000
    lost_point_capacity = 0

    # Make for each course a schedule when they are present in the schedule.
    # Lectures, seminars and practicals will be saved both seperately als together.
    for course in courses:
        capacity_vak = 0

        # for each classroom in the schedule calculate the capactity of the classrooom
        for rooms, schedule_each_room in schedule.items():
            zaal = 0
            capacity_classroom_list = 0
            for multiple_classrooms in classrooms:
                if rooms == multiple_classrooms[0]:
                    capacity_classroom_list = int(multiple_classrooms[1])

            # Check each timeslot if the course in timeslot equals the course that were looking for
            for zaal_per_dag in schedule_each_room:
                for vak_per_zaal in zaal_per_dag:
                    if course in vak_per_zaal:

                        # check which kind of activity the course is
                        # seminar:
                        if "werkgroep" in vak_per_zaal:
                            for row in all_information_courses:
                                if course == row[0]:
                                    capacity_vak = float(row[3])
                                    timeslot_seminar_list.append((dag,tijdsblok))

                        # lecture:
                        if "hoorcollege" in vak_per_zaal:
                            for students in course_and_student:
                                if students[0] == course:
                                   student_list = students[1:]
                                   vak_name = Courses(course, student_list)
                                   capacity_vak = vak_name.studNumber()
                                   timeslot_lectures_list.append((dag,tijdsblok))
                                   #print capacity_vak, "hoorcollege"

                        # practicals:
                        if "practica" in vak_per_zaal:
                            for row in all_information_courses:
                                if course== row[0]:
                                    capacity_vak = float(row[5])
                                    timeslot_practicals_list.append((dag,tijdsblok))

                        course_schedule_dict[vak_per_zaal] = ((dag,tijdsblok))
                        if capacity_vak > capacity_classroom_list:
                            #print "vak past niet in de zaal"
                            lost_point_capacity += (capacity_vak - capacity_classroom_list)

                        # voeg toe welke plaats tot het rooster.
                    tijdsblok += 1
                tijdsblok = 0
                dag = dag +1
            dag = 0

        course_schedule_lecture_dict[course] = timeslot_lectures_list
        course_schedule_practicals_dict[course] = timeslot_practicals_list
        course_schedule_seminars_dict[course] = timeslot_seminar_list

        timeslot_seminar_list = []
        timeslot_practicals_list = []
        timeslot_lectures_list = []

    #print " Het aantal minpunten vanwege studenten die niet in de zaal passen:" ,lost_point_capacity

    #course_schedule_practicals_dict
    #course_schedule_lecture_dict
    #course_schedule_seminars_dict
    #print " dit is het course_schedule_dict: ", course_schedule_dict


    bonuspunten = 0
    minpunten = 0
    for vak_activiteit in all_information_courses:
         number_of_activities = int(vak_activiteit[1]) + int(vak_activiteit[2]) + int(vak_activiteit[4])

          # de dagen van de colleges:
         daghoorcollege = course_schedule_lecture_dict[vak_activiteit[0]]
         dagwerkcollege = course_schedule_seminars_dict[vak_activiteit[0]]
         dagpracticum = course_schedule_practicals_dict[vak_activiteit[0]]
         daglijsthoor = []
         daglijstwerk = []
         daglijstprac = []
         for tijd in daghoorcollege:
            daglijsthoor.append(tijd[0])
            #print daglijsthoor
         for tijd in dagwerkcollege:
            daglijstwerk.append(tijd[0])
         for tijd in dagpracticum:
            daglijstprac.append(tijd[0])

         # alles uitschrijven op basis van het aantal activiteiten
         # bij 1 activiteit hoeft er niks gedaan te worden.
         # bij twee activiteiten:
         #
         #print vak_activiteit[0]
         if number_of_activities == 2:
             #print "    heeft twee activiteite"
             if len(daglijsthoor) == 2:
                 #print "           2 hoorcolleges"
                 verschil = abs(daglijsthoor[0]- daglijsthoor[1])
                 if verschil == 3:
                     bonuspunten += 20
                #     print "                    goed ingeroosterd"
                 elif verschil == 0 :  # dan zijn ze op 1 dag ingeroosterd
                     minpunten += 10
                #     print "                    2 colleges op 1 dag"

            # als er 1 hoorcollege en 1 werkgroep per week is
             if len(daglijsthoor) == 1 and daglijstwerk != []:
                #print "        1 hoorcollege en 1 werkcollege"
                #print "             verschillende werkgroepen:",len(daglijstwerk)
                for dag in daglijstwerk:
                    #print  daglijsthoor, dag
                    verschil = abs(daglijsthoor[0] - dag)
                    if verschil == 3:
                        bonuspunten += 20
                #        print "             goed ingeroosterd"
                    elif verschil == 0 :  # dan zijn ze op 1 dag ingeroosterd
                        minpunten += 10
                        #print "               2 colleges in 1 dag"

            # als er 1 hoorcollege en 1 practicum per week is:
             if len(daglijsthoor) == 1 and daglijstprac != []:
                 #print "        1 hoorcollege en 1 practica"
                 #print "                verschillende werkgroepen:",len(daglijstprac)
                 for dag in daglijstprac:
                  # print daglijsthoor, dag
                   verschil = abs(daglijsthoor[0] - dag)
                   if verschil == 3:
                       bonuspunten += 20
                    #   print    "           goed ingeroosterd"
                   elif verschil == 0 :  # dan zijn ze op 1 dag ingeroosterd
                       minpunten += 10
                     #  print "             2 colleges in 1 dag ingeroosterd"

         if number_of_activities == 3:
            #print "   er zijn 3 colleges"
            if len(daglijsthoor) == 2 and daglijstwerk != []:
                #print "         2 hoocolleges en 1 werkcollges"
                #print "             verschillende werkgroepen:",len(daglijstwerk)
                lijst = []
                for dag in daglijstwerk:
                    for dagen in daglijsthoor:
                        lijst.append(dagen)
                    lijst.append(dag)
                    list.sort(lijst)
                    #print lijst
                    if lijst[0] == 0 and lijst[1] == 2 and lijst[2] == 4:
                        bonuspunten += 20
                        #print "                 Goed ingeroosterd"
                    elif lijst[0] == lijst[1] == lijst[2]:
                        minpunten += 20
                        #print "                     3 colleges in 1 dag"
                    elif lijst[0] == lijst[1] or lijst[1] == lijst[2]:
                        minpunten += 10
                        #print "                     3 colleges in 2 dagen"

                    lijst = []

            if len(daglijsthoor) == 1 and daglijstwerk != [] and daglijstprac != []:
                #print "             van alles 1 college "
                lijst = []
                #print "         verschillende werkgroepen:",len(daglijstwerk)
                #print "         verschillende practica:",len(daglijstprac)
                for dag in daglijstwerk:
                    for dagen in daglijstprac:
                        lijst.append(daglijsthoor[0])
                        lijst.append(dag)
                        lijst.append(dagen)
                        list.sort(lijst)
                        #print lijst
                        if lijst[0] == 0 and lijst[1] == 2 and lijst[2] == 4:
                            bonuspunten += 20
                        #    print "                     goed gedaan"
                        elif lijst[0] == lijst[1] == lijst[2]:
                            minpunten += 20
                        #    print "                       3 colleges in 1 dag"
                        elif lijst[0] == lijst[1] or lijst[1] == lijst[2]:
                            minpunten += 10
                    #        print "                     3 colleges in 2 dagen"

                        lijst = []


         if number_of_activities == 4:
            #print "     er zijn vier activiteiten "
            if len(daglijsthoor) == 2 and daglijstwerk != [] and daglijstprac != []:
                #print  "        2 hoorcolleges, 1 werkcollege and 1 practica"
                lijst = []
                #print "verschillende werkgroepen:",len(daglijstwerk)
                #print "verschillende practica:",len(daglijstprac)
                for dag in daglijstwerk:
                    for dagen in daglijstprac:
                        for hoor in daglijsthoor:
                            lijst.append(hoor)
                        lijst.append(dag)
                        lijst.append(dagen)
                        list.sort(lijst)
                        #print lijst
                        if lijst[0] == 0 and lijst[1] == 1 and lijst[2] == 3 and lijst[3] == 4:
                            bonuspunten += 20
                            #print "                         extra goed "
                        elif lijst[0] == lijst[1] == lijst[2]==lijst[3]:
                            minpunten += 30
                            #print "                            4 colleges in 1 dag"
                        elif lijst[0] == lijst[1] == lijst[2] or lijst[1] == lijst[2] == lijst[3]:
                            minpunten += 20
                            #print "                           4 colleges in 2 dagen"
                        elif lijst[0] == lijst[1] and lijst[2]== lijst[3]:
                            minpunten += 20
                            #print "                             4 colleges in 2 dagen"
                        elif lijst[0] == lijst[1] or lijst[1] == lijst[2] or lijst[2] == lijst[3]:
                            minpunten += 10
                            #print "                         4 colleges in 3 dagen"
                        lijst = []
         if number_of_activities == 5:
            #print "     er zijn 5 acitviteiten"
            if len(daglijsthoor) == 3 and daglijstwerk != [] and daglijstprac != []:
                #print "            3 hoorcolleges, 1 werkcollege and 1 practica"
                #print "         verschillende werkgroepen:",len(daglijstwerk)
                #print "         verschillende practica:",len(daglijstprac)
                for dag in daglijstwerk:
                    for dagen in daglijstprac:
                        for hoor in daglijsthoor:
                            lijst.append(hoor)
                        lijst.append(dag)
                        lijst.append(dagen)
                        list.sort(lijst)
                        #print lijst
                        if lijst[0] == 0 and lijst[1] == 1 and lijst[2] == 2 and lijst[3] == 3 and lijst[4] == 4:
                            bonuspunten += 20
                            #print  "                    goed ingeoorsterd"
                        elif lijst[0] == lijst[1] == lijst[2] == lijst[3] == lijst [4]:
                            minpunten += 40
                            #print "                         5 colleges in 1 dag"
                        elif lijst[0] == lijst[1] == lijst[2] == lijst[3] or lijst[1] == lijst[2] == lijst[3] == lijst[4]:
                            minpunten += 30
                            #print "                         5 colleges in 2 dagen"
                        elif (lijst[0]== lijst[1] and lijst[2]== lijst[3] == lijst[4]) or (lijst[0] == lijst[1] == lijst[2] and lijst[3] == lijst[4]):
                            minpunten += 30
                            #print "                         5 colleges in 2 dagen"
                        elif lijst[0] == lijst[1] == lijst[2]  or lijst[1] == lijst[2] == lijst[3] or lijst[2]== lijst[3] == lijst[4]:
                            minpunten += 20
                            #print "                         5 colleges in 3 dagen"
                        elif (lijst[0]== lijst[1] and lijst[2]== lijst[3]) or (lijst[0] == lijst[1] and lijst[3] == lijst[4]) or (lijst[1] == lijst[2] and lijst[3] == lijst[4]):
                            minpunten += 20
                            #print "                         5 colleges in 3 dagen"
                        elif lijst[0] == lijst[1] or lijst[1] == lijst[2] or lijst[2] == lijst[3] or lijst[3] == lijst[4]:
                            minpunten += 10
                            #print "                         5 colleges in 4 dagen"

                        lijst = []

    #print " het aantal bonuspunten van dit rooster:", bonuspunten
    #print " het aantal minpunten van dit rooster:", minpunten


    # conflicten van de studenten berekenen:
    #print "iets"
    studentrooster = {}
    studierooster = student_import_list
    #print studierooster
    #print course_schedule_dict

    for student in Student_and_their_courses:
        studentenlijst = []
        studnumber = int(student[2])

        #print student
        for vak in student[3:7]:
            if vak != "":
                for vak1 in studierooster.items():

                    if vak in vak1[0]:
                        #print "hij zit er in"
                        #print vak
                        for studenten in vak1[1:]:
                            for stud in studenten:
                                if studnumber == int(stud):
                                    #print "true"
                                    #print vak
                                    #print vak1

                                    studentenlijst.append( course_schedule_dict[vak1[0]])

        studentrooster[studnumber] = studentenlijst
    #print studentrooster
    from collections import Counter
    #print studentrooster
    minpuntstudent = 0
    for student in studentrooster.values():
          waarde = Counter(student).values()
          #print waarde
          if len(waarde)!= len(student):
              minpuntstudent += (len(student) - len(waarde))
    #print " het aantal conflicten bij studenten:" ,minpuntstudent


    total = points + bonuspunten - lost_point_capacity - minpunten - minpuntstudent
    #print "total points is:", total
    #print studentrooster
    #print total
    return total
