import random

def analyseer():
    klanten=[]
    aantalKlanten=20
    for i in range(aantalKlanten):
        klantgeld = random.randint(1,10)
        klantkoek = random.randint(1,10)
        klantchips = random. randint(1,10)
        klantwater = random. randint(1,10)
        klantcola = random.randint(1,10)
        klanten.append({'geld':klantgeld,'koek':klantkoek,'chips':klantchips,'water':klantwater,'cola':klantcola})
    return klanten

klanten=analyseer()
print(klanten)