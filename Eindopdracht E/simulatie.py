import random

class Klant():
    def __init__(self,kinderen,volwassenen,studenten65,films):
        self.kinderen=kinderen
        self.volwassenen=volwassenen
        self.studenten65=studenten65

        self.film = random.choice(films)
        

def simulateer(aantalKlanten,films):
    klanten=[]
    for i in range(aantalKlanten):

        klanten.append(Klant(random.randint(0,3),random.randint(0,3),random.randint(0,3),films))
    return klanten

