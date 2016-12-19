import numpy as np
import matplotlib.pyplot as plt

from scoringsfunctie import *
from Schedule_room import *
from main import *

import copy
import random
import math

# at this moment we start with a random schedule
schedule, courses = main()
starting_schedule = copy.deepcopy(schedule)
scoring_schedule = scoringsfunctie(starting_schedule, courses)
lists = hoofd_main()
course_and_activity = lists[0]
classroom_name = lists[1]



def simulated_annealing(starting_schedule, courses, classroom_name):

    # set initial temp
    temp = 1000
    cooling_rate = 0.003

    high_score = scoringsfunctie(starting_schedule, courses)
    SA = True
    steps = 0

    while True:

        while True:

            steps = steps + 1

            # choose two random timeslots, swap the courses
            random_room_a = classroom_name[random.randint(0,6)]
            random_room_b = classroom_name[random.randint(0,6)]

            random_day_a = random.randint(0,4)
            random_day_b = random.randint(0,4)

            random_hour_a = random.randint(0,3)
            random_hour_b = random.randint(0,3)

            course_a = starting_schedule[random_room_a][random_day_a][random_hour_a]
            course_b = starting_schedule[random_room_b][random_day_b][random_hour_b]
            new_schedule = copy.deepcopy(starting_schedule)
            new_schedule[random_room_a][random_day_a][random_hour_a] = course_b
            new_schedule[random_room_b][random_day_b][random_hour_b] = course_a

            # if score is higher than highscore, keep swap
            # if acceptance higher than random.random, keep swap
            # else: swap back
            new_score = scoringsfunctie(new_schedule, courses)
            acceptance = math.exp((new_score - high_score) / temp)

            if SA:

                temp *= 1 - cooling_rate

                if acceptance > random.random():
                    high_score = new_score
                    starting_schedule = new_schedule
                    break
            else:
                if new_score > high_score:
                    high_score = new_score
                    starting_schedule = new_schedule
                    break
                else:
                    new_score = scoringsfunctie(starting_schedule, courses)

                if steps > 5000:
                    print (schedule)
                    print high_score
                    return [starting_schedule, high_score]
            if temp < 1:
                SA = False
            print (steps)
            print (starting_schedule)
            print(high_score)

#running the simulated annealing:
#simulated_annealing(starting_schedule, courses, classroom_name)
