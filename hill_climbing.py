# hill climbing algorithm to create schedule
# Lectures & roosters
#
# Ayanna, Lois, Femke
#

# make random schedule
# count scoring
#
# change one little thing
#

from scoringsfunctie import *
from Schedule_room import *
from main import *

def hill_climbing():

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
        course_loop.append(row)

    classroom_name = lists[1]
    random.shuffle(classroom_name)

    high_score = -20000

    if int(high_score) < int(scoring_schedule):
        high_score = scoring_schedule

        day = 0
        hour = 0

        for key, week in list(schedule.items()):

            for days in week:

                for hours in days:

                    for row in course_and_activity:
                        course = row
                        old_course = schedule[key][day][hour]
                        schedule[key][day][hour] = course

                        scoring_schedule = scoringsfunctie(schedule, courses)

                        if high_score < scoring_schedule:
                            high_score = scoring_schedule
                            print 'current highscore', high_score
                            keep_track_new_course = course
                        else:
                            keep_track_new_course = old_course

                    schedule[key][day][hour] = keep_track_new_course
                    print 'current schedule'
                    print schedule
                    print keep_track_new_course
                    print "hihgscore:", high_score

                    print 'current day', day
                    print 'current hour', hour

                    print course_and_activity

                    if keep_track_new_course in course_and_activity:
                        # do nothing
                        course_and_activity.remove(keep_track_new_course)

                    hour = hour + 1
                hour = 0
                day = day + 1
            hour = 0
            day = 0

    print high_score
    print schedule
    return schedule 

hill_climbing()
