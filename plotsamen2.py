from scoringsfunctie import *
from random_algorithm import *
import numpy as np
from numpy import array
import matplotlib.pyplot as plt
from simulated_annealing import *
from main import *
from visualize import *
import copy
import random
import math


hillclimbing_max = [2686, 2562, 2510, 2586, 2543, 2412, 2628, 2591, 2582,  2633, 2614.0,  2510, 2510, 2533, 2460, 2521, 2548, 2592, 2548, 2418.0, 2500, 2574, 2531, 2585, 2477, 2590, 2554, 2598.0, 2426, 2458, 2622, 2566.0, 2477.0, 2614, 2568, 2584, 2631.0, 2520, 2556, 2571, 2562.0, 2685, 2636, 2636, 2653, 2611, 2477]
hillclimbing_min = [-402.0, -848.0, -722.0, -474.0, -837.0, -265.0, -372.0, -585.0, -271.0, -734.0, -497.0, -407.0, -986.0, -744.0, -604.0, -628.0, -727.0, -992.0, -1041.0, -761.0, -519.0, -708.0, -479.0, -437.0, -514.0, -514.0, -740.0, -357.0, -697.0, -958.0, -620.0, -636.0, -627.0, -756.0, -715.0, -660.0, -701.0, -460.0, -670.0, -533.0, -324.0, -677.0, -608.0, -633.0, -491.0, -671.0, -623.0, -558.0, -737.0, -516.0, -192.0]
print len(hillclimbing_max)

plt.hist(hillclimbing_max)



############################################################
simulated_annealing
samendit = [(-767.0, 2528), (-1007.0, 2509.0), (-728.0, 2495.0), (-565.0, 2456), (-619.0, 2540), (-814.0, 2417.0), (-785.0, 2499), (-596.0, 2414.0), (-465.0, 2538.0), (-671.0, 2494)]

sim_min = [-767.0, -1007.0, -728.0, -565.0, -619.0, -814.0, -785.0, -596.0, -465.0, -671.0]
sim_max =  [2528, 2509.0, 2495.0, 2456, 2540, 2417.0, 2499, 2414.0, 2538.0, 2494]

simmulatedlijst = [(-777.0, 2559), (-583.0, 2521), (-764.0, 2539.0), (-865.0, 2497.0), (-376.0, 2529.0), (-813.0, 2530), (-437.0, 2595), (-682.0, 2571.0), (-711.0, 2496), (-788.0, 2598)]

for temp in (simmulatedlijst):
    sim_min.append(temp[0])
    sim_max.append(temp[1])

print len(sim_max)

plt.hist(sim_max)


plt.legend(['Hillclimbing', 'Simulated Annealing'], loc='upper left')
plt.subplots_adjust(bottom=0.15)
plt.savefig("Comparison simulated annealing vs hillclimbing 2 ")
plt.show()
