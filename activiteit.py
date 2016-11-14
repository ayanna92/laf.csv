

# Classe activiteit

import class_students
import class_vakken

class activiteit (object):
    """
    object that wil contain how many hoorcollege, werkcolleges and practica
    are needed for each course.
    """
    def __init__(self, stud_vak):
        self.stud_vak = stud_vak
        self.stud_num = stud_num
        self.name_and_activity = name_and_activity


    def hoorcollege():
        """
        returns how many hoorcollege the course has
        Dit staat in het vakken csv
        """

    def werkcolleges():
        """
        returns how many werkcollege the course has
        Er is nooit meer dan 1 werkgroep
        Hier moet rekening gehouden met hoeveel studenten er zijn en daaruit moeten dus het aantal colleges gehaald worden.
        """

    def practica():
        """
        returns how many practica the course has ER is ook altijd maar 1 practica per week
        Hier moet rekening gehouden met hoeveel studenten er zijn en daaruit moeten dus het aantal pracica gehaald worden.
        """

################
# make courses and calculate their capacity

import csv
fil_2 = open('vakken2.csv')
file_vakken = csv.reader(fil_2)
file_1 = open('studentenenvakken.csv')
student_vakken = csv.reader(file_1)

from collections import defaultdict, Counter
data = defaultdict(list)

student_vakken.next() #skip header

vak1 = [row[3] for row in student_vakken]
vak2 = [row[4] for row in student_vakken]
vak3 = [row[5] for row in student_vakken]
vak4 = [row[6] for row in student_vakken]
vak5 = [row[7] for row in student_vakken]

print vak1

print stud_vak
from collections import defaultdict, Counter
for (k,v) in Counter(stud_vak).dataitems():
    print "%s appears %d studenten" % (k, v)









#courses = []
#courses_list = []
#data = defaultdict(list)

# read csv file in variable courses
#for rows in file_vakken:
    #courses.append(rows)

# put al the courses names in variable names
#for col in courses[0:]:
#    name = col[0]
    # for name in data.items()
#        number_of_students = count(name)
#    print name
#    print number_of_students


# combine names and activit


# een forloop maken waarbij een tabel wordt gemaakt met daarin de benodigde informatie
# voor elke vak in vakken.csv:
#   schrijf de naam
#   check hoeveel keer de naam voorkomt in studenten.csv
#   Maak een nieuwe tabel aan waar deze waardes in staan.
#for x in range (0 , len(file_vakken)):
    #name = file_vakken[x]
    #number_of_students = student_vakken.count(name)
