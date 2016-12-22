
from scoringsfunctie import *
from random_algorithm import *
import numpy as np
import matplotlib.pyplot as plt
from simulated_annealing import *
from main import *
from visualize import *
import copy
import random
import math


def simmulated_algoritme():


    lijst_rooster_maxscore = []
    lijst_rooster_minscore = []
    zaalrooster_beste = {}
    print "laten we starten"
    score_Best_overal = 0
    for i in range(0,30):
        schedule, courses = main()
        lists = hoofd_main()
        course_and_activity = lists[0]
        classroom_name = lists[1]
        print i

        starting_schedule, high_score, starting_score = simulated_annealing(schedule, courses, classroom_name)

        lijst_rooster_minscore.append(starting_score)
        lijst_rooster_maxscore.append(high_score)


        if score_Best_overal < high_score:
            zaalrooster_beste = starting_schedule
            score_Best_overal = high_score
        if i == 25:
            print "min", lijst_rooster_minscore
            print "max", lijst_rooster_maxscore
        if i == 50:
            print "min", lijst_rooster_minscore
            print "max", lijst_rooster_maxscore
            #print "hij is beter"]


    from matplotlib.pyplot import plot, title, xlabel, ylabel, savefig, legend
    from numpy import array

    days = array([1, 2])

    samen = zip(lijst_rooster_minscore, lijst_rooster_maxscore)

    print samen
    for temp in (samen):
        plt.plot(days, (temp),'-ro' )
    plt.title('Comparison before and after simulated annealing')
    plt.xlabel('Before and After')
    plt.ylabel('Score')

    #x = lijst_rooster_minscore
    #y = lijst_rooster_maxscore
    labels = ['before', 'after']
    plt.xticks(lijst_rooster_minscore, labels, rotation='vertical')
    # Pad margins so that markers don't get clipped by the axes
    plt.margins(0.2)
    # Tweak spacing to prevent clipping of tick-labels
    plt.subplots_adjust(bottom=0.15)
    plt.savefig("different roosters simulated")
    plt.show()

    return score_Best_overal, lijst_rooster_minscore, lijst_rooster_maxscore,  zaalrooster_beste,

print simmulated_algoritme()
