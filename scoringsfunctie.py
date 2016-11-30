# scoringsfunctie

# Ayanne, Femke en Lois

# functie die het aantal punten returned

from Schedule_room_test import *
from class_rooms import *
from class_courses import *

fil_2 = open('vakken2.csv')
file_vakken = csv.reader(fil_2)
vakken = []
fil_3 = open("classrooms.csv")
file_zalen = csv.reader(fil_3)
zalen = []
course_student_list = csv.reader(open('course_stud_num.csv'))
course_and_student = []

for row in file_zalen:
    zalen.append(row)

for row in file_vakken:
    vakken.append(row[0])

for row in course_student_list:
    course_and_student.append(row)

rooster = main()
vakrooster = {}

dag = 0
tijdsblok = 0

tijdsblokken = []
count  = 0
capaciteit_zaal = []
minpunten = 0


# voor elk vak een rooster maken wanneer ze voorkomen.
for vak in vakken:
    capacity_vak = 0
    # bereken hoeveel studenten er in het vak zit
    for students in course_and_student:
        if students[0] == vak:
           student_list = students[1:]
           vak_name = Courses(vak, student_list)
           capacity_vak = vak_name.studNumber()
           #print "capacity:"
           #print capacity_vak
    for rooms, rooster_per_room in rooster.items():
        zaal = 0

        capaciteit_zaal = 0
        # wat is de capaciteit van de zaal:
        for meerzalen in zalen:
            if rooms == meerzalen[0]:
                capaciteit_zaal = int(meerzalen[1])
                #print "capaciteit_zaal:"
                #print capaciteit_zaal


        # selecteer voor elke zaal een dag.
        for zaal_per_dag in rooster_per_room:
            for tijdsblok_per_zaal in zaal_per_dag:
                #print tijdsblok_per_zaal
                # check of het vak in het tijdsblok zit.
                if vak == tijdsblok_per_zaal:
                    # voeg toe welke plaats tot het rooster.
                    tijdsblokken.append((dag,tijdsblok))
                    #print tijdsblokken
                    # dan zit het vak dus in deze specifieke zaal
                    print capacity_vak
                    print capaciteit_zaal

                    if capacity_vak > capaciteit_zaal:
                        print "vak past niet in de zaal"
                        minpunten += capacity_vak - capaciteit_zaal
                    elif (capacity_vak) < (capaciteit_zaal):
                        print "vak past er in"


                tijdsblok += 1
            tijdsblok = 0
            dag = dag +1
        dag = 0

    vakrooster[vak] = tijdsblokken
    tijdsblokken = []

print minpunten


#print vakrooster

# als een vak op eenzelfde uur wordt gegeven:
#for vak in vakrooster.keys():
maluspunten = 0
for vak in vakrooster.values():
    for tijdsblok in vak:
        # nog wel te maken met als ze hetzelfde zijn, dan
        if vak.count(tijdsblok) == 2 :
            maluspunten += 10
        if vak.count(tijdsblok) == 3:
            maluspunten += (20/3)
print maluspunten





def scoringsfunctie(schedulerooms_list, vakken):
    # als alle acitiviteiten een zaal toegewezen hebben gekregen
        # points += 1000
    # else
        # print("error")

    rooster = main()
    vakrooster = {}
    # maak een lijst voor elke vak wanneer ze gegeven worden


            # kijk voor elk vak in welke zalen hij zit op welke tijden en sla dit op
            # als de capaciteit van de zaal groter is dan het aantal studenten
            # points -= 1 voor elke student.


    # hier uiteindelijk een lijst met alle vakken en zijn tijden wanneer er les hebben
    #for vak in vakrooster:
        # (vak: heuristieken, tijd :[(dag,tijdvak), (1,2), (2,2), (2,3)]

# bonuspunten:
# als een vak x aantal activiteit heeft en deze ook op x dagen zijn ingeroostred
    # points += 20
#minpunt:
# als een vak x aantal activieit heeft en deze op x-1 dagen zijn ingeroosterd
    # points -= 10
# als een vak x aantal acitiviteiten heeft en deze op x-2 dagen zijn ingeroosterd
    # points -= 20
# als een vak x aantal acitiviteiten heeft en deze op x-3 dagen zijn ingeroosterd
    # points -= 30


    #for student in student_list:
        #print (student)
        # voor elke student zoek het vak op in vakrooster, pak de tijden van elk vak erbij en kijk of er vakken tegelijkertijd worden gegeven
    #    for vak in student
            # zoek het vak op in het vakrooster
            # kijk welke tijden er zijn
            # als een student een vak heeft op hetzelfde tijdstip
                # points -= 1



    return points



#print scoringsfunctie(, vakken)
