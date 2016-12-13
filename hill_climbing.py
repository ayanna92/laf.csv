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
    print schedule

    for row in course_and_activity:
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
        for key, week in list(schedule.items()):

            for days in week:

                for hours in days:
                    print "start:"
                    print key
                    print days
                    print hours

                    for row in course_and_activity:

                        course = row
                        # remember current course in schedule
                        current_course = schedule[key][day][hour]
                        # put in new value in schedule
                        schedule[key][day][hour] = course

                        #find value of course in dictionary
                        # fill in current_course op de plek waar course nu staat


                        # score the new value
                        scoring_schedule_current = scoringsfunctie(schedule, courses)
                        #print 'high score nu', high_score
                        #print 'gewone score nu', scoring_schedule_current

                        if high_score < scoring_schedule_current:
                            high_score = scoring_schedule_current
                            print 'current highscore', high_score
                            print 'met course', course
                            keep_track_new_course = course
                        else:
                            keep_track_new_course = current_course

                    schedule[key][day][hour] = keep_track_new_course

                    print 'current schedule'
                    print schedule

                    print "hihgscore:", high_score
                    print 'key is: ', key
                    print 'current day', day
                    print 'current hour', hour
                    print 'course that has been placed:', keep_track_new_course

                    course_and_activity.remove(keep_track_new_course)

                    hour = hour + 1
                hour = 0
                day = day + 1
            hour = 0
            day = 0

    print high_score
    print schedule

hill_climbing()
