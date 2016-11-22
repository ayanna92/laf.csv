from class_rooster import *
from class_tijdslot import *

def main(student_list, course_list, zalen_list):
    import random

    time_list = []

    # create objects to schedule room
    rooster_zaal_list = []
    for zalen in zalen_list:
        room_schedule = RoomSchedule(zalen)
        rooster_zaal_list.append(room_schedule)

    # create objects to schedule students
    rooster_student_list = []
    for student in student_list:
        student_schedule = StudentSchedule(student)
        rooster_student_list.append(student_schedule) #make sure stud_num is in here

    # create a timeslot for different course types(hoorcollege, practica, werkcollege)
    # assign them to a day, hour and room
    for course in course_list:
        tijd_slot = TijdSlot(course)

        # a list of student schedule for every student in tijd slot
        student_schedule_tijdslot = []
        for student in tijd_slot.students:
            for student_schedule in student_schedule_tijdslot:
                if student == student_schedule.student_id:
                    student_schedule_tijdslot.append(student_schedule)

        # give random day & hour to tijdslot
        tijd_slot.classification()
        room_schedule = random.choice(rooster_zaal_list)


        while(True):

            # if tijd slot room is empty, fill room schedule and room student
            if tijd_slot.emptyTijdslotRoom(room_schedule):
                tijd_slot.fillSlot(room_schedule, student_schedule_tijdslot)
                tijd_slot.zaal = room_schedule.zaal
                time_list.append(tijd_slot)
                break

            # if not assign a new random day and hour, and then go through loop again
            else:
                tijd_slot.classification()
                room_schedule = random.choice(rooster_zaal_list)

    return [rooster_zaal_list, student_schedule_tijdslot, course_list, time_list]
