
from scoringsfunctie import *
from Schedule_room import *
from poging2 import *
import numpy as np
import matplotlib.pyplot as plt


def hilclimbing_algoritme():

    lijst_rooster_maxscore = []
    lijst_rooster_minscore = []
    tuplescores = []
    zaalrooster_beste = {}
    print "laten we starten"
    score_Best_overal = 0
    for i in range(0,5):
        print i

        starting_score, high_score, starting_schedule = hilclimbing()


        if score_Best_overal < high_score:
            zaalrooster_beste = starting_schedule
            score_Best_overal = high_score

            #print "hij is beter"]
        lijst_rooster_minscore.append(starting_score)
        lijst_rooster_maxscore.append(high_score)


    from matplotlib.pyplot import plot, title, xlabel, ylabel, savefig, legend
    from numpy import array

    days = array([1, 2])

    samen = zip(lijst_rooster_minscore, lijst_rooster_maxscore)

    print samen
    for temp in (samen):
        plt.plot(days, (temp),'-ro' )
    plt.title('Comparison before and after hillclimbing algorithm')
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
    plt.savefig("verschillende roosters")
    plt.show()

    return score_Best_overal, tuplescores,  zaalrooster_beste,

print hilclimbing_algoritme()
