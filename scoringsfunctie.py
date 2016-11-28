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



for row in file_zalen:
    zalen.append(row)
print zalen

for row in file_vakken:
    vakken.append(row[0])



rooster = main()
vakrooster = {}
dag = 0
tijdsblok = 0

tijdsblokken = []
count  = 0


print rooster.keys()
for zaal in rooster.keys():
    for meerzalen in zalen:
        if zaal == meerzalen[0]:
            capaciteit_zaal = meerzalen[1]


for vak in vakken:
    for rooms in rooster.values():
        zaal = 0
        for zaal_per_dag in rooms:
            for tijdsblok_per_zaal in zaal_per_dag:

                # heb je een zaal, zoek de capaciteit van de zaal
                # zoek capaciteit van vak
                if vak == tijdsblok_per_zaal:
                    #print "true"
                    tijdsblokken.append((dag,tijdsblok))
                    #print tijdsblokken
                tijdsblok += 1
            tijdsblok = 0
            dag = dag +1
        dag = 0

    vakrooster[vak] = tijdsblokken
    tijdsblokken = []

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
