# scoringsfunctie

# Ayanne, Femke en Lois

# functie die het aantal punten returned

from Schedule_room import *
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
student_course_list = csv.reader(open('studentenenvakken.csv'))
student_en_hun_vakken = []
vakken_volledig = []

next(student_course_list)
for row in student_course_list:
    student_en_hun_vakken.append(row)

for row in file_zalen:
    zalen.append(row)

for row in file_vakken:
    vakken.append(row[0])
    vakken_volledig.append(row)

for row in course_student_list:
    course_and_student.append(row)



def scoringsfunctie(schedule, students):

    # Nu nog omslachtige manier
    # idee is dat als alles straks klopt, je het schedule en de bij behorende lijst met welke studenten welk volgen mee geeft
    # en dan wordt score berekend
    # default is nu scoringsfunctie(0,0)

    trial = main()

    if schedule == 0:
        rooster = trial[0]
        student_import_list = trial[1]
    else:
        rooster = schedule
        student_import_list = trial[1]

    vakroosterhoorcolleges = {}
    vakroosterwerkcolleges = {}
    vakroosterpractica = {}
    vakkenpakketrooster = {}

    dag = 0
    tijdsblok = 0

    tijdsblokkenwerkgroep = []
    tijdsblokkenpractica = []
    tijdsblokkenhoorcollege = []
    count  = 0

    capaciteit_zaal = []
    points = 1000
    minpunt = 0

    # voor elk vak een rooster maken wanneer ze voorkomen.
    for vak in vakken:
        capacity_vak = 0
        # bereken hoeveel studenten er in het vak zit
        for rooms, rooster_per_room in rooster.items():
            zaal = 0
            #print rooms
            capaciteit_zaal = 0
            # wat is de capaciteit van de zaal:
            for meerzalen in zalen:
                if rooms == meerzalen[0]:
                    capaciteit_zaal = int(meerzalen[1])

            # selecteer voor elke zaal een dag.
            for zaal_per_dag in rooster_per_room:
                for vak_per_zaal in zaal_per_dag:
                    if vak in vak_per_zaal:
                        #print vak

                        # bereken capaciteit werkcollege
                        if "werkgroep" in vak_per_zaal:
                            for row in vakken_volledig:
                                if vak == row[0]:
                                    capacity_vak = float(row[3])
                                    tijdsblokkenwerkgroep.append((dag,tijdsblok))
                                    #print capacity_vak, "werkcollege"

                        # bereken capaciteit van hoorcollege:
                        if "hoorcollege" in vak_per_zaal:
                            for students in course_and_student:
                                if students[0] == vak:
                                   student_list = students[1:]
                                   vak_name = Courses(vak, student_list)
                                   capacity_vak = vak_name.studNumber()
                                   tijdsblokkenhoorcollege.append((dag,tijdsblok))
                                   #print capacity_vak, "hoorcollege"

                        # bereken capaciteit van practicum
                        if "practica" in vak_per_zaal:
                            for row in vakken_volledig:
                                if vak == row[0]:
                                    capacity_vak = float(row[5])
                                    tijdsblokkenpractica.append((dag,tijdsblok))

                        vakkenpakketrooster[vak_per_zaal] = ((dag,tijdsblok))
                        if capacity_vak > capaciteit_zaal:
                            #print "vak past niet in de zaal"
                            minpunt += capacity_vak - capaciteit_zaal

                        # voeg toe welke plaats tot het rooster.
                    tijdsblok += 1
                tijdsblok = 0
                dag = dag +1
            dag = 0

        vakroosterhoorcolleges[vak] = tijdsblokkenhoorcollege
        vakroosterpractica[vak] = tijdsblokkenpractica
        vakroosterwerkcolleges[vak] = tijdsblokkenwerkgroep

        tijdsblokkenwerkgroep = []
        tijdsblokkenpractica = []
        tijdsblokkenhoorcollege = []
    points -= minpunt
    #print " Het aantal minpunten vanwege studenten die niet in de zaal passen:" ,minpunt


    #print vakroosterpractica
    #print vakroosterhoorcolleges
    #print vakroosterwerkcolleges
    #print " dit is het vakkenpakketrooster: ", vakkenpakketrooster


    bonuspunten = 0
    minpunten = 0
    for vak_activiteit in vakken_volledig:
         number_of_activities = int(vak_activiteit[1]) + int(vak_activiteit[2]) + int(vak_activiteit[4])

          # de dagen van de colleges:
         daghoorcollege = vakroosterhoorcolleges[vak_activiteit[0]]
         dagwerkcollege = vakroosterwerkcolleges[vak_activiteit[0]]
         dagpracticum = vakroosterpractica[vak_activiteit[0]]
         daglijsthoor = []
         daglijstwerk = []
         daglijstprac = []
         for tijd in daghoorcollege:
            daglijsthoor.append(tijd[0])
         for tijd in dagwerkcollege:
            daglijstwerk.append(tijd[0])
         for tijd in dagpracticum:
            daglijstprac.append(tijd[0])

         # alles uitschrijven op basis van het aantal activiteiten
         # bij 1 activiteit hoeft er niks gedaan te worden.
         # bij twee activiteiten:
         #print vak_activiteit[0]
         if number_of_activities == 2:
             #print "    heeft twee activiteite"
             if len(daglijsthoor) == 2:
                # print "           2 hoorcolleges"
                 verschil = abs(daglijsthoor[0]- daglijsthoor[1])
                 if verschil == 3:
                     bonuspunten += 20
                #     print "                    goed ingeroosterd"
                 elif verschil == 0 :  # dan zijn ze op 1 dag ingeroosterd
                     minpunt -= 10
                #     print "                    2 colleges op 1 dag"

            # als er 1 hoorcollege en 1 werkgroep per week is
             if len(daglijsthoor) == 1 and daglijstwerk != []:
                #print "        1 hoorcollege en 1 werkcollege"
                for dag in daglijstwerk:
                    #print  daglijsthoor, dag
                    verschil = abs(daglijsthoor[0] - dag)
                    if verschil == 3:
                        bonuspunten += 20
                #        print "             goed ingeroosterd"
                    elif verschil == 0 :  # dan zijn ze op 1 dag ingeroosterd
                        minpunt -= 10
                        #print "               2 colleges in 1 dag"

            # als er 1 hoorcollege en 1 practicum per week is:
             if len(daglijsthoor) == 1 and daglijstprac != []:
                # print "        1 hoorcollege en 1 practica"
                 for dag in daglijstprac:
                  # print daglijsthoor, dag
                   verschil = abs(daglijsthoor[0] - dag)
                   if verschil == 3:
                       bonuspunten += 20
                    #   print    "           goed ingeroosterd"
                   elif verschil == 0 :  # dan zijn ze op 1 dag ingeroosterd
                       minpunt -= 10
                     #  print "             2 colleges in 1 dag ingeroosterd"

         if number_of_activities == 3:
            #print "   er zijn 3 colleges"
            if len(daglijsthoor) == 2 and daglijstwerk != []:
                #print "         2 hoocolleges en 1 werkcollges"

                lijst = []
                for dag in daglijstwerk:
                    for dagen in daglijsthoor:
                        lijst.append(dagen)
                    lijst.append(dag)
                    list.sort(lijst)
                    #print lijst
                    if lijst[0] == 0 and lijst[1] == 2 and lijst[2] == 4:
                        bonuspunten += 20
                    #    print "                 Goed ingeroosterd"
                    elif lijst[0] == lijst[1] == lijst[2]:
                        minpunten -= 20
                    #    print "                     3 colleges in 1 dag"
                    elif lijst[0] == lijst[1] or lijst[1] == lijst[2]:
                        minpunten -= 10
                    #    print "                     3 colleges in 2 dagen"

                    lijst = []

            if len(daglijsthoor) == 1 and daglijstwerk != [] and daglijstprac != []:
                #print "             van alles 1 college "
                lijst = []
                #daglijstwerk, daglijstprac
                for dag in daglijstwerk:
                    for dagen in daglijstprac:
                        lijst.append(daglijsthoor[0])
                        lijst.append(dag)
                        lijst.append(dagen)
                        list.sort(lijst)
                        #print lijst
                        if lijst[0] == 0 and lijst[1] == 2 and lijst[2] == 4:
                            bonuspunten += 20
                        #    print "                     goed gedaan"
                        elif lijst[0] == lijst[1] == lijst[2]:
                            minpunten -= 20
                        #    print "                       3 colleges in 1 dag"
                        elif lijst[0] == lijst[1] or lijst[1] == lijst[2]:
                            minpunten -= 10
                    #        print "                     3 colleges in 2 dagen"

                        lijst = []


         if number_of_activities == 4:
            #print "     er zijn vier activiteiten "
            if len(daglijsthoor) == 2 and daglijstwerk != [] and daglijstprac != []:
                #print  "        2 hoorcolleges, 1 werkcollege and 1 practica"
                lijst = []

                for dag in daglijstwerk:
                    for dagen in daglijstprac:
                        for hoor in daglijsthoor:
                            lijst.append(hoor)
                        lijst.append(dag)
                        lijst.append(dagen)
                        list.sort(lijst)
                        #print lijst
                        if lijst[0] == 0 and lijst[1] == 1 and lijst[2] == 3 and lijst[3] == 4:
                            bonuspunten += 20
                            #print "                         extra goed "
                        elif lijst[0] == lijst[1] == lijst[2]==lijst[3]:
                            minpunten -= 30
                            #print "                            4 colleges in 1 dag"
                        elif lijst[0] == lijst[1] == lijst[2] or lijst[1] == lijst[2] == lijst[3]:
                            minpunten -= 20
                            #print "                           4 colleges in 2 dagen"
                        elif lijst[0] == lijst[1] and lijst[2]== lijst[3]:
                            minpunten -= 20
                            #print "                             4 colleges in 2 dagen"
                        elif lijst[0] == lijst[1] or lijst[1] == lijst[2] or lijst[2] == lijst[3]:
                            minpunten -= 10
                            #print "                         4 colleges in 3 dagen"
                        lijst = []
         if number_of_activities == 5:
            #print "     er zijn 5 acitviteiten"
            if len(daglijsthoor) == 3 and daglijstwerk != [] and daglijstprac != []:
                #print "            3 hoorcolleges, 1 werkcollege and 1 practica"
                for dag in daglijstwerk:
                    for dagen in daglijstprac:
                        for hoor in daglijsthoor:
                            lijst.append(hoor)
                        lijst.append(dag)
                        lijst.append(dagen)
                        list.sort(lijst)
                        #print lijst
                        if lijst[0] == 0 and lijst[1] == 1 and lijst[2] == 2 and lijst[3] == 3 and lijst[4] == 4:
                            bonuspunten += 20
                            #print  "                    goed ingeoorsterd"
                        elif lijst[0] == lijst[1] == lijst[2] == lijst[3] == lijst [4]:
                            minpunten -= 40
                            #print "                         5 colleges in 1 dag"
                        elif lijst[0] == lijst[1] == lijst[2] == lijst[3] or lijst[1] == lijst[2] == lijst[3] == lijst[4]:
                            minpunten -= 30
                            #print "                         5 colleges in 2 dagen"
                        elif (lijst[0]== lijst[1] and lijst[2]== lijst[3] == lijst[4]) or (lijst[0] == lijst[1] == lijst[2] and lijst[3] == lijst[4]):
                            minpunten -= 30
                            #print "                         5 colleges in 2 dagen"
                        elif lijst[0] == lijst[1] == lijst[2]  or lijst[1] == lijst[2] == lijst[3] or lijst[2]== lijst[3] == lijst[4]:
                            minpunten -= 20
                            #print "                         5 colleges in 3 dagen"
                        elif (lijst[0]== lijst[1] and lijst[2]== lijst[3]) or (lijst[0] == lijst[1] and lijst[3] == lijst[4]) or (lijst[1] == lijst[2] and lijst[3] == lijst[4]):
                            minpunten -= 20
                            #print "                         5 colleges in 3 dagen"
                        elif lijst[0] == lijst[1] or lijst[1] == lijst[2] or lijst[2] == lijst[3] or lijst[3] == lijst[4]:
                            minpunten -= 10
                            #print "                         5 colleges in 4 dagen"

                        lijst = []

    #print " het aantal bonuspunten van dit rooster:", bonuspunten
    #print " het aantal minpunten van dit rooster:", minpunten


    # conflicten van de studenten berekenen:

    studentrooster = {}
    studierooster = student_import_list

    for student in student_en_hun_vakken:
        studentenlijst = []
        studnumber = int(student[2])
        for vak, studenten in studierooster.items():
            for stud in studenten:
                #print studnumber, stud
                if int(stud) == studnumber:
                        studentenlijst.append( vakkenpakketrooster[vak])
                        studentrooster[studnumber] = studentenlijst


    from collections import Counter
    #print studentrooster
    minpuntstudent = 0
    for student in studentrooster.values():
          waarde = Counter(student).values()
          #print waarde
          if len(waarde)!= len(student):
              minpuntstudent += (len(student) - len(waarde))
    #print " het aantal conflicten bij studenten:" ,minpuntstudent


    total = points + bonuspunten - minpunt + minpunten - minpuntstudent
    print "total points is:", total
    #print studentrooster

    return total

#scoringsfunctie(0,0)
