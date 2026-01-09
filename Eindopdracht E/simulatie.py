import random

class Klant():
    def __init__(self, kinderen, volwassenen, studenten65, films):
        self.kinderen = int(kinderen)
        self.volwassenen = int(volwassenen)
        self.studenten65 = int(studenten65)

        self.film = random.choice(list(films.keys()))
        self.tijdslot = random.choice(list(films[self.film].keys()))

    def __repr__(self):
        return (f"Klant(film={self.film}, tijdslot={self.tijdslot}, "
                f"kinderen={self.kinderen}, volwassenen={self.volwassenen}, "
                f"studenten65={self.studenten65})")


def simuleer(aantalKlanten, films):
    klanten = []
    for i in range(aantalKlanten):
        klanten.append(Klant(random.randint(0, 3),random.randint(0, 3),random.randint(0, 3),films))
    return klanten





'''films = {
    'Oppenheimer': {
        '15:00': 40,
        '17:00': 40,
        '21:00': 40
    },
    'Dune': {
        '15:00': 30,
        '17:00': 30,
        '21:00': 30
    },
    'Avatar': {
        '15:00': 50,
        '17:00': 50,
        '21:00': 50
    }
}

klanten = simuleer(5, films)

for klant in klanten:
    print(klant)'''
