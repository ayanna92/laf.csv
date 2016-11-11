class students(object):
    """
    Object that will contain student number, student courses
    and number of courses.
    """

    def __init__(self, stud_num, stud_vak):

        self.stud_num = stud_num
        self.stud_vak = stud_vak

    def vakNumber(self):

        return len(self.stud_vak)

##########################
import csv
# open and read csv files
open_1 = open('studentenenvakken.csv')
file_1 = csv.reader(open_1)

# make empty list for student information, and list which will contain info
stud_info = []
stud_list = []

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
    print stud_vak

      # add student object to list
    student = students(stud_num, stud_vak)
    stud_list.append(student)

#check
print stud_info
