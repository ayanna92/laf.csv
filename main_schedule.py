from class_rooster import *

def main(student_list, course_list, zalen_list):
    import random

    time_list = []

    rooster_zaal_list = []
    for zalen in zalen_list:
        room_schedule = RoomSchedule(zalen)
        rooster_zaal_list.append(room_schedule)

    rooster_student_list = []
    for student in student_list:
        student_schedule = StudentSchedule(student)
        rooster_student_list.append(student_schedule) #make sure stud_num is in here

    for course in course_list:
        tijd_slot = TijdSlot(course) #hoe vragen we hier apart type college aantal

        student_schedule_tijdslot = []
        for student in tijd_slot.students: # in TijdSlot moet students
            for student_schedule in student_schedule_tijdslot:
                if student == student_schedule.student_id:
                    student_schedule_tijdslot.append(student_schedule)

        tijd_slot.classification()
        room_schedule = random.choice(rooster_zaal_list)

        while(True):
            if tijd_slot.emptyRoom(room_schedule): #emptyRoom def aanmaken
                tijd_slot.fillSlot(room_schedule, student_schedule_tijdslot)
                tijd_slot.zaal = room_schedule.zaal
                time_list.append(tijd_slot)
                break
            else:
                tijd_slot.classification()
                room_schedule = random.choice(rooster_zaal_list)

    return [rooster_zaal_list, student_schedule_tijdslot, course_list, time_list]
