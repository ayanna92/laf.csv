# scoringsfunctie

# Ayanne, Femke en Lois

# functie die het aantal punten returned

from Schedule_room_test import *
from class_rooms import *
from class_courses import *



fil_2 = open('vakken2.csv')
file_vakken = csv.reader(fil_2)
vakken = []

for row in file_vakken:
    vakken.append(row[0])

rooster = main()
vakrooster = {}

for vak in vakken:
    for rooms in rooster.values():
        print "rooom is"
        for room in rooms:
            for vak2 in room:
                if vak  ==  vak2:
                    print "jeej"
        

def scoringsfunctie(schedulerooms_list, vakken):
    # als alle acitiviteiten een zaal toegewezen hebben gekregen
        # points += 1000
    # else
        # print("error")

    rooster = main()
    vakrooster = {}
    # maak een lijst voor elke vak wanneer ze gegeven worden

    for vak in vakken:
        for room in rooster.keys():
            print vak

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
