# scoringsfunctie

# Ayanne, Femke en Lois

# functie die het aantal punten returned

import csv
from class_rooms import *
from class_courses import *
from collections import Counter

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

    # print "lost points due to capacity clasrooms:", lost_point_capacity


    # next step is to calculate the bonuspoints and lost points that are caused
    # when a course and their acivities are scheduled on the same day, or on different days.
    bonuspoints = 0
    lost_points_activity = 0
    for course_activity in all_information_courses:
         number_of_activities = int(course_activity[1]) + int(course_activity[2]) + int(course_activity[4])

         lecture_list_day = course_schedule_lecture_dict[course_activity[0]]
         seminar_list_day = course_schedule_seminars_dict[course_activity[0]]
         practicals_list_day = course_schedule_practicals_dict[course_activity[0]]
         day_list_lectur = []
         day_list_seminar = []
         day_list_practicals = []

         # make lists of what times the activities are
         for tijd in lecture_list_day:
            day_list_lectur.append(tijd[0])
         for tijd in seminar_list_day:
            day_list_seminar.append(tijd[0])
         for tijd in practicals_list_day:
            day_list_practicals.append(tijd[0])

         # for each number of activities there are different situations:
         if number_of_activities == 2:
             if len(day_list_lectur) == 2:
                 verschil = abs(day_list_lectur[0]- day_list_lectur[1])
                 if verschil == 3:
                     bonuspoints += 20
                 elif verschil == 0 :
                     lost_points_activity += 10

             if len(day_list_lectur) == 1 and day_list_seminar != []:
                for dag in day_list_seminar:

                    verschil = abs(day_list_lectur[0] - dag)
                    if verschil == 3:
                        bonuspoints += 20

                    elif verschil == 0 :
                        lost_points_activity += 10


             if len(day_list_lectur) == 1 and day_list_practicals != []:
                 for dag in day_list_practicals:
                   verschil = abs(day_list_lectur[0] - dag)
                   if verschil == 3:
                       bonuspoints += 20

                   elif verschil == 0 :
                       lost_points_activity += 10

         if number_of_activities == 3:
            if len(day_list_lectur) == 2 and day_list_seminar != []:
                lijst = []
                for dag in day_list_seminar:
                    for dagen in day_list_lectur:
                        lijst.append(dagen)
                    lijst.append(dag)
                    list.sort(lijst)
                    if lijst[0] == 0 and lijst[1] == 2 and lijst[2] == 4:
                        bonuspoints += 20
                    elif lijst[0] == lijst[1] == lijst[2]:
                        lost_points_activity += 20
                    elif lijst[0] == lijst[1] or lijst[1] == lijst[2]:
                        lost_points_activity += 10

                    lijst = []

            if len(day_list_lectur) == 1 and day_list_seminar != [] and day_list_practicals != []:
                lijst = []
                for dag in day_list_seminar:
                    for dagen in day_list_practicals:
                        lijst.append(day_list_lectur[0])
                        lijst.append(dag)
                        lijst.append(dagen)
                        list.sort(lijst)
                        if lijst[0] == 0 and lijst[1] == 2 and lijst[2] == 4:
                            bonuspoints += 20
                        elif lijst[0] == lijst[1] == lijst[2]:
                            lost_points_activity += 20
                        elif lijst[0] == lijst[1] or lijst[1] == lijst[2]:
                            lost_points_activity += 10

                        lijst = []


         if number_of_activities == 4:
            if len(day_list_lectur) == 2 and day_list_seminar != [] and day_list_practicals != []:
                lijst = []
                for dag in day_list_seminar:
                    for dagen in day_list_practicals:
                        for hoor in day_list_lectur:
                            lijst.append(hoor)
                        lijst.append(dag)
                        lijst.append(dagen)
                        list.sort(lijst)
                        if lijst[0] == 0 and lijst[1] == 1 and lijst[2] == 3 and lijst[3] == 4:
                            bonuspoints += 20
                        elif lijst[0] == lijst[1] == lijst[2]==lijst[3]:
                            lost_points_activity += 30
                        elif lijst[0] == lijst[1] == lijst[2] or lijst[1] == lijst[2] == lijst[3]:
                            lost_points_activity += 20
                        elif lijst[0] == lijst[1] and lijst[2]== lijst[3]:
                            lost_points_activity += 20
                        elif lijst[0] == lijst[1] or lijst[1] == lijst[2] or lijst[2] == lijst[3]:
                            lost_points_activity += 10
                        lijst = []
         if number_of_activities == 5:
            if len(day_list_lectur) == 3 and day_list_seminar != [] and day_list_practicals != []:
                for dag in day_list_seminar:
                    for dagen in day_list_practicals:
                        for hoor in day_list_lectur:
                            lijst.append(hoor)
                        lijst.append(dag)
                        lijst.append(dagen)
                        list.sort(lijst)
                        if lijst[0] == 0 and lijst[1] == 1 and lijst[2] == 2 and lijst[3] == 3 and lijst[4] == 4:
                            bonuspoints += 20
                        elif lijst[0] == lijst[1] == lijst[2] == lijst[3] == lijst [4]:
                            lost_points_activity += 40
                        elif lijst[0] == lijst[1] == lijst[2] == lijst[3] or lijst[1] == lijst[2] == lijst[3] == lijst[4]:
                            lost_points_activity += 30
                        elif (lijst[0]== lijst[1] and lijst[2]== lijst[3] == lijst[4]) or (lijst[0] == lijst[1] == lijst[2] and lijst[3] == lijst[4]):
                            lost_points_activity += 30
                        elif lijst[0] == lijst[1] == lijst[2]  or lijst[1] == lijst[2] == lijst[3] or lijst[2]== lijst[3] == lijst[4]:
                            lost_points_activity += 20
                        elif (lijst[0]== lijst[1] and lijst[2]== lijst[3]) or (lijst[0] == lijst[1] and lijst[3] == lijst[4]) or (lijst[1] == lijst[2] and lijst[3] == lijst[4]):
                            lost_points_activity += 20
                        elif lijst[0] == lijst[1] or lijst[1] == lijst[2] or lijst[2] == lijst[3] or lijst[3] == lijst[4]:
                            lost_points_activity += 10

                        lijst = []

    # print "number of bonuspoints due to good spread of the course:", bonuspoints
    # print "number of lostpoints due to bad spread of the course:", lost_points_activity
    student_schedules = {}
    student_and_courses_schedule = student_import_list


    # in this section, lost points are calculated that are caused by conflicten timeslots for student.
    # first make for each student a schedule with day and time slots
    for student in Student_and_their_courses:
        studentenlijst = []
        studnumber = int(student[2])

        for course in student[3:7]:
            if course != "":
                for course_and_its_students in student_and_courses_schedule.items():
                    if course in course_and_its_students[0]:
                        for studenten in course_and_its_students[1:]:
                            for stud in studenten:
                                if studnumber == int(stud):
                                    studentenlijst.append( course_schedule_dict[course_and_its_students[0]])

        student_schedules[studnumber] = studentenlijst

    loss_points_student = 0
    for student in student_schedules.values():
          unique_values = Counter(student).values()
          if len(unique_values)!= len(student):
              loss_points_student += (len(student) - len(unique_values))

    total = points + bonuspoints - lost_point_capacity - lost_points_activity - loss_points_student
    #print"total points is:", total
    #print student_schedules
    #print total
    return total
