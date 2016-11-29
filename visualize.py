import math
import time
import 

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

    def fillSchedule(self, course_and_activity):


    def done(self):
        mainloop()

Visualization().done()
