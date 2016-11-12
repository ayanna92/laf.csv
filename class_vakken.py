# class for courses
# Lectures & roosters
#
# Ayanna, Lois, Femke
#

class Courses(object):
    """
    Object that will contain course name and course name and activities
    """

    def __init__(self, name, name_and_activity):
        """
        Initialize student and corresponding courses
        """

        self.name = name
        self.name_and_activity = name_and_activity


import csv
fil_2 = open('vakken2.csv')
file_vakken = csv.reader(fil_2)

courses = []
courses_list = []

# read csv file in variable courses
for rows in file_vakken:
    courses.append(rows)

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

    #print name_and_activity

    # add course object to list
    cours = Courses(name, name_and_activity)
    courses_list.append(cours)
