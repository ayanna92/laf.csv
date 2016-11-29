
from class_students import *
from class_courses import *
from class_rooms import *

def main():

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


        #check
        #print stud_vak

        # add student object to list
        stud = Students(stud_num, stud_vak)
        stud_list.append(stud)

        # courses of students for loop
        for vakken in stud_vak:
            exist_vak = False

            # check if vakken exists already
            for vak in vak_list:

                # if vak name and vakken are the same, add student number to existing
                # vak with append
                if vak.name_course == vakken:
                    #print vak.name_course
                    vak.students.append(stud_num)
                    #print vak.students
                    # vak.students is nu een lijst waar elke studenten nummer gelinkt is aan elk vak
                    # dat ze volgen
                    exist_vak = True


            # if vakken doesn't exist yet, create a new course and add student
            # number
            if exist_vak == False:
                if vakken != '':
                    students = []
                    course = Courses(vakken, students)
                    vak_list.append(course)
                    #print vak_list
                    course.students.append(stud_num)
            #print course.students

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




    # add new list for type of activity
    courses = []
    courses_list = []

    # read csv file in variable courses
    for row in file_vakken:
        courses.append(row)

        # put al the courses names in variable names
    for col in courses[0:]:
        name = col[0]

        # combine the names and the activities of the courses
        if col[1] != '0':
            course_activity= ': hoorcollege '

        if col[2] == '1':
            course_activity += 'werkgroep '

        if col[4] == '1':
            course_activity += 'practicum'

        # add new line to make it readable
        course_activity + '\n'

        # combine names and activities
        name_and_activity = name + course_activity
        course_activity = ""

        print name_and_activity

        # add course object to list
        cours = Courses(name, name_and_activity)
        courses_list.append(cours)

        A104 = Classrooms('A1.04', 41)

        A104.roomCapacity()

        for row in courses_and_students:
            cours_student.append(row)


        for col in courses[0:]:
            course = col[0]


            for students in cours_student:
                if students[0] == course:
                    student_list_courses = students[1:]
                    courses = Courses(course, student_list_courses)


            import csv
            resultFile = open("course_and_activity.csv",'wb')
            wr = csv.writer(resultFile, dialect='excel')

            if courses.hoorcollege(course) > 0:
                   course_and_activity.append(courses.name_course + " hoorcollege 1")
                   wr.writerow(course_and_activity)

            if courses.hoorcollege(course) > 1:
                   course_and_activity.append(course + " hoorcollege 2")
                   wr.writerow(course_and_activity)

            if courses.hoorcollege(course) > 2:
                   course_and_activity.append(course + " hoorcollege 3")
                   wr.writerow(course_and_activity)

            if courses.hoorcollege(course) > 3:
                   course_and_activity.append(course + " hoorcollege 4")
                   wr.writerow(course_and_activity)

            if courses.werkcolleges(course) > 0:
                   course_and_activity.append(course + " Werkgroep 1")
                   wr.writerow(course_and_activity)

            if courses.werkcolleges(course) > 1:
                   course_and_activity.append(course + " werkgroep 2")
                   wr.writerow(course_and_activity)

            if courses.werkcolleges(course) > 2:
                   course_and_activity.append(course + " werkgroep 3")
                   wr.writerow(course_and_activity)

            if courses.werkcolleges(course) > 3:
                   course_and_activity.append(course + " werkgroep 4")
                   wr.writerow(course_and_activity)

            if courses.practica(course) > 0:
                   course_and_activity.append(course + " practica 1")
                   wr.writerow(course_and_activity)

            if courses.practica(course) > 1:
                   course_and_activity.append(course + " practica 2")

            if courses.practica(course) > 2:
                   course_and_activity.append(course + " practica 3")
                   wr.writerow(course_and_activity)

            if courses.practica(course) > 3:
                   course_and_activity.append(course + " practica 4")
                   wr.writerow(course_and_activity)




            #print course


        return [stud_list, vak_list, classroom_list]

main()
