# try out

from scoringsfunctie import *
from Schedule_room import *
from main import *


import random

# at this moment we start with a random schedule
schedule, courses = main()
starting_schedule = schedule
scoring_schedule = scoringsfunctie(schedule, courses)
lists = hoofd_main()
course_and_activity = lists[0]
course_loop = []
keep_track_new_course = ()

for row in course_and_activity:
    #lijst met alle activiteitem
    course_loop.append(row)

classroom_name = lists[1]
random.shuffle(classroom_name)


high_score = -20000
previsou_score = scoring_schedule

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

                    # remember current course in schedule
                    current_course = starting_schedule[key][day][hour]
                    new_schedule = starting_schedule

                    #remember the score of the schedule without new value
                    #scoring_schedule_previous = scoringsfunctie(starting_schedule, courses)
                    print "current course:", current_course
                    print "course:", course
                    print "old schedule", starting_schedule
                    print "new schedule" ,new_schedule


                    #if current_course in course_and_activity:
                    #    current_course = current_course
                    #else:
                    #    current_course = row[0]

                    for zaal,week in starting_schedule.items():
                        dagje = 0
                        for dag in week:
                            #print dag
                            if course in dag:
                                i = dag.index(course)
                                print i, dagje
                                dag[i] = current_course
                            dagje += 1

                    print "new start:", starting_schedule
                    starting_schedule[key][day][hour] = course
                    print" nog een keer:", starting_schedule



                    # score the new value
                    print " changed new schedule:", new_schedule
                    scoring_schedule_current = scoringsfunctie(new_schedule, courses)
                    print " changed new schedule:", new_schedule
                    #print 'high score nu', high_score
                    #print 'gewone score nu', scoring_schedule_current


                    if high_score < scoring_schedule_current:
                        high_score = scoring_schedule_current
                        starting_schedule = new_schedule
                        print "meer punten"
                        print high_score
                        print starting_schedule

                course_and_activity.remove(keep_track_new_course)


            hour = hour + 1
        hour = 0
        day = day + 1
    hour = 0
    day = 0

print high_score
print schedule

hill_climbing()
