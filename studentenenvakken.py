import csv
with open('studentenenvakken.csv') as csvfile:
    studenten = csv.DictReader(csvfile)
    for row in studenten:
        # door column namen uit csv door te geven als row['naam'] kun je
        # onderdelen die je interesseren uit csv file selecteren
        print(row['Achternaam'], row['Voornaam'], row['Vak1'])

import csv
with open('zalen.csv', 'rU') as csvfile:
    zalen = csv.DictReader(csvfile)
    for row in zalen:
        print row['zaalnummer'], row['max_capaciteit']

print(studenten[0]) 
