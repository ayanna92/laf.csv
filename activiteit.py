

<<<<<<< Updated upstream
# Classe activiteit
=======
# het berekenen van het aantal hoorcolleges, werkcolleges en practica per vak.
# door het gebruik van studenten.py het berekenen van de capaciteit van elk college
import class_students
import class_vakken
>>>>>>> Stashed changes

import class_students

class activiteit (object):
    """
    object that wil contain how many hoorcollege, werkcolleges and practica
    are needed for each course.
    """
    def __init__(self, stud_vak, stud_num, name_and_activity):
        self.stud_vak = stud_vak
        self.stud_num = stud_num
        self.name_and_activity = name_and_activity # moet dit niet alleen activity zijn?

    def studNumber(self):
        """
        return the number of students
        """
        return len(self.stud_num) # aantal studenten per activiteit leek me ook handig

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

courses = []
courses_list = []

# read csv file in variable courses
for rows in file_vakken:
    courses.append(rows)

# put al the courses names in variable names
for col in courses[0:]:
    name = col[0]
    print name
    number_of_students = student_vakken.count(name)
    print number_of_students


# combine names and activit





print student_vakken
# een forloop maken waarbij een tabel wordt gemaakt met daarin de benodigde informatie
# voor elke vak in vakken.csv:
#   schrijf de naam
#   check hoeveel keer de naam voorkomt in studenten.csv
#   Maak een nieuwe tabel aan waar deze waardes in staan.
#for x in range (0 , len(file_vakken)):
    #name = file_vakken[x]
    #number_of_students = student_vakken.count(name)
