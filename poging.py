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

print "starting schedule", starting_schedule
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
                        index_zero = 0

                                    #new_schedule[key][dag][uur] = current_course

                    #print "new start:", starting_schedule
                    new_schedule[key][day][hour] = course
                    #print" nog een keer:", starting_schedule
                    # score the new value
                    #print " changed new schedule:", new_schedule
                    scoring_schedule_new = scoringsfunctie(new_schedule, courses)
                    #print scoring_schedule_new
                    #print " changed new schedule:", new_schedule
                    #print 'high score nu', high_score
                    #print 'gewone score nu', scoring_schedule_current


                    if high_score < scoring_schedule_new:
                        high_score = scoring_schedule_new
                        print starting_schedule
                        keep_track_new_course = course
                        starting_schedule = new_schedule
                        print "new high score found: "
                        print high_score
                        print "IN ZAAL, DAY, HOUR:"
                        print key, day, hour
                        print new_schedule
                        print "current course:", current_course
                        print "is now", course
                        print "DONE"

                    keep_track_new_course = current_course

                course_and_activity.remove(keep_track_new_course)
                print "schedule start is now:", starting_schedule

                hour = hour + 1
            hour = 0
            day = day + 1
            print "zaal:  ",key
            print "day:   ",day

        hour = 0
        day = 0

print "END", high_score
print "END", starting_schedule

hill_climbing()
