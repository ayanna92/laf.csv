# scoringsfunctie

# Ayanne, Femke en Lois

# functie die het aantal punten returned
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

    day = 0
    timeslot = 0

    timeslot_seminar_list = []
    timeslot_practicals_list = []
    timeslot_lectures_list = []
    count  = 0

    points = 1000
    lost_point_capacity = 0

    # Make for each course a schedule when they are present in the schedule.
    # Lectures, seminars and practicals will be saved both seperately and together.
    for course in courses:
        capacity_course = 0

        # for each classroom in the schedule calculate the capactity of the classrooom
        for rooms, schedule_each_room in schedule.items():
            zaal = 0
            capacity_classroom = 0
            for multiple_classrooms in classrooms:
                if rooms == multiple_classrooms[0]:
                    capacity_classroom = int(multiple_classrooms[1])

            # Check each timeslot if the course in timeslot equals the course that were looking for
            for day_in_room in schedule_each_room:
                for course_timeslot in day_in_room:
                    if course in course_timeslot:

                        # check which kind of activity the course is and append the times (days,timeslot) to their list.
                        # seminar:
                        if "werkgroep" in course_timeslot:
                            for row in all_information_courses:
                                if course == row[0]:
                                    capacity_course = float(row[3])
                                    timeslot_seminar_list.append((day,timeslot))

                        # lecture:
                        if "hoorcollege" in course_timeslot:
                            for students in course_and_student:
                                if students[0] == course:
                                   student_list = students[1:]
                                   vak_name = Courses(course, student_list)
                                   capacity_course = vak_name.studNumber()
                                   timeslot_lectures_list.append((day,timeslot))
                                   #print capacity_course, "hoorcollege"

                        # practicals:
                        if "practica" in course_timeslot:
                            for row in all_information_courses:
                                if course== row[0]:
                                    capacity_course = float(row[5])
                                    timeslot_practicals_list.append((day,timeslot))

                        # add time to the dictionay where each time is saved in.
                        course_schedule_dict[course_timeslot] = ((day,timeslot))

                        # calculate how many students dont fit in the room if the
                        # capacity is smaller than the amount of students
                        if capacity_course > capacity_classroom:
                            lost_point_capacity += (capacity_course - capacity_classroom)

                    timeslot += 1
                timeslot = 0
                day = day +1
            day = 0


        # add the lists to their dictionaries.
        course_schedule_lecture_dict[course] = timeslot_lectures_list
        course_schedule_practicals_dict[course] = timeslot_practicals_list
        course_schedule_seminars_dict[course] = timeslot_seminar_list

        # make the lists empty for the next course.
        timeslot_seminar_list = []
        timeslot_practicals_list = []
        timeslot_lectures_list = []



    # next step is to calculate the bonuspoints and lost points that are caused
    # when a course and their acivities are scheduled on the same day, or on different days.
    bonuspoints = 0
    lost_points_activity = 0
    for course_activity in all_information_courses:
         number_of_activities = int(course_activity[1]) + int(course_activity[2]) + int(course_activity[4])

          # de dagen van de colleges:
         daghoorcollege = course_schedule_lecture_dict[course_activity[0]]
         dagwerkcollege = course_schedule_seminars_dict[course_activity[0]]
         dagpracticum = course_schedule_practicals_dict[course_activity[0]]
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
         #print course_activity[0]
         if number_of_activities == 2:
             #print "    heeft twee activiteite"
             if len(daglijsthoor) == 2:
                 #print "           2 hoorcolleges"
                 verschil = abs(daglijsthoor[0]- daglijsthoor[1])
                 if verschil == 3:
                     bonuspoints += 20
                #     print "                    goed ingeroosterd"
                 elif verschil == 0 :  # dan zijn ze op 1 dag ingeroosterd
                     lost_points_activity += 10
                #     print "                    2 colleges op 1 dag"

            # als er 1 hoorcollege en 1 werkgroep per week is
             if len(daglijsthoor) == 1 and daglijstwerk != []:
                #print "        1 hoorcollege en 1 werkcollege"
                #print "             verschillende werkgroepen:",len(daglijstwerk)
                for dag in daglijstwerk:
                    #print  daglijsthoor, dag
                    verschil = abs(daglijsthoor[0] - dag)
                    if verschil == 3:
                        bonuspoints += 20
                #        print "             goed ingeroosterd"
                    elif verschil == 0 :  # dan zijn ze op 1 dag ingeroosterd
                        lost_points_activity += 10
                        #print "               2 colleges in 1 dag"

            # als er 1 hoorcollege en 1 practicum per week is:
             if len(daglijsthoor) == 1 and daglijstprac != []:
                 #print "        1 hoorcollege en 1 practica"
                 #print "                verschillende werkgroepen:",len(daglijstprac)
                 for dag in daglijstprac:
                  # print daglijsthoor, dag
                   verschil = abs(daglijsthoor[0] - dag)
                   if verschil == 3:
                       bonuspoints += 20
                    #   print    "           goed ingeroosterd"
                   elif verschil == 0 :  # dan zijn ze op 1 dag ingeroosterd
                       lost_points_activity += 10
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
                        bonuspoints += 20
                        #print "                 Goed ingeroosterd"
                    elif lijst[0] == lijst[1] == lijst[2]:
                        lost_points_activity += 20
                        #print "                     3 colleges in 1 dag"
                    elif lijst[0] == lijst[1] or lijst[1] == lijst[2]:
                        lost_points_activity += 10
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
                            bonuspoints += 20
                        #    print "                     goed gedaan"
                        elif lijst[0] == lijst[1] == lijst[2]:
                            lost_points_activity += 20
                        #    print "                       3 colleges in 1 dag"
                        elif lijst[0] == lijst[1] or lijst[1] == lijst[2]:
                            lost_points_activity += 10
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
                            bonuspoints += 20
                            #print "                         extra goed "
                        elif lijst[0] == lijst[1] == lijst[2]==lijst[3]:
                            lost_points_activity += 30
                            #print "                            4 colleges in 1 dag"
                        elif lijst[0] == lijst[1] == lijst[2] or lijst[1] == lijst[2] == lijst[3]:
                            lost_points_activity += 20
                            #print "                           4 colleges in 2 dagen"
                        elif lijst[0] == lijst[1] and lijst[2]== lijst[3]:
                            lost_points_activity += 20
                            #print "                             4 colleges in 2 dagen"
                        elif lijst[0] == lijst[1] or lijst[1] == lijst[2] or lijst[2] == lijst[3]:
                            lost_points_activity += 10
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
                            bonuspoints += 20
                            #print  "                    goed ingeoorsterd"
                        elif lijst[0] == lijst[1] == lijst[2] == lijst[3] == lijst [4]:
                            lost_points_activity += 40
                            #print "                         5 colleges in 1 dag"
                        elif lijst[0] == lijst[1] == lijst[2] == lijst[3] or lijst[1] == lijst[2] == lijst[3] == lijst[4]:
                            lost_points_activity += 30
                            #print "                         5 colleges in 2 dagen"
                        elif (lijst[0]== lijst[1] and lijst[2]== lijst[3] == lijst[4]) or (lijst[0] == lijst[1] == lijst[2] and lijst[3] == lijst[4]):
                            lost_points_activity += 30
                            #print "                         5 colleges in 2 dagen"
                        elif lijst[0] == lijst[1] == lijst[2]  or lijst[1] == lijst[2] == lijst[3] or lijst[2]== lijst[3] == lijst[4]:
                            lost_points_activity += 20
                            #print "                         5 colleges in 3 dagen"
                        elif (lijst[0]== lijst[1] and lijst[2]== lijst[3]) or (lijst[0] == lijst[1] and lijst[3] == lijst[4]) or (lijst[1] == lijst[2] and lijst[3] == lijst[4]):
                            lost_points_activity += 20
                            #print "                         5 colleges in 3 dagen"
                        elif lijst[0] == lijst[1] or lijst[1] == lijst[2] or lijst[2] == lijst[3] or lijst[3] == lijst[4]:
                            lost_points_activity += 10
                            #print "                         5 colleges in 4 dagen"

                        lijst = []

    #print " het aantal bonuspoints van dit rooster:", bonuspoints
    #print " het aantal lost_points_activity van dit rooster:", lost_points_activity


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


    total = points + bonuspoints - lost_point_capacity - lost_points_activity - minpuntstudent
    #print "total points is:", total
    #print studentrooster
    #print total
    return total
