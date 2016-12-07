import math
import time
from Schedule_room_test import *

from Tkinter import *

class Visualization:

    def __init__(self, room):

        # initialize drawing surface
        self.master = Tk()
        self.w = Canvas(self.master, width = 1000, height = 600)
        self.w.pack()
        self.days = 1000
        self.hours = 600
        self.room = room
        self.master.wm_title(self.room)
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

        courses2 = []
        for key, value in zaalrooster.items():
            if key == self.room:
                value = value #str(value).strip('[]')
                #print 'hello', ''.join(map(str, value))
                for courses in value:
                    #print "hi", courses
                    #courses2.append(courses)
                    for course in courses:
                        course = str(course)
                        print "what", course
                        courses2.append(course)
        print courses2

        for i in range(5):
            for j in range(5):
                self.w.create_text(100 + i, 150 + j, text = courses2[i], width = 80)
                self.w.create_text(100 + i, 250 + j, text = courses2[i+1], width = 80)
                self.w.create_text(100 + i, 350 + j, text = courses2[i+2], width = 80)
                self.w.create_text(100 + i, 450 + j, text = courses2[i+3], width = 80)
                self.w.create_text(300 + i, 150 + j, text = courses2[i+4], width = 80)
                self.w.create_text(300 + i, 250 + j, text = courses2[i+5], width = 80)
                self.w.create_text(300 + i, 350 + j, text = courses2[i+6], width = 80)
                self.w.create_text(300 + i, 450 + j, text = courses2[i+7], width = 80)
                self.w.create_text(500 + i, 150 + j, text = courses2[i+8], width = 80)
                self.w.create_text(500 + i, 250 + j, text = courses2[i+9], width = 80)
                self.w.create_text(500 + i, 350 + j, text = courses2[i+10], width = 80)
                self.w.create_text(500 + i, 450 + j, text = courses2[i+11], width = 80)
                self.w.create_text(700 + i, 150 + j, text = courses2[i+12], width = 80)
                self.w.create_text(700 + i, 250 + j, text = courses2[i+13], width = 80)
                self.w.create_text(700 + i, 350 + j, text = courses2[i+14], width = 80)
                self.w.create_text(700 + i, 450 + j, text = courses2[i+15], width = 80)
                self.w.create_text(900 + i, 150 + j, text = courses2[i+16], width = 80)
                self.w.create_text(900 + i, 250 + j, text = courses2[i+17], width = 80)
                self.w.create_text(900 + i, 350 + j, text = courses2[i+18], width = 80)
                self.w.create_text(900 + i, 450 + j, text = courses2[i+19], width = 80)


                mainloop()

"""
unhash the below to see class schedule for that room
"""
#Visualization('A1.04').fillSchedule()
#Visualization('A1.06').fillSchedule()
#Visualization('A1.08').fillSchedule()
#Visualization('A1.10').fillSchedule()
#Visualization('B0.201').fillSchedule()
#Visualization('C0.110').fillSchedule()
#Visualization('C1.112').fillSchedule()
