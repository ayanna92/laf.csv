

# Classe activiteit

import class_students
import class_vakken
import math
from collections import Counter
import csv

# open and read csv files
open_1 = open('studentenenvakken.csv')
file_1 = csv.reader(open_1)

fil_2 = open('vakken2.csv')
file_vakken = csv.reader(fil_2)
#skip header
file_1.next()

# make list for how many students are taking each course
vak = []

for row in file_1:
    vak.append(row[3])
    vak.append(row[4])
    vak.append(row[5])
    vak.append(row[6])
    vak.append(row[7])

# example
name_course = "Calculus 2"
number_of_students = vak.count(name_course)
#print vak
#print len(vak)
#print Counter(vak)
#for row in file_vakken:
#    if name_course in row and row[2] != 0:
#        capacity = float(row[3])

#print number_of_students
#print capacity
#print math.ceil(number_of_students / capacity)


class activiteit (object):
    """
    object that wil contain how many hoorcollege, werkcolleges and practica
    are needed for each course.
    """
    def __init__(self, name_course):
        self.name_course = name_course
        self.stud_num = stud_num
        self.name_and_activity = name_and_activity
        self.number_of_students = vak.count(name_course)

    def hoorcollege(name_course):
        """
        returns how many hoorcollege the course has
        Dit staat in het vakken csv
        """

        for row in file_vakken:
            if name_course in row:
                return row[1]

    def werkcolleges(number_of_students, name_course):
        """
        returns how many werkcollege the course has
        Er is nooit meer dan 1 werkgroep
        Hier moet rekening gehouden met hoeveel studenten er zijn en daaruit moeten dus het aantal colleges gehaald worden.
        """"
        for row in file_vakken:
            if name_course in row and row[2] != 0:
                capacity = float(row[3])

        #print number_of_students
        #print capacity
        return math.ceil(number_of_students / capacity)  # klopt nog niet helemaal want geeft nog een verkeerd afgerond getal terug.


    def practica():
        """

        returns how many practica the course has ER is ook altijd maar 1 practica per week
        Hier moet rekening gehouden met hoeveel studenten er zijn en daaruit moeten dus het aantal pracica gehaald worden.
        """

        for row in file_vakken:
            if name_course in row and row[5] != 0:
                capacity = float(row[6])

        #print number_of_students
        #print capacity
        return math.ceil(number_of_students / capacity)


################
# make courses and calculate their capacity







"""



#from collections import defaultdict, Counter
#for (k,v) in Counter(stud_vak).dataitems():
#    print "%s appears %d studenten" % (k, v)
"""
