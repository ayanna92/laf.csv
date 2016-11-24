class Students(object):
    """
    Object that will contain student number, student courses
    and number of courses.
    """

    def __init__(self, stud_num, stud_vak):
        """
        Initialize student and corresponding courses
        """
        self.stud_num = stud_num
        self.stud_vak = stud_vak

    def vakNumber(self):
        """
        Number of courses per student returned
        """
        return len(self.stud_vak)

        
