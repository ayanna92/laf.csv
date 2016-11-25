
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

        for row in file_vakken:
            if name_course in row:
                return row[1]

    def werkcolleges(self, name_course):
        """
        returns how many werkcollege the course has
        Er is nooit meer dan 1 werkgroep
        Hier moet rekening gehouden met hoeveel studenten er zijn en daaruit moeten dus het aantal colleges gehaald worden.
        """
        for row in file_vakken:
            if name_course in row and row[2] != 0:
                capacity = float(row[3])
        return math.ceil(len(self.students)/ capacity)  # klopt nog niet helemaal want geeft nog een verkeerd afgerond getal terug.


    def practica(self, name_course):
        """

        returns how many practica the course has ER is ook altijd maar 1 practica per week
        Hier moet rekening gehouden met hoeveel studenten er zijn en daaruit moeten dus het aantal pracica gehaald worden.
        """

        for row in file_vakken:
            if name_course in row and row[5] != 0:
                capacity = float(row[6])
        return math.ceil(len(self.students) / capacity)
