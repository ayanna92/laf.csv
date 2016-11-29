
# Classe activiteit
class Courses (object):
    """
    object that wil contain how many hoorcollege, werkcolleges and practica
    are needed for each course.
    """

    def __init__(self, name_course, students):
        self.name_course = name_course
        self.students = students

    def studNumber(self):
        """
        returns number of students for each course
        """
        return len(self.students)

    def hoorcollege(self, name_course):
        """
        returns how many hoorcollege the course has
        Dit staat in het vakken csv
        """

        import csv

        # Moest ik er bij zetten omdat anders die bij mij niet laade, haal ik hierna weer weg!!
        fil_2 = open('vakken2.csv')
        file_vakken = csv.reader(fil_2)

        for row in file_vakken:
            if name_course == row[0]:
                return row[1]


    def werkcolleges(self, name_course):
        """
        returns how many werkcollege the course has
        Er is nooit meer dan 1 werkgroep
        Hier moet rekening gehouden met hoeveel studenten er zijn en daaruit moeten dus het aantal colleges gehaald worden.
        """
        import csv
        import math

        # Moest ik er bij zetten omdat anders die bij mij niet laade, haal ik hierna weer weg!!
        fil_2 = open('vakken2.csv')
        file_vakken = csv.reader(fil_2)

        for row in file_vakken:
            if name_course == row[0] and row[2] != "0":
                return math.ceil(len(self.students)/ float(row[3]))

        return 0


    def practica(self, name_course):
        """

        returns how many practica the course has ER is ook altijd maar 1 practica per week
        Hier moet rekening gehouden met hoeveel studenten er zijn en daaruit moeten dus het aantal pracica gehaald worden.
        """
        import csv
        import math

        # Moest ik er bij zetten omdat anders die bij mij niet laade, haal ik hierna weer weg!!
        fil_2 = open('vakken2.csv')
        file_vakken = csv.reader(fil_2)
        for row in file_vakken:
            if name_course == row[0] and row[4] != "0":
                number_of_werkcolleges = math.ceil(len(self.students) / float(row[5]))
        return 0
