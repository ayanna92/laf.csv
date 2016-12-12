
from scoringsfunctie import *
from Schedule_room import *
import numpy as np
import matplotlib.pyplot as plt

lijst_rooster_score = []
zaalrooster_beste = {}


def random_algoritme():
    score_beste_rooster = -20000
    for i in range(0,2000):
        rooster, courses = main()
        score_rooster = scoringsfunctie(0,0)

        if score_rooster > score_beste_rooster:
            zaalrooster_beste = rooster
            score_beste_rooster = score_rooster
            #print "hij is beter"

        lijst_rooster_score.append(score_rooster)

    plt.hist(lijst_rooster_score)
    plt.show()
    print lijst_rooster_score
    return score_beste_rooster, zaalrooster_beste

print random_algoritme()

#print score_beste_rooster
#print zaalrooster_beste

# the histogram of the data
