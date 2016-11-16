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
