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
    starting_score = scoringsfunctie(schedule,courses)
<<<<<<< HEAD:hillclimbing.py
    schedule, courses = main()


    starting_schedule = copy.deepcopy(schedule)
=======
    # starting schedule is het rooster die we kunnen aanpassen.
    starting_schedule = {'B0.201': [['Zoeken sturen en bewegen practica 3', 'Technology for games werkgroep 2', 'Reflectie op de digitale cultuur werkgroep 1', 'Software engineering practica 2'], ['Webprogrammeren en databases hoorcollege 2', 'Heuristieken 2 hoorcollege 1', 'Data Mining practica 2', 'Data Mining practica 1'], ['Technology for games hoorcollege 2', 'Zoeken sturen en bewegen practica 1', 'Collectieve Intelligentie werkgroep 4', 'Bioinformatica practica 2'], ['Compilerbouw werkgroep 2', 'Data Mining hoorcollege 1', 'Bioinformatica hoorcollege 1', 'Databases 2 werkgroep 1'], ['Data Mining hoorcollege 2', 'Moderne Databases werkgroep 1', 'Algoritmen en complexiteit hoorcollege 1', 'Technology for games hoorcollege 1']], 'A1.08': [['Collectieve Intelligentie practica 1', 'Informatie- en organisatieontwerp practica 1', 'Collectieve Intelligentie practica 2', 'Informatie- en organisatieontwerp practica 2'], ['Technology for games werkgroep 1', 'Project Numerical Recipes practica 2', 'Programmeren in Java 2 practica 1', 'Project Genetic Algorithms practica 3'], ['Collectieve Intelligentie werkgroep 1', 'Reflectie op de digitale cultuur werkgroep 3', 'Moderne Databases practica 3', 'Webprogrammeren en databases practica 1'], ['Reflectie op de digitale cultuur werkgroep 2', 'Netwerken en systeembeveiliging practica 3', 'Informatie- en organisatieontwerp hoorcollege 1', 'Autonomous Agents 2 werkgroep 1'], ['Autonomous Agents 2 practica 2', 'Advanced Heuristics hoorcollege 1', 'Informatie- en organisatieontwerp werkgroep 1', 'Autonomous Agents 2 practica 3']], 'C0.110': [['Databases 2 hoorcollege 1', 'Bioinformatica hoorcollege 2', 'Algoritmen en complexiteit werkgroep 2', 'Data Mining werkgroep 1'], ['Compilerbouw hoorcollege 1', 'Zoeken sturen en bewegen practica 2', 'Collectieve Intelligentie hoorcollege 1', 'Calculus 2 hoorcollege 1'], ['Software engineering hoorcollege 1', 'Collectieve Intelligentie werkgroep 2', 'Kansrekenen 2 hoorcollege 1', 'Algoritmen en complexiteit practica 1'], ['Compilerbouw werkgroep 1', 'Collectieve Intelligentie hoorcollege 2', 'Lineaire Algebra hoorcollege 1', 'Kansrekenen 2 hoorcollege 2'], ['Compilerbouw hoorcollege 2', 'Collectieve Intelligentie hoorcollege 3', 'Webprogrammeren en databases werkgroep 1', 'Software engineering werkgroep 1']], 'A1.04': [['Machine Learning hoorcollege 1', 'Algoritmen en complexiteit werkgroep 1', 'Compilerbouw practica 2', 'Heuristieken 1 werkgroep 1'], ['Autonomous Agents 2 hoorcollege 2', 'Interactie-ontwerp hoorcollege 1', 'Project Genetic Algorithms practica 1', 'Netwerken en systeembeveiliging practica 2'], ['Netwerken en systeembeveiliging practica 4', 'Moderne Databases practica 1', 'Project Genetic Algorithms practica 2', 'Bioinformatica practica 1'], ['Webprogrammeren en databases hoorcollege 1', 'Autonomous Agents 2 werkgroep 3', 'Project Numerical Recipes practica 3', 'Databases 2 werkgroep 2'], ['Software engineering werkgroep 2', 'Webprogrammeren en databases werkgroep 2', 'Moderne Databases werkgroep 2', 'Calculus 2 werkgroep 3']], 'A1.06': [['Data Mining werkgroep 2', 'Webprogrammeren en databases practica 2', 'Data Mining werkgroep 3', 'Collectieve Intelligentie practica 3'], ['Netwerken en systeembeveiliging practica 1', 'Architectuur en computerorganisatie hoorcollege 2', 'Advanced Heuristics practica 2', 'Project Numerical Recipes practica 1'], ['Moderne Databases practica 2', 'Collectieve Intelligentie werkgroep 3', 'Programmeren in Java 2 practica 3', 'Programmeren in Java 2 practica 2'], ['', '', '', 'Autonomous Agents 2 werkgroep 2'], ['Moderne Databases werkgroep 3', 'Informatie- en organisatieontwerp werkgroep 2', 'Interactie-ontwerp hoorcollege 2', 'Architectuur en computerorganisatie hoorcollege 1']], 'C1.112': [['Software engineering practica 1', 'Reflectie op de digitale cultuur hoorcollege 2', 'Lineaire Algebra hoorcollege 2', 'Compilerbouw practica 1'], ['Advanced Heuristics practica 1', 'Bioinformatica werkgroep 3', '', 'Informatie- en organisatieontwerp hoorcollege 2'], ['', 'practicum_compilerbouw practica 1', '', 'Algoritmen en complexiteit practica 2'], ['Heuristieken 1 hoorcollege 1', 'Analysemethoden en -technieken hoorcollege 1', '', 'practicum_compilerbouw practica 2'], ['Autonomous Agents 2 practica 1', 'Heuristieken 2 werkgroep 1', 'Bioinformatica hoorcollege 3', 'Heuristieken 2 werkgroep 2']], 'A1.10': [['Heuristieken 1 werkgroep 2', 'Autonomous Agents 2 hoorcollege 1', 'Moderne Databases hoorcollege 1', 'Collectieve Intelligentie practica 4'], ['Data Mining practica 3', '', 'Bioinformatica werkgroep 1', 'Bioinformatica werkgroep 2'], ['Bioinformatica practica 3', 'Programmeren in Java 2 practica 4', 'practicum_compilerbouw practica 3', ''], ['', 'practicum_compilerbouw practica 4', 'Machine Learning hoorcollege 2', ''], ['Calculus 2 werkgroep 2', '', 'Reflectie op de digitale cultuur hoorcollege 1', 'Calculus 2 werkgroep 1']]}

>>>>>>> origin/master:poging2.py
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
<<<<<<< HEAD:hillclimbing.py
=======
                                    #print amount_of_hiscores
                                    if amount_of_hiscores == 5000:
                                        x = np.arange(0,len(lijst_scores),1)
                                        plt.scatter(x, lijst_scores)
                                        plt.plot(x,lijst_scores)
                                        xlabel('Trials')
                                        ylabel('Score')
                                        plt.savefig("hillclimbing2")
                                        print "highscore is", high_score
                                        return starting_score, high_score, starting_schedule
>>>>>>> origin/master:poging2.py

                        hour = hour + 1
                        if keep_track_new_course in course_and_activity:
                            course_and_activity.remove(keep_track_new_course)
                    hour = 0
                    day = day + 1
                hour = 0
                day = 0

<<<<<<< HEAD:hillclimbing.py
    # For making a scatterplot of the highscore:
    #x = np.arange(0,len(lijst_scores),1)
    #plt.scatter(x, lijst_scores)
    #plt.xlabel('Iterations')
    #plt.ylabel('Score')
    #plt.plot(x, lijst_scores)
    #plt.savefig("hillclimbing2")
=======
    x = np.arange(0,len(lijst_scores),1)

    plt.scatter(x, lijst_scores)

    xlabel('Iterations')
    ylabel('Score')
    plt.plot(x, lijst_scores)
    plt.savefig("hillclimbing2")
>>>>>>> origin/master:poging2.py

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
