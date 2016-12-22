
from scoringsfunctie import *
from random_algorithm import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, title, xlabel, ylabel, savefig, legend

lijst_rooster_score = []
zaalrooster_beste = {}
print "printing the plot in verschillende roosters..."
plt.ion()
def random_algoritme():
    score_beste_rooster = -20000
    for i in range(0,1000):
        rooster, courses = main()
        score_rooster = scoringsfunctie(rooster,courses)

        if score_rooster > score_beste_rooster:
            zaalrooster_beste = rooster
            score_beste_rooster = score_rooster
            #print "hij is beter"

        lijst_rooster_score.append(score_rooster)


    x = np.arange(0,len(lijst_rooster_score),1)

    #plt.scatter(x, lijst_rooster_score)
    plt.hist(lijst_rooster_score)
    xlabel('Trials')
    ylabel('Score')
    plt.show()
    plt.savefig("verschillende roosters")

    return score_beste_rooster, zaalrooster_beste

print random_algoritme()

#print score_beste_rooster
#print zaalrooster_beste

# the histogram of the data
