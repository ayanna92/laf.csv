import numpy as np
import matplotlib.pyplot as plt
rooster =(['Before','After'])


lijst_rooster_minscore= [-886.0, -480.0, -344]
lijst_rooster_maxscore = [ -886.0,2000.0, 680]
days = ([1, 2])

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
