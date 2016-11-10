# Main file classes
# Lectures & roosters
#
# Ayanna, Lois, Femke
#

import math
import random
import pylab
import studentenvakken.csv

# === Provide classes
class rooster(object):
    """
    representeert een rooster voor een week
    """

    def __init__(self):

        self.days = 5
        self.timeblocks = 4
        self.rooster = []

    def fillIn (self, timeslots):

        if (timeslots) not in self.rooster:
            self.rooster.append(timeslots)

    def isAvailable(self, days, timeblocks):

        if timeslots not in rooster:
            return True
