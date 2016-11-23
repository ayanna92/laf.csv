# class for schedule
# Lectures & roosters
#
# ayanna, lois, Femke
#

from class_courses import *
from class_rooms import *


class schedule(object):

    def __init__(self):

        self.days = ['ma', 'di', 'wo', 'do', 'vr']
        self.timeblocks = 4
        self.schedule = {}

    def empty_timeblock(self, tijdsloten):

        timeblock_empty = False

        if tijdsloten != '':
            timeblock_empty = True

        return timeblock_empty

    def
