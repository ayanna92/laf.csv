import numpy as np
import matplotlib.pyplot as plt

from scoringsfunctie import *
from Schedule_room import *
from main import *

import copy
import random
import math

# at this moment we start with a random schedule
schedule, courses = main()
starting_schedule = {'B0.201': [['Zoeken sturen en bewegen practica 3', 'Technology for games werkgroep 2', 'Reflectie op de digitale cultuur werkgroep 1', 'Software engineering practica 2'], ['Webprogrammeren en databases hoorcollege 2', 'Heuristieken 2 hoorcollege 1', 'Data Mining practica 2', 'Data Mining practica 1'], ['Technology for games hoorcollege 2', 'Zoeken sturen en bewegen practica 1', 'Collectieve Intelligentie werkgroep 4', 'Bioinformatica practica 2'], ['Compilerbouw werkgroep 2', 'Data Mining hoorcollege 1', 'Bioinformatica hoorcollege 1', 'Databases 2 werkgroep 1'], ['Data Mining hoorcollege 2', 'Moderne Databases werkgroep 1', 'Algoritmen en complexiteit hoorcollege 1', 'Technology for games hoorcollege 1']], 'A1.08': [['Collectieve Intelligentie practica 1', 'Informatie- en organisatieontwerp practica 1', 'Collectieve Intelligentie practica 2', 'Informatie- en organisatieontwerp practica 2'], ['Technology for games werkgroep 1', 'Project Numerical Recipes practica 2', 'Programmeren in Java 2 practica 1', 'Project Genetic Algorithms practica 3'], ['Collectieve Intelligentie werkgroep 1', 'Reflectie op de digitale cultuur werkgroep 3', 'Moderne Databases practica 3', 'Webprogrammeren en databases practica 1'], ['Reflectie op de digitale cultuur werkgroep 2', 'Netwerken en systeembeveiliging practica 3', 'Informatie- en organisatieontwerp hoorcollege 1', 'Autonomous Agents 2 werkgroep 1'], ['Autonomous Agents 2 practica 2', 'Advanced Heuristics hoorcollege 1', 'Informatie- en organisatieontwerp werkgroep 1', 'Autonomous Agents 2 practica 3']], 'C0.110': [['Databases 2 hoorcollege 1', 'Bioinformatica hoorcollege 2', 'Algoritmen en complexiteit werkgroep 2', 'Data Mining werkgroep 1'], ['Compilerbouw hoorcollege 1', 'Zoeken sturen en bewegen practica 2', 'Collectieve Intelligentie hoorcollege 1', 'Calculus 2 hoorcollege 1'], ['Software engineering hoorcollege 1', 'Collectieve Intelligentie werkgroep 2', 'Kansrekenen 2 hoorcollege 1', 'Algoritmen en complexiteit practica 1'], ['Compilerbouw werkgroep 1', 'Collectieve Intelligentie hoorcollege 2', 'Lineaire Algebra hoorcollege 1', 'Kansrekenen 2 hoorcollege 2'], ['Compilerbouw hoorcollege 2', 'Collectieve Intelligentie hoorcollege 3', 'Webprogrammeren en databases werkgroep 1', 'Software engineering werkgroep 1']], 'A1.04': [['Machine Learning hoorcollege 1', 'Algoritmen en complexiteit werkgroep 1', 'Compilerbouw practica 2', 'Heuristieken 1 werkgroep 1'], ['Autonomous Agents 2 hoorcollege 2', 'Interactie-ontwerp hoorcollege 1', 'Project Genetic Algorithms practica 1', 'Netwerken en systeembeveiliging practica 2'], ['Netwerken en systeembeveiliging practica 4', 'Moderne Databases practica 1', 'Project Genetic Algorithms practica 2', 'Bioinformatica practica 1'], ['Webprogrammeren en databases hoorcollege 1', 'Autonomous Agents 2 werkgroep 3', 'Project Numerical Recipes practica 3', 'Databases 2 werkgroep 2'], ['Software engineering werkgroep 2', 'Webprogrammeren en databases werkgroep 2', 'Moderne Databases werkgroep 2', 'Calculus 2 werkgroep 3']], 'A1.06': [['Data Mining werkgroep 2', 'Webprogrammeren en databases practica 2', 'Data Mining werkgroep 3', 'Collectieve Intelligentie practica 3'], ['Netwerken en systeembeveiliging practica 1', 'Architectuur en computerorganisatie hoorcollege 2', 'Advanced Heuristics practica 2', 'Project Numerical Recipes practica 1'], ['Moderne Databases practica 2', 'Collectieve Intelligentie werkgroep 3', 'Programmeren in Java 2 practica 3', 'Programmeren in Java 2 practica 2'], ['', '', '', 'Autonomous Agents 2 werkgroep 2'], ['Moderne Databases werkgroep 3', 'Informatie- en organisatieontwerp werkgroep 2', 'Interactie-ontwerp hoorcollege 2', 'Architectuur en computerorganisatie hoorcollege 1']], 'C1.112': [['Software engineering practica 1', 'Reflectie op de digitale cultuur hoorcollege 2', 'Lineaire Algebra hoorcollege 2', 'Compilerbouw practica 1'], ['Advanced Heuristics practica 1', 'Bioinformatica werkgroep 3', '', 'Informatie- en organisatieontwerp hoorcollege 2'], ['', 'practicum_compilerbouw practica 1', '', 'Algoritmen en complexiteit practica 2'], ['Heuristieken 1 hoorcollege 1', 'Analysemethoden en -technieken hoorcollege 1', '', 'practicum_compilerbouw practica 2'], ['Autonomous Agents 2 practica 1', 'Heuristieken 2 werkgroep 1', 'Bioinformatica hoorcollege 3', 'Heuristieken 2 werkgroep 2']], 'A1.10': [['Heuristieken 1 werkgroep 2', 'Autonomous Agents 2 hoorcollege 1', 'Moderne Databases hoorcollege 1', 'Collectieve Intelligentie practica 4'], ['Data Mining practica 3', '', 'Bioinformatica werkgroep 1', 'Bioinformatica werkgroep 2'], ['Bioinformatica practica 3', 'Programmeren in Java 2 practica 4', 'practicum_compilerbouw practica 3', ''], ['', 'practicum_compilerbouw practica 4', 'Machine Learning hoorcollege 2', ''], ['Calculus 2 werkgroep 2', '', 'Reflectie op de digitale cultuur hoorcollege 1', 'Calculus 2 werkgroep 1']]}
scoring_schedule = 2562
lists = hoofd_main()
course_and_activity = lists[0]

# set initial temp
temp = 1000
cooling_rate = 0.003

day = 0
hour = 0
high_score = scoring_schedule
SA = True

for key, week in list(starting_schedule.items()):
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
                    acceptance = math.exp((scoring_schedule_new - high_score) / temp)

                    if SA:
                        if temp < 0.0564203093121:
                            temp = 0.0564203093121
                        else:
                            temp *= 1-cooling_rate

                        if acceptance > random.random():
                            high_score = scoring_schedule_new
                            starting_schedule = new_schedule
                            keep_track_new_course = course
                        else:
                            keep_track_new_course = current_course
                    else:
                        if high_score < scoring_schedule_new:
                            print ("new high score")
                            high_score = scoring_schedule_new
                            print (high_score)
                            keep_track_new_course = course
                            starting_schedule = new_schedule
                        else:
                            keep_track_new_course = current_course

                    print ("TEMP")
                    print temp
                    print ("HIGHSCORE")
                    print high_score
                    if temp < 1:
                        sim = False

            print "course_and_activity: ", len(course_and_activity)
            print "course to remove: ", keep_track_new_course
            course_and_activity.remove(keep_track_new_course)
            hour = hour + 1
        hour = 0
        day = day + 1
        print("ZAAL, DAY, HOUR", key, day, hour)
    hour = 0
    day = 0
