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

class Courses(object):
    """
    Object that will contain course name and course name and activities
    """

    def __init__(self, name, students):
        """
        Initialize student and corresponding courses
        """

        self.name = name
        self.students = students
        #self.name_and_activity = name_and_activity

    def studNumber(self):
        """
        return the number of students
        """
        return len(self.students)


def main():
##########################
    import csv
    # open and read csv files
    open_1 = open('studentenenvakken.csv')
    file_1 = csv.reader(open_1)

    # make empty list for student information, and list which will contain info
    stud_info = []
    stud_list = []
    vak_list = []

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
                if vak.name == vakken:
                    print vak.name
                    vak.students.append(stud_num)
                    print vak.students
                    # als je vak.name en vak.student samen print zie je dat iedere
                    # keer als een nieuwe student wordt gevonden met een vak
                    # deze wordt bijgevoegd
                    exist_vak = True

            # if vakken doesn't exist yet, create a new course and add student
            # number
            if exist_vak == False:
                if vakken != '':
                    students = []
                    course = Courses(vakken, students)
                    vak_list.append(course)
                    course.students.append(stud_num)
                    #print course.students

    return [stud_list, vak_list]

main()
