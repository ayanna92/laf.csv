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
        self.timeslot = [[]]
        self.days = [1, 2, 3, 4, 5]
        self.hours = [1, 2, 3, 4]

    # zaal.roomCapacity() gives capacity of room
    def roomCapacity(self):

        return self.capacity

    def emptyTimeSlot(self, )

    def fillTimeslot(self):

        for day in self.days:
            for hour in self.hours:
                self.timeslot[day[hour]] = self.days[day] + self.hours[hour]

        return timeslot

A104 = Classrooms("A1.04", 41)

print A104.fillTimeslot()
