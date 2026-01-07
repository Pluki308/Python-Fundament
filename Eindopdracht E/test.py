import random
filmkeuzes=[['oppenheimer',50], ['zoolander',30], ['help!',25]]
filmnamen = [f[0] for f in filmkeuzes]
film=''
leeftijdscategoriekeuzes=[['kind',5],['volwassene',8],['student/65+',6]]
leeftijdsnamen = [l[0] for l in leeftijdscategoriekeuzes]
leeftijdscategorie=''
selecting_movie=True
selecting_age=False

def maak_klanten(films, leeftijdscategories, aantalklanten):
    klanten=[]
    for i in range(aantalklanten):
        randomgetalfilm=random.randint(0,len(films)-1)
        randomgetalleeftijd=random.randint(0,len(leeftijdscategories)-1)
        filmkeuze=films[randomgetalfilm]
        leeftijd=leeftijdscategories[randomgetalleeftijd]
        klanten.append([filmkeuze,leeftijd])
    return klanten

print(maak_klanten(filmnamen,leeftijdsnamen,30))