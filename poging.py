# try out

from scoringsfunctie import *
from Schedule_room import *
from main import *

import copy
import random

# at this moment we start with a random schedule
schedule, courses = main()
starting_schedule = {'B0.201': [['Technology for games werkgroep 1', 'Technology for games werkgroep 2', 'Webprogrammeren en databases hoorcollege 1', 'Webprogrammeren en databases hoorcollege 2'], ['Webprogrammeren en databases werkgroep 1', 'Webprogrammeren en databases werkgroep 2', 'Webprogrammeren en databases practica 1', 'Webprogrammeren en databases practica 2'], ['Zoeken sturen en bewegen practica 1', 'Zoeken sturen en bewegen practica 2', 'Zoeken sturen en bewegen practica 3', ''], ['Bioinformatica werkgroep 3', 'Bioinformatica werkgroep 1', 'Bioinformatica practica 1', 'Algoritmen en complexiteit werkgroep 2'], ['Software engineering hoorcollege 1', 'Calculus 2 werkgroep 2', 'Technology for games hoorcollege 2', 'Collectieve Intelligentie hoorcollege 3']], 'A1.08': [['Advanced Heuristics practica 1', 'Algoritmen en complexiteit werkgroep 1', 'Autonomous Agents 2 practica 2', 'Software engineering werkgroep 2'], ['Heuristieken 2 werkgroep 1', 'Autonomous Agents 2 hoorcollege 2', 'practicum_compilerbouw practica 3', 'Reflectie op de digitale cultuur werkgroep 2'], ['Informatie- en organisatieontwerp werkgroep 1', 'Informatie- en organisatieontwerp hoorcollege 1', 'Netwerken en systeembeveiliging practica 2', 'Project Numerical Recipes practica 2'], ['Heuristieken 2 hoorcollege 1', 'Databases 2 hoorcollege 1', 'Project Genetic Algorithms practica 1', 'Advanced Heuristics practica 2'], ['Data Mining practica 2', 'Bioinformatica werkgroep 2', 'Programmeren in Java 2 practica 1', 'Collectieve Intelligentie werkgroep 4']], 'C0.110': [['Moderne Databases practica 2', 'Software engineering werkgroep 1', 'Data Mining werkgroep 3', 'Compilerbouw practica 1'], ['Kansrekenen 2 hoorcollege 2', 'Interactie-ontwerp hoorcollege 2', 'Technology for games hoorcollege 2', 'Bioinformatica practica 3'], ['Lineaire Algebra hoorcollege 1', 'Reflectie op de digitale cultuur werkgroep 3', 'Moderne Databases hoorcollege 1', 'Analysemethoden en -technieken hoorcollege 1'], ['Software engineering practica 1', 'Programmeren in Java 2 practica 3', 'Algoritmen en complexiteit practica 1', 'Machine Learning hoorcollege 2'], ['Programmeren in Java 2 practica 2', 'Calculus 2 werkgroep 1', 'Bioinformatica practica 2', 'Heuristieken 2 werkgroep 2']], 'A1.04': [['Kansrekenen 2 hoorcollege 1', 'Technology for games hoorcollege 2', 'Algoritmen en complexiteit hoorcollege 1', 'Bioinformatica hoorcollege 3'], ['Databases 2 werkgroep 2', 'Compilerbouw hoorcollege 1', 'practicum_compilerbouw practica 2', 'Heuristieken 1 werkgroep 2'], ['Collectieve Intelligentie werkgroep 2', 'Technology for games hoorcollege 2', 'Moderne Databases werkgroep 2', 'Calculus 2 werkgroep 3'], ['Algoritmen en complexiteit practica 2', 'Interactie-ontwerp hoorcollege 1', 'Software engineering practica 2', 'Data Mining hoorcollege 1'], ['Compilerbouw hoorcollege 2', 'Moderne Databases werkgroep 3', 'Technology for games hoorcollege 2', 'Informatie- en organisatieontwerp werkgroep 2']], 'A1.06': [['Netwerken en systeembeveiliging practica 4', 'Collectieve Intelligentie hoorcollege 2', 'Informatie- en organisatieontwerp practica 1', 'Machine Learning hoorcollege 1'], ['Reflectie op de digitale cultuur hoorcollege 2', 'Technology for games hoorcollege 2', 'Technology for games werkgroep 1', 'practicum_compilerbouw practica 1'], ['Collectieve Intelligentie practica 4', 'Data Mining practica 3', 'Collectieve Intelligentie practica 2', 'practicum_compilerbouw practica 4'], ['Autonomous Agents 2 hoorcollege 1', 'Collectieve Intelligentie werkgroep 3', 'Autonomous Agents 2 werkgroep 1', 'Databases 2 werkgroep 1'], ['Project Genetic Algorithms practica 3', 'Technology for games hoorcollege 2', 'Reflectie op de digitale cultuur werkgroep 1', 'Architectuur en computerorganisatie hoorcollege 2']], 'C1.112': [['Netwerken en systeembeveiliging practica 3', 'Advanced Heuristics hoorcollege 1', 'Compilerbouw werkgroep 2', 'Moderne Databases practica 1'], ['Heuristieken 1 werkgroep 1', 'Collectieve Intelligentie practica 3', 'Autonomous Agents 2 practica 1', 'Technology for games hoorcollege 2'], ['Lineaire Algebra hoorcollege 2', 'Data Mining werkgroep 1', 'Collectieve Intelligentie werkgroep 1', 'Technology for games hoorcollege 2'], ['Technology for games hoorcollege 2', 'Project Genetic Algorithms practica 2', 'Heuristieken 1 hoorcollege 1', 'Architectuur en computerorganisatie hoorcollege 1'], ['Informatie- en organisatieontwerp practica 2', 'Reflectie op de digitale cultuur hoorcollege 1', 'Programmeren in Java 2 practica 4', 'Autonomous Agents 2 werkgroep 3']], 'A1.10': [['Compilerbouw werkgroep 1', 'Technology for games hoorcollege 1', 'Calculus 2 hoorcollege 1', 'Data Mining werkgroep 2'], ['Netwerken en systeembeveiliging practica 1', 'Data Mining hoorcollege 2', 'Collectieve Intelligentie hoorcollege 1', 'Bioinformatica hoorcollege 2'], ['Compilerbouw practica 2', 'Technology for games hoorcollege 2', 'Bioinformatica hoorcollege 1', 'Autonomous Agents 2 werkgroep 2'], ['Project Numerical Recipes practica 3', 'Data Mining practica 1', 'Autonomous Agents 2 practica 3', 'Collectieve Intelligentie practica 1'], ['Moderne Databases werkgroep 1', 'Informatie- en organisatieontwerp hoorcollege 2', 'Project Numerical Recipes practica 1', 'Moderne Databases practica 3']]}
scoring_schedule = -85.0
lists = hoofd_main()
course_and_activity = lists[0]
course_loop = []
keep_track_new_course = ()

for row in course_and_activity:
    #lijst met alle activiteitem
    course_loop.append(row)

classroom_name = lists[1]
random.shuffle(classroom_name)

print "starting schedule", starting_schedule
high_score = -20000

if int(high_score) < int(scoring_schedule):
    high_score = scoring_schedule

    day = 0
    hour = 0
    #print schedule
    for key, week in list(starting_schedule.items()):

        for days in week:
            #print days
            for hours in days:
                #print hours
                for row in course_and_activity:
                    course = row

<<<<<<< HEAD
                    if course == "":
                        print "course is empty"
                    print " uit proberen:",course
                    print "hallllooooooo starting_schedule"
                    # remember current course in schedule
                    current_course = starting_schedule[key][day][hour]
                    keep_track_new_course = starting_schedule[key][day][hour]
                    new_schedule = copy.deepcopy(starting_schedule)
                    print " wat er nu staat:", current_course

                    print "Course die we willen plaatsen:", course
                    print "plek: "
                    print "DAY", day
                    print "hour", hour


                    # remember current course in schedule
                    current_course = starting_schedule[key][day][hour]
                    new_schedule = starting_schedule
                    print "course die er staat:", current_course


                    #remember the score of the schedule without new value
                    #scoring_schedule_previous = scoringsfunctie(starting_schedule, courses)
                    #print "current course:", current_course
                    #print "course:", course
                    #print "old schedule", starting_schedule
                    print "eerste rooster:", starting_schedule

                    #if current_course in course_and_activity:
                    #    current_course = current_course
                    #else:
                    #    current_course = row[0]
                    index_zero = 0
                    index_second = 0
                    #print new_schedule
                    for zaal,week in new_schedule.items():

                        for dag in week:
                            for uur in dag:

                                #print "zaal", zaal
                                #print "DAY, HOUR", index_zero, index_second
                                if course == uur:
                                    #print uur
                                    #print new_schedule[zaal][index_zero][index_second]
                                    print "Course gevonden op: "
                                    print index_zero, index_second
                                    print "course was: ", new_schedule[zaal][index_zero][index_second]
                                    new_schedule[zaal][index_zero][index_second] = current_course
                                    print "course is: ", new_schedule[zaal][index_zero][index_second]
                                    #print new_schedule[zaal][index_zero][index_second]
                                else:
                                    index_second = index_second + 1
                            index_second = 0
                            index_zero = index_zero + 1
                        index_second = 0
=======
                    if course != "":


                        #if course == "":
                            #print "course is empty"
                        #print " uit proberen:",course
                        #print "hallllooooooo starting_schedule"
                        # remember current course in schedule
                        current_course = starting_schedule[key][day][hour]
                        keep_track_new_course = starting_schedule[key][day][hour]
                        new_schedule = copy.deepcopy(starting_schedule)
                        #print " wat er nu staat:", current_course

                        #print "Course die we willen plaatsen:", course
                        #print "plek: "
                        #print "DAY", day
                        #print "hour", hour


                        # remember current course in schedule
                        #new_schedule = starting_schedule
                        #print "course die er staat:", current_course

                        #remember the score of the schedule without new value
                        #scoring_schedule_previous = scoringsfunctie(starting_schedule, courses)
                        #print "current course:", current_course
                        #print "course:", course
                        #print "old schedule", starting_schedule
                        #print "eerste rooster:", starting_schedule

                        #if current_course in course_and_activity:
                        #    current_course = current_course
                        #else:
                        #    current_course = row[0]
>>>>>>> origin/master
                        index_zero = 0
                        index_second = 0
                        #print new_schedule
                        for zaal,week in new_schedule.items():

                            for dag in week:
                                for uur in dag:

                                    #print "zaal", zaal
                                    #print "DAY, HOUR", index_zero, index_second
                                    if course == uur:
                                        #print uur
                                        #print new_schedule[zaal][index_zero][index_second]
                                        #print "Course gevonden op: "
                                        #print index_zero, index_second
                                        #print "course was: ", new_schedule[zaal][index_zero][index_second]
                                        new_schedule[zaal][index_zero][index_second] = current_course
                                        #print "course is: ", new_schedule[zaal][index_zero][index_second]
                                        #print new_schedule[zaal][index_zero][index_second]
                                    else:
                                        index_second = index_second + 1
                                index_second = 0
                                index_zero = index_zero + 1
                            index_second = 0
                            index_zero = 0

                        new_schedule[key][day][hour] = course

                        #print" nog een keer:", new_schedule
                        #print " beter blijft dee hetzelfde", starting_schedule


                        #print" nog een keer:", starting_schedule
                        # score the new value

                        scoring_schedule_new = scoringsfunctie(new_schedule, courses)

<<<<<<< HEAD
                    new_schedule[key][day][hour] = course

                    print" nog een keer:", new_schedule
                    print " beter blijft dee hetzelfde", starting_schedule


                    #print" nog een keer:", starting_schedule
                    # score the new value
                    #print " changed new schedule:", new_schedule

                    scoring_schedule_new = scoringsfunctie(new_schedule, courses)

                    print "high_score:", high_score
                    print "score niewe rooster: ", scoring_schedule_new
                    if high_score < scoring_schedule_new:
                        high_score = scoring_schedule_new
                        #print starting_schedule
                        keep_track_new_course = course
                        starting_schedule = new_schedule
                    else:
                        starting_schedule = starting_schedule

                    print "schedule start is now:", starting_schedule
=======
                        #print "high_score:", high_score
                        #print "score niewe rooster: ", scoring_schedule_new
                        if high_score < scoring_schedule_new:
                            high_score = scoring_schedule_new
                            print "NEW HIGHSCORE"
                            print high_score
                            print "oude rooster"
                            print starting_schedule
                            print "nieuwe rooster"
                            print new_schedule
                            #print starting_schedule
                            keep_track_new_course = course
                            starting_schedule = new_schedule
                        else:
                            starting_schedule = starting_schedule
>>>>>>> origin/master

                        #print "schedule start is now:", starting_schedule
                print "zaal, day, hour", key, day, hour
                hour = hour + 1
                course_and_activity.remove(keep_track_new_course)
            hour = 0
            day = day + 1
            print "zaal:  ",key
            print "day:   ",day

        hour = 0
        day = 0

print "END", high_score
print "END", starting_schedule

hill_climbing()
