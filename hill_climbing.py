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
            print "key':",  key
            print "week:", week
            for days in week:
                print days
                for hours in days:
                    print hours
                    for row in course_and_activity:
                        course = row
<<<<<<< Updated upstream

                        # remember current course in schedule
                        current_course = schedule[key][day][hour]


                        #remember the score of the schedule without new value
                        scoring_schedule_previous = scoringsfunctie(schedule, courses)
=======
                        print "course:", course
                        current_course = schedule[key][day][hour]
                        print "schedule" ,schedule[key][day][hour]
                        if current_course in course_and_activity:
                            current_course = current_course
                        else:
                            current_course = row[0]

                        schedule[key][day][hour] = course
                        print " new schedule:", schedule
>>>>>>> Stashed changes

                        # only remember current course when it is still in course_and_activity list

                        # put in new value in schedule
                        schedule[key][day][hour] = course

                        # score the new value
                        scoring_schedule_current = scoringsfunctie(schedule, courses)
                        #print 'high score nu', high_score
                        #print 'gewone score nu', scoring_schedule_current

                        if high_score < scoring_schedule_current:
                            high_score = scoring_schedule_current
                            print 'current highscore', high_score
                            print 'met course', course
                            keep_track_new_course = course

<<<<<<< Updated upstream
                        if scoring_schedule_previous < scoring_schedule_current:
                            keep_track_secondbest_score = course

                        if scoring_schedule_previous > scoring_schedule_current:
                            if current_course in course_and_activity:
                                previous_best_score = current_course
                            elif keep_track_secondbest_score != '':
                                if keep_track_secondbest_score in course_and_activity:
                                    previous_best_score = keep_track_secondbest_score
                            else:
                                previous_best_score = course
                        else:
                            previous_best_score = course

                    print "invullen beste vak... "
                    print "met highscore: ", high_score
                    if keep_track_new_course != 'empty':
                        schedule[key][day][hour] = keep_track_new_course
                        course_and_activity.remove(keep_track_new_course)
                        print 'new course:', keep_track_new_course
                    elif keep_track_secondbest_score != 'empty':
                        schedule[key][day][hour] = keep_track_secondbest_score
                        course_and_activity.remove(keep_track_secondbest_score)
                        print 'second best', keep_track_secondbest_score
                    elif previous_best_score != 'empty':
                        schedule[key][day][hour] = previous_best_score
                        course_and_activity.remove(previous_best_score)
                        print 'vorige vak was beter', previous_best_score
                    else:
                        schedule[key][day][hour] = course
                        course_and_activity.remove(course)
                        print 'geen van de opties', course

                    print schedule 
                    keep_track_new_course = 'empty'
                    keep_track_secondbest_score = 'empty'
                    previous_best_score = 'empty'
                    schedule = schedule
=======
                        schedule[key][day][hour] = keep_track_new_course

                        print 'current schedule'
                        print schedule

                        print "hihgscore:", high_score
                        print 'key is: ', key
                        print 'current day', day
                        print 'current hour', hour
                        print 'course that has been placed:', keep_track_new_course

                        course_and_activity.remove(keep_track_new_course)
>>>>>>> Stashed changes

                        hour = hour + 1
                hour = 0
                day = day + 1
            hour = 0
            day = 0

    print high_score
    print schedule

hill_climbing()
