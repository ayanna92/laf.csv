import math
import time
from Schedule_room_test import *

from Tkinter import *

class Visualization:

    def __init__(self):

        # initialize drawing surface
        self.master = Tk()
        self.w = Canvas(self.master, width = 1000, height = 600)
        self.w.pack()
        self.days = 1000
        self.hours = 600
        self.master.update()

        # make loop for rectangles
        self.times = {}
        for i in range(0, self.days, 200):
            for j in range(0, self.hours, 100):
                x1 = i
                y1 = j
                x2 = i + 200
                y2 = j + 100
                self.times[(i, j)] = self.w.create_rectangle(x1, y1, x2, y2, fill = "white")

        self.monday = self.w.create_text((75, 50), text = "Monday", font = ("Arial", 25))
        self.tuesday = self.w.create_text((275, 50), text = "Tuesday", font = ("Arial", 25))
        self.wednesday = self.w.create_text((475, 50), text = "Wednesday", font = ("Arial", 25))
        self.thursday = self.w.create_text((675, 50), text = "Thursday", font = ("Arial", 25))
        self.friday = self.w.create_text((875, 50), text = "Friday", font = ("Arial", 25))

    def fillSchedule(self):
        self.rooster = main()

        #key = self.rooster["B0.201", "A1.05", "A1.06", "A1.08","A1.10","C0.110","C1.112"]
        #print "hello", key
        # zo print ik de vakken uit zalen
        #print self.rooster["B0.201"]
        #print self.rooster["A1.04"]

        XBASE, YBASE, DISTANCE = 200, 100, 100

        for zalen, values in zaalrooster.items():
            #print zalen, values
            for value in values:
                print "hello", value
                for i, course in enumerate(values):
                    self.w.create_text((XBASE, YBASE + i * DISTANCE), text = value)
                    #print self.w.create_text((XBASE, YBASE + i * DISTANCE), text = value)
                    #mainloop()

        #for value, key in self.rooster.iteritems():
            #if key == 'B0.201':
                #print value
        #B0201 = self.rooster['B0.201']
        #for course in B0201:
        #    self.w.create_text((XBASE, YBASE + i * DISTANCE), text = course)

        #for i, zaal in self.rooster.items:
        #    zaal = i[0]
        #    course = i[1:]
        #    self.w.create_text((XBASE, YBASE + i * DISTANCE), text = course)
            #print zaal
            #for j, course in self.rooster.iteritems():
            #    print course





Visualization().fillSchedule()
