import random

filmkeuzes=[['oppenheimer',50], ['zoolander',30], ['help!',25]]
filmnamen = [f[0] for f in filmkeuzes]
film=''
leeftijdscategoriekeuzes=[['kind',5],['volwassene',8],['student/65+',6]]
leeftijdsnamen = [l[0] for l in leeftijdscategoriekeuzes]
leeftijdscategorie=''
selecting_movie=True
selecting_age=False
while True:
    # selecteer de films
    if (film not in filmnamen) and selecting_movie:
        film=input(f'Welke film wil je kiezen? kies uit {", ".join(f[0].capitalize() for f in filmkeuzes)}: ').lower()
    elif (film in filmnamen) and selecting_movie:
        print(f'U heeft geselecteerd: {film.capitalize()}')
        selecting_movie=False
        selecting_age=True
    elif (leeftijdscategorie not in leeftijdsnamen) and selecting_age:
        leeftijdscategorie=input(f'Welke film wil je kiezen? kies uit {", ".join(l[0].capitalize() for l in leeftijdscategoriekeuzes)}: ').lower()
    elif (leeftijdscategorie in leeftijdsnamen) and selecting_age: 
        print(f'U heeft geselecteerd: {leeftijdscategorie.capitalize()}')
        selecting_age=False
        break
