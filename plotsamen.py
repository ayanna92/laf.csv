
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


hillclimbinglijst = [(-903.0, 2545), (-619.0, 2499), (-366.0, 2391), (-454.0, 2600), (-511.0, 2491), (-367.0, 2621), (-590.0, 2582.0), (-836.0, 2594), (-733.0, 2617), (-591.0, 2577)]

simmulatedlijst = [(-777.0, 2559), (-583.0, 2521), (-764.0, 2539.0), (-865.0, 2497.0), (-376.0, 2529.0), (-813.0, 2530), (-437.0, 2595), (-682.0, 2571.0), (-711.0, 2496), (-788.0, 2598)]

minimumscore = [-777.0, -583.0, -764.0, -865.0, -376.0, -813.0, -437.0, -682.0, -711.0, -788.0]

days = ([1, 2])
minimum = []
maxi = []
miniSA = []
maxiSA = []
for temp in (hillclimbinglijst):
    minimum.append(temp[0])
    maxi.append(temp[1])

    #l1 = plt.plot(days, (temp),'-ro' )
plt.hist(maxi)

for temp in (simmulatedlijst):
    miniSA.append(temp[0])
    maxiSA.append(temp[1])
    #l2 = plt.plot(days, (temp), '-bo')
    print "hoi"

plt.hist(maxiSA)

plt.title('Comparison before and after simulated annealing')
#plt.xlabel('Before and After')
#plt.ylabel('Score')

#x = lijst_rooster_minscore
#y = lijst_rooster_maxscore
#labels = ['before', 'after']
#plt.xticks(minimumscore, labels, rotation='vertical')
# Pad margins so that markers don't get clipped by the axes
plt.margins(0.2)
# Tweak spacing to prevent clipping of tick-labels
#plt.legend((l1,l2),('hillclimbing 2.0','simulated annealing'), loc = 'best')





plt.legend(['Hillclimbing', 'Simulated Annealing'], loc='upper left')
plt.subplots_adjust(bottom=0.15)
plt.savefig("Comparison simulated annealing vs hillclimbing ")
plt.show()
