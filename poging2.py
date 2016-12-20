# try out
import numpy as np
import matplotlib.pyplot as plt

from scoringsfunctie import *
from random_algorithm import *
from main import *
from matplotlib.pyplot import plot, title, xlabel, ylabel, savefig, legend

import copy
import random

# at this moment we start with a random schedule

def hilclimbing():
    lijst_scores = []
    schedule, courses = main()
    amount_of_hiscores = 0

    # sla het allereerste aantal punten van het rooster op.
    starting_score = scoringsfunctie(schedule,courses)
    # starting schedule is het rooster die we kunnen aanpassen.
    starting_schedule = copy.deepcopy(schedule)
    scoring_schedule = scoringsfunctie(starting_schedule, courses)

    lists = hoofd_main()
    course_and_activity = lists[0]
    course_loop = []
    keep_track_new_course = ()

    for row in course_and_activity:
        #lijst met alle activiteitem
        course_loop.append(row)

        classroom_name = lists[1]
        # volgens mij hoeft dit nu niet persee
        random.shuffle(classroom_name)

        #print "starting schedule", starting_schedule
        # alle scores zijn sowieso hoger dan -2000
        high_score = -20000
        previsous_score = scoring_schedule

        # waarom dit precies?
        if int(high_score) < int(scoring_schedule):
            high_score = scoring_schedule

            day = 0
            hour = 0
            #print schedule
            for key, week in list(starting_schedule.items()):
                print key
                for days in week:
                    #print days
                    for hours in days:
                        #print hours
                        for row in course_and_activity:
                            course = row

                            if course != "":
                                # remember current course in schedule
                                current_course = starting_schedule[key][day][hour]
                                new_schedule = copy.deepcopy(starting_schedule)
                                keep_track_new_course = current_course
                                index_zero = 0
                                index_second = 0
                                for zaal,week in new_schedule.items():
                                    for dag in week:
                                        for uur in dag:
                                            if course == uur:
                                                new_schedule[zaal][index_zero][index_second] = current_course
                                            else:
                                                index_second = index_second + 1
                                        index_second = 0
                                        index_zero = index_zero + 1
                                    index_second = 0
                                    index_zero = 0
                                new_schedule[key][day][hour] = course
                                scoring_schedule_new = scoringsfunctie(new_schedule, courses)

                                if high_score < scoring_schedule_new:
                                    high_score = scoring_schedule_new
                                    keep_track_new_course = course
                                    starting_schedule = new_schedule
                                    amount_of_hiscores = 0
                                    lijst_scores.append(high_score)
                                else:
                                    keep_track_new_course = current_course
                                    lijst_scores.append(high_score)
                                    amount_of_hiscores += 1
                                    #print amount_of_hiscores
                                    if amount_of_hiscores == 1000:
                                        #x = np.arange(0,len(lijst_scores),1)
                                        #plt.scatter(x, lijst_scores)
                                        #plt.plot(x,lijst_scores)
                                        #xlabel('Trials')
                                        #ylabel('Score')
                                        #plt.savefig("hillclimbing2")

                                        return starting_score, high_score, starting_schedule

                        hour = hour + 1
                        course_and_activity.remove(keep_track_new_course)
                    hour = 0
                    day = day + 1
                hour = 0
                day = 0

    #x = np.arange(0,len(lijst_scores),1)

    #plt.scatter(x, lijst_scores)

    #xlabel('Trials')
    #ylabel('Score')
    #plt.plot(x, lijst_scores)
    #plt.savefig("hillclimbing2")

    return starting_score, high_score, starting_schedule

print hilclimbing()
