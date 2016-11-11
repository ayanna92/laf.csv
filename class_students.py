# students
# Lectures & roosters
#
# Ayanna, Femke & Lois
#

import csv

class students(object):
    with open('studentenenvakken.csv') as csvfile:
        studenten = csv.DictReader(csvfile)
        info = []

        for row in studenten:
        # door column namen uit csv door te geven als row['naam'] kun je
        # onderdelen die je interesseren uit csv file selecteren
            info.append(row)
        print info







#class students(object):

    #def __init__(self):
        # voor/achternaam (studentnummer)
        #for row in

        # aantal vakken [1-5]

        # naam vak [max array of 5]
