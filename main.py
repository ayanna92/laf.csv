
from class_students import *
from class_courses import *
from class_rooms import *

def hoofd_main():

    import csv
    import math

    # open and read csv files
    open_1 = open('studentenenvakken.csv')
    file_1 = csv.reader(open_1)
    fil_2 = open('vakken2.csv')
    file_vakken = csv.reader(fil_2)
    fil = open('classrooms.csv')
    file_zalen = csv.reader(fil)
    courses_and_students = csv.reader(open('course_stud_num.csv'))

    # make empty list for student information, and list which will contain info
    stud_info = []
    stud_list = []
    vak_list = []
    classroom_name = []
    cours_student = []
    course_and_activity = []

    # fills empty list with student information
    for row in file_1:
        stud_info.append(row)

    # for every column in student info
    for col in stud_info[1:]:

        # student number ( in column 2)
        stud_num = col[2]

        # make empty list for courses and fill list with rows from
        # column 3 - end
        # don't add if column is empty ("") and fill list
        stud_vak = []
        for vak in col[3:]:
            if vak != "":
                stud_vak.append(vak)

        # add student object to list
        stud = Students(stud_num, stud_vak)
        stud_list.append(stud)

        # courses of students for loop
        for vakken in stud_vak:
            exist_vak = False

            # check if vakken exists already
            for vak in vak_list:

                # if vak name and vakken are the same, add student number to existing
                if vak.name_course == vakken:
                    vak.students.append(stud_num)
                    exist_vak = True


            # if vakken doesn't exist yet, create a new course and add student
            if exist_vak == False:
                if vakken != '':
                    students = []
                    course = Courses(vakken, students)
                    vak_list.append(course)
                    course.students.append(stud_num)

    zalen = []
    classroom_list = []

    # put csv file in variable zalen
    for rows in file_zalen:
        zalen.append(rows)

    # put al the room numbers in room
    for col in zalen:
        room = col[0]
        capacity = col[1]

        # add classroom object to list
        classroom = Classrooms(room, capacity)
        classroom_list.append(classroom)
        classroom_name.append(col[0])

    # add new list for type of activity
    courses = []
    courses_list = []

    # read csv file in variable courses
    for row in file_vakken:
        courses.append(row)

    # put al the courses names in variable names
    for col in courses[0:]:
        name = col[0]

    ## CODE FOR READING IN COURSES AND ACTIVITY
    # for all the 29 courses
    for col in courses[0:]:
        name = col[0]

        # and for each student for that course
        for row in courses_and_students:
            cours_student.append(row)

        # remember the name of the course
        for col in courses[0:]:
            course = col[0]

            # take all the students of that course
            for students in cours_student:
                if students[0] == course:
                    student_list_courses = students[1:]
                    courses = Courses(course, student_list_courses)

            # find through class courses how many hoorcollege, werkcollege and practia activities there are.
            # and make a list 'course and activity' containing name of course and the activity
            if int(courses.hoorcollege(course)) > 0:
                   course_and_activity.append(course + " hoorcollege 1")

            if int(courses.hoorcollege(course)) > 1:
                   course_and_activity.append(course + " hoorcollege 2")

            if int(courses.hoorcollege(course)) > 2:
                   course_and_activity.append(course + " hoorcollege 3")

            if int(courses.hoorcollege(course)) > 3:
                   course_and_activity.append(course + " hoorcollege 4")


            if float(courses.werkcolleges(course)) > 0:
                   course_and_activity.append(course + " werkgroep 1")

            if int(courses.werkcolleges(course)) > 1:
                   course_and_activity.append(course + " werkgroep 2")

            if int(courses.werkcolleges(course)) > 2:
                   course_and_activity.append(course + " werkgroep 3")

            if int(courses.werkcolleges(course)) > 3:
                   course_and_activity.append(course + " werkgroep 4")


            if int(courses.practica(course)) > 0:
                   course_and_activity.append(course + " practica 1")

            if int(courses.practica(course)) > 1:
                   course_and_activity.append(course + " practica 2")

            if int(courses.practica(course)) > 2:
                   course_and_activity.append(course + " practica 3")

            if int(courses.practica(course)) > 3:
                   course_and_activity.append(course + " practica 4")

        # our schedule exists of 140 timeslots to fill, we have 128 activities.
        # filled in 12 "" strings to create empty timeslots in schedule
        for x in range(12):
            course_and_activity.append('')

        return course_and_activity, classroom_name
#hoofd_main()
