# scoringsfunctie

# Ayanna, Femke en Lois

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


def scorefunction(schedule, students):

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
                        if "lecturecollege" in course_timeslot:
                            for students in course_and_student:
                                if students[0] == course:
                                   student_list = students[1:]
                                   vak_name = Courses(course, student_list)
                                   capacity_course = vak_name.studNumber()
                                   timeslot_lectures_list.append((day,timeslot))
                                   #print capacity_course, "lecturecollege"

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
                            print "true"
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

          # make list of when the acitivities of the specific course are planned.
         lecture_day = course_schedule_lecture_dict[course_activity[0]]
         seminar_day = course_schedule_seminars_dict[course_activity[0]]
         practicals_day = course_schedule_practicals_dict[course_activity[0]]
         lecture_day_list = []
         seminar_day_list = []
         practicals_day_list = []
         for tijd in lecture_day:
            lecture_day_list.append(tijd[0])
         for tijd in seminar_day:
            seminar_day_list.append(tijd[0])
         for tijd in practicals_day:
            practicals_day_list.append(tijd[0])



        # For each amount of activities there are different scenarios for when you get
        # bonuspoints and when you lose point.
         if number_of_activities == 2:
             if len(lecture_day_list) == 2:
                 difference = abs(lecture_day_list[0]- lecture_day_list[1])
                 if difference == 3:
                     bonuspoints += 20
                # when they are scheduled for x-1 days:
                 elif difference == 0 :
                     lost_points_activity += 10

            # If there is 1 lecture and 1 seminar
            # every saminar consists of multiple groups. Each groep is compared to the lecture.
             if len(lecture_day_list) == 1 and seminar_day_list != []:
                for day in seminar_day_list:
                    difference = abs(lecture_day_list[0] - day)
                    if difference == 3:
                        bonuspoints += 20
                    elif difference == 0 :
                        lost_points_activity += 10

            # If there is 1 lecture and 1 seminar
            # every practical consists of multiple groups. Each groep is compared to the lecture.
             if len(lecture_day_list) == 1 and practicals_day_list != []:
                 for day in practicals_day_list:
                   difference = abs(lecture_day_list[0] - day)
                   if difference == 3:
                       bonuspoints += 20
                   elif difference == 0 :
                       lost_points_activity += 10

         if number_of_activities == 3:

             # 2 lectures and 1 seminar
            if len(lecture_day_list) == 2 and seminar_day_list != []:

                # create empty list and fill it with the lectures and one groep within seminars
                list_activity = []
                for day in seminar_day_list:
                    for times in lecture_day_list:
                        list_activity.append(times)
                    list_activity.append(day)
                    list.sort(list_activity)
                    if list_activity[0] == 0 and list_activity[1] == 2 and list_activity[2] == 4:
                        bonuspoints += 20
                    elif list_activity[0] == list_activity[1] == list_activity[2]:
                        lost_points_activity += 20
                    elif list_activity[0] == list_activity[1] or list_activity[1] == list_activity[2]:
                        lost_points_activity += 10

                    # make list empty
                    list_activity = []

            if len(lecture_day_list) == 1 and seminar_day_list != [] and practicals_day_list != []:

                list_activity = []

                for day in seminar_day_list:
                    for group in practicals_day_list:
                        list_activity.append(lecture_day_list[0])
                        list_activity.append(day)
                        list_activity.append(group)
                        list.sort(list_activity)

                        if list_activity[0] == 0 and list_activity[1] == 2 and list_activity[2] == 4:
                            bonuspoints += 20

                        elif list_activity[0] == list_activity[1] == list_activity[2]:
                            lost_points_activity += 20

                        elif list_activity[0] == list_activity[1] or list_activity[1] == list_activity[2]:
                            lost_points_activity += 10

                        list_activity = []


         if number_of_activities == 4:
            if len(lecture_day_list) == 2 and seminar_day_list != [] and practicals_day_list != []:
                list_activity = []
                for day in seminar_day_list:
                    for group in practicals_day_list:
                        for lecture in lecture_day_list:
                            list_activity.append(lecture)
                        list_activity.append(day)
                        list_activity.append(group)
                        list.sort(list_activity)
                        if list_activity[0] == 0 and list_activity[1] == 1 and list_activity[2] == 3 and list_activity[3] == 4:
                            bonuspoints += 20
                        elif list_activity[0] == list_activity[1] == list_activity[2]==list_activity[3]:
                            lost_points_activity += 30
                        elif list_activity[0] == list_activity[1] == list_activity[2] or list_activity[1] == list_activity[2] == list_activity[3]:
                            lost_points_activity += 20
                        elif list_activity[0] == list_activity[1] and list_activity[2]== list_activity[3]:
                            lost_points_activity += 20
                        elif list_activity[0] == list_activity[1] or list_activity[1] == list_activity[2] or list_activity[2] == list_activity[3]:
                            lost_points_activity += 10
                        list_activity = []

         if number_of_activities == 5:

            if len(lecture_day_list) == 3 and seminar_day_list != [] and practicals_day_list != []:
                for day in seminar_day_list:
                    for group in practicals_day_list:
                        for lecture in lecture_day_list:
                            list_activity.append(lecture)
                        list_activity.append(day)
                        list_activity.append(group)
                        list.sort(list_activity)
                        if list_activity[0] == 0 and list_activity[1] == 1 and list_activity[2] == 2 and list_activity[3] == 3 and list_activity[4] == 4:
                            bonuspoints += 20

                        elif list_activity[0] == list_activity[1] == list_activity[2] == list_activity[3] == list_activity [4]:
                            lost_points_activity += 40

                        elif list_activity[0] == list_activity[1] == list_activity[2] == list_activity[3] or list_activity[1] == list_activity[2] == list_activity[3] == list_activity[4]:
                            lost_points_activity += 30

                        elif (list_activity[0]== list_activity[1] and list_activity[2]== list_activity[3] == list_activity[4]) or (list_activity[0] == list_activity[1] == list_activity[2] and list_activity[3] == list_activity[4]):
                            lost_points_activity += 30

                        elif list_activity[0] == list_activity[1] == list_activity[2]  or list_activity[1] == list_activity[2] == list_activity[3] or list_activity[2]== list_activity[3] == list_activity[4]:
                            lost_points_activity += 20

                        elif (list_activity[0]== list_activity[1] and list_activity[2]== list_activity[3]) or (list_activity[0] == list_activity[1] and list_activity[3] == list_activity[4]) or (list_activity[1] == list_activity[2] and list_activity[3] == list_activity[4]):
                            lost_points_activity += 20

                        elif list_activity[0] == list_activity[1] or list_activity[1] == list_activity[2] or list_activity[2] == list_activity[3] or list_activity[3] == list_activity[4]:
                            lost_points_activity += 10


                        list_activity = []

    # In the next section the amount of conflicts for each student are calculated
    # First an dicitionary for each student is made. the values are the times that the student is busy.
    student_dict = {}
    studierooster = student_import_list
    #print studierooster

    for student in Student_and_their_courses:
        studentenlist_activity = []
        studnumber = int(student[2])

        for student_course in student[3:7]:
            if student_course != "":
                for course_student in studierooster.items():

                    if student_course in course_student[0]:

                        for studenten in course_student[1:]:
                            for stud in studenten:
                                if studnumber == int(stud):

                                    studentenlist_activity.append(course_schedule_dict[course_student[0]])

        student_dict[studnumber] = studentenlist_activity

    conflicts_student = 0
    for student in student_dict.values():
          unique_timeslots = Counter(student).values()
          if len(unique_timeslots)!= len(student):
              conflicts_student += (len(student) - len(unique_timeslots))

    print bonuspoints, lost_point_capacity, lost_points_activity, conflicts_student

    # calculate points
    total = points + bonuspoints - lost_point_capacity - lost_points_activity - conflicts_student

    return total
