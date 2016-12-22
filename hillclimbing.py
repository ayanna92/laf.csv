# Ayanna, Femke en Lois
#
# heuristics
# Hilclimbing algorithm
#
# this file contains the hillclimbing 2.0 algorithm. A random schedule is made
# and changed to a better schedule.
# in hillclimbing plot the hillclimbing algorithm is done 50 times and a plot is made.
#
#
import numpy as np
import matplotlib.pyplot as plt

from scoringsfunctie import *
from random_algorithm import *
from main import *
from numpy import array

import copy
import random


def hilclimbing():
    lijst_scores = []

    # save the first schedule and there scores
    schedule, courses = main()
    starting_score = scoringsfunctie(schedule,courses)



    starting_schedule = copy.deepcopy(schedule)
    scoring_schedule = scoringsfunctie(starting_schedule, courses)

    lists = hoofd_main()
    course_and_activity = lists[0]
    course_loop = []
    keep_track_new_course = ()

    for row in course_and_activity:
        # list with al acticities
        course_loop.append(row)

        classroom_name = lists[1]
        random.shuffle(classroom_name)

        # set a highscore so the if statement can start.
        high_score = -20000
        previsous_score = scoring_schedule

        # dit kan misschien weg.
        if int(high_score) < int(scoring_schedule):
            high_score = scoring_schedule

            day = 0
            hour = 0


            # for each timeslot swap courses and calculate the score.
            for key, week in list(starting_schedule.items()):
                for days in week:
                    for hours in days:
                        for row in course_and_activity:
                            course = row

                            if course != "":

                                # remember current course in schedule
                                current_course = starting_schedule[key][day][hour]
                                new_schedule = copy.deepcopy(starting_schedule)
                                keep_track_new_course = current_course
                                index_zero = 0
                                index_second = 0

                                # find the other course in schedule and switch the courses
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

                                # check if new schedule is better
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


                        hour = hour + 1
                        if keep_track_new_course in course_and_activity:
                            course_and_activity.remove(keep_track_new_course)
                    hour = 0
                    day = day + 1
                hour = 0
                day = 0

    # For making a scatterplot of the highscore:
    #x = np.arange(0,len(lijst_scores),1)
    #plt.scatter(x, lijst_scores)
    #plt.xlabel('Iterations')
    #plt.ylabel('Score')
    #plt.plot(x, lijst_scores)
    #plt.savefig("hillclimbing2")


    return starting_score, high_score, starting_schedule

print hilclimbing()

# function to take 50 random schedule and find the best schedule.

def hilclimbing_plot():

    lijst_rooster_maxscore = []
    lijst_rooster_minscore = []
    zaalrooster_beste = {}
    score_Best_overal = 0

    # 50 times
    for i in range(0,50):

        starting_score, high_score, starting_schedule = hilclimbing()

        if score_Best_overal < high_score:
            zaalrooster_beste = starting_schedule
            score_Best_overal = high_score

        lijst_rooster_minscore.append(starting_score)
        lijst_rooster_maxscore.append(high_score)

    days = array([1, 2])

    samen = zip(lijst_rooster_minscore, lijst_rooster_maxscore)

    for temp in (samen):
        plt.plot(days, (temp),'-ro' )

    plt.xlabel('Before and After')
    plt.ylabel('Score')
    plt.title('Comparison before and after hillclimbing algorithm')
    labels = ['before', 'after']
    plt.xticks(lijst_rooster_minscore, labels, rotation='vertical')

    # Pad margins so that markers don't get clipped by the axes
    plt.margins(0.2)

    # Tweak spacing to prevent clipping of tick-labels
    plt.subplots_adjust(bottom=0.15)
    plt.savefig("verschillende roosters")
    plt.show()

    return score_Best_overal, tuplescores,  zaalrooster_beste,

print hilclimbing_plot
