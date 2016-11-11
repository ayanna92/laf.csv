# class for courses
# Lectures & roosters
#
# Ayanna, Lois, Femke
#

import csv
fil_2 = open('vakken2.csv')
file_vakken = csv.reader(fil_2)

courses = []
courses_info = dict()

# read csv file in variable courses
for rows in file_vakken:
    courses.append(rows)

# put al the courses names in variable names
for col in courses[0:]:
    course_name = col[0]

# combine the names and the activities of the courses
    if col[1] != '0':
        course_activity= ': hoorcollege '

    if col[2] == '1':
        course_activity += '+ werkgroep '

    if col[4] == '1':
        course_activity += '+ practica'

    # add new line to make it readable
    course_activity + '\n'

    # combine names and activities
    name_and_activity = course_name + course_activity
    course_activity = ""

    #print name_and_activity
