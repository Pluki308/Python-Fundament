from math import ceil
class Olibol():
    def __init__(self,melk,gist,ei,bloem):
        self.melk=melk
        self.gist=gist
        self.ei=ei
        self.bloem=bloem

melkpak=1000 #40 olibollen
gist=3 #60 olibollen
ei=6 #120 olibollen
bloem=500 #20 olibollen


olibol=Olibol(25, #500/20
              1/20,
              1/20,
              25 #500/20
)

aantal=int(input('Hoeveel olibollen wil je bakken? '))
aantalBloem=(aantal*olibol.bloem)/bloem
aantalMelk=(aantal*olibol.melk)/melkpak
aantalGist=(aantal*olibol.gist)/gist
aantalEi=(aantal*olibol.ei)/ei




aantalOlibollen=(ceil(aantalBloem)*bloem)/olibol.bloem
if aantalOlibollen>(ceil(aantalMelk)*melkpak)/olibol.melk:
    aantalOlibollen=(ceil(aantalMelk)*melkpak)/olibol.melk
if aantalOlibollen>(ceil(aantalGist)*gist)/olibol.gist:
    aantalOlibollen=(ceil(aantalGist)*gist)/olibol.gist
if aantalOlibollen>(ceil(aantalEi)*ei)/olibol.ei:
    aantalOlibollen=(ceil(aantalEi)*ei)/olibol.ei
    



print(f'Je hebt ingrediënten nodig voor {aantalOlibollen:.0f} olibollen, anders kloppen de verhoudingen niet.\n')


if aantalMelk == 1:
    melk_tekst = f"Je hebt dan precies genoeg aan {int(aantalMelk)} pak melk!"
elif aantalMelk.is_integer():
    melk_tekst = f"Je hebt dan precies genoeg aan {int(aantalMelk)} pakken melk!"
else:
    melk_tekst = f"Je hebt {ceil(aantalMelk)} pakken melk nodig."

if aantalGist == 1:
    gist_tekst = f"Je hebt dan precies genoeg aan {int(aantalGist)} verpakking gist!"
elif aantalGist.is_integer():
    gist_tekst = f"Je hebt dan precies genoeg aan {int(aantalGist)} verpakkingen gist!"
else:
    gist_tekst = f"Je hebt {ceil(aantalGist)} verpakkingen gist nodig."

if aantalEi == 1:
    ei_tekst = f"Je hebt dan precies genoeg aan {int(aantalEi)} verpakking ei!"
elif aantalEi.is_integer():
    ei_tekst = f"Je hebt dan precies genoeg aan {int(aantalEi)} verpakkingen ei!"
else:
    ei_tekst = f"Je hebt {ceil(aantalEi)} verpakkingen ei nodig."

if aantalBloem == 1:
    bloem_tekst = f"Je hebt dan precies genoeg aan {int(aantalBloem)} pak bloem!"
elif aantalBloem.is_integer():
    bloem_tekst = f"Je hebt dan precies genoeg aan {int(aantalBloem)} pakken bloem!"
else:
    bloem_tekst = f"Je hebt {ceil(aantalBloem)} pakken bloem nodig."



print(f'''
Ingrediëntenlijst:
Melk
Je hebt {aantalMelk*melkpak:.1f} ml melk nodig. In één verpakking zit {melkpak} ml melk.
{melk_tekst}

Gist
Je hebt {aantalGist*gist:.1f} zakjes gist nodig. In één verpakking zitten {gist} zakjes.
{gist_tekst}

Ei
Je hebt {aantalEi*ei:.1f} stuks ei nodig. In één verpakking zitten {ei} stuks.
{ei_tekst}

Bloem
Je hebt {aantalBloem*bloem:.1f} g bloem nodig. In één verpakking zit {bloem} g bloem.
{bloem_tekst}

Suiker, zout en zonnebloemolie heb je al genoeg.
''')




'''


De volgende lijst bevat de ingrediënten om ongeveer 20 oliebollen te bakken.

    500 ml melk
    1 zakje gist (7 g)
    1 ei
    500 g bloem
    #3 eetlepels suiker
    #Snufje zout
    #Zonnebloemolie om in te bakken

    Deze producten zijn te koop per:

    Melk: een pak van 1 liter (1000 ml)
    Gist: een doosje met 3 zakjes gist
    Bloem: een zak van 500 gram
    Eieren: een doos met 6 eieren


'''
