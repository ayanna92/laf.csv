# class for classrooms
# Lectures & roosters
#
# Ayanna, Lois, Femke
#

class Classrooms(object):
    """
    Object that will contain the classrooms and their capacity
    """

    def __init__(self, room, capacity):
        """
        Initialize classroom number and capacity of the classroom
        """

        self.room = room
        self.capacity = capacity
        self.tijdsloten = {'9.00': '', '11.00': '', '13.00': '', '15.00': '', '17.00': ''}

        # example of filling in the timeslots
        # tijdsloten['9.00'] = activiteit


###################################

import csv

fil = open('classrooms.csv')
file_zalen = csv.reader(fil)

zalen = []
classroom_list = []


# put csv file in variable zalen
for rows in file_zalen:
    zalen.append(rows)

# put al the room numbers in room
for col in zalen[1:]:
    room = col[0]
    capacity = col[1]

    # add classroom object to list
    classroom = Classrooms(room, capacity)
    classroom_list.append(classroom)
