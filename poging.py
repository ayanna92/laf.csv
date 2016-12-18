# try out

from scoringsfunctie import *
from Schedule_room import *
from main import *

import copy
import random

# at this moment we start with a random schedule
schedule, courses = main()
starting_schedule = copy.deepcopy(schedule)
scoring_schedule = scoringsfunctie(starting_schedule, courses)
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

                    if course != "":
                        # remember current course in schedule
                        current_course = starting_schedule[key][day][hour]
                        new_schedule = copy.deepcopy(starting_schedule)


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
                                        new_schedule[zaal][index_zero][index_second] = current_course
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

                        if high_score < scoring_schedule_new:
                            high_score = scoring_schedule_new
                            print "NEW HIGHSCORE"
                            print high_score
                            print "oude rooster"
                            print starting_schedule
                            print "nieuwe rooster"
                            print new_schedule
                            print "current course", current_course
                            print "course", course
                            #print starting_schedule
                            keep_track_new_course = course
                            starting_schedule = new_schedule
                        else:
                            starting_schedule = starting_schedule
                            keep_track_new_course = current_course


                        #print "schedule start is now:", starting_schedule
                print "zaal, day, hour", key, day, hour
                if keep_track_new_course != "":
                    course_and_activity.remove(keep_track_new_course)
                hour = hour + 1
            hour = 0
            day = day + 1
        hour = 0
        day = 0

print "END", high_score
print "END", starting_schedule
