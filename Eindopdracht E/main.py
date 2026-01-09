"""
Variant E – Bioscoopticketautomaat

Laat gebruikers een film kiezen (3 opties) en een tijdslot. 
Tickets verschillen in prijs per leeftijdscategorie: 
kind (€5), volwassene (€8), student/65+ (€6). Elke film heeft een maximumcapaciteit. 
Simuleer 30 klanten en geef inzicht in: hoeveel tickets per film, welke categorieën het meest kopen, 
en hoe vaak 'uitverkocht' voorkomt. 
"""

from appJar import gui
import simulatie

app=gui('Bioscoopticketautomaat','600x300')

filmCapaciteiten = {
    'Oppenheimer': {
        '13:00': 30,
        '15:00': 25,
        '17:00': 25,
    },
    'Dune': {
        '18:30': 35,
        '19:00': 35,
        '20:00': 30,
    },
    'Avatar': {
        '8:00': 40,
        '12:00': 35,
        '16:00': 50,
    }
}


def koop(name,gesimuleerd=False,klant=None):
    global filmCapaciteiten

    if gesimuleerd and klant:
        filmkeuze=klant.film
        tijdslot=klant.tijdslot
        kind=klant.kinderen
        volwassene=klant.volwassenen
        student65=klant.studenten65
    else:
        filmkeuze=str(app.getOptionBox('filmkeuzes'))
        tijdslot=str(app.getOptionBox('tijdslot'))
        kind=int(app.getSpinBox('kind'))
        volwassene=int(app.getSpinBox('volwassene'))
        student65=int(app.getSpinBox('student/65+'))
        
    if filmkeuze:
        capaciteit=filmCapaciteiten[filmkeuze][tijdslot]
    else:
        capaciteit=0
    
    
    if kind+volwassene+student65<=capaciteit:
        filmCapaciteiten[filmkeuze][tijdslot]-=kind+volwassene+student65
        if not gesimuleerd:
            app.setLabel('capaciteit',f'Nog {capaciteit} plaatsen beschikbaar')
            app.setLabel('intro','Transactie succesvol!')
            app.after(3000, lambda: app.setLabel('intro','Bioscoopticketautomaat'))
        
        with open('Eindopdracht E/tickets.txt','a') as f:
            f.write(f'{filmkeuze}: {kind} kinderen, {volwassene} volwassenen, {student65} studenten/65+\'ers totale prijs: €{kind*5+volwassene*8+student65*6}. Plaatsen over: {capaciteit}\n')

            #f.write(f'{filmkeuze}, {kind}, {volwassene}, {student65}\n')
    else:
        if not gesimuleerd:
            app.setLabel('intro','Transactie onsuccesvol! Er zijn niet genoeg plaatsen bij de film.')
            app.after(5000, lambda: app.setLabel('intro','Bioscoopticketautomaat'))
        with open('Eindopdracht E/tickets.txt','a') as f:
            f.write(f'GEFAALD, TE WEINIG PLAATSEN: {filmkeuze}: {kind} kinderen, {volwassene} volwassenen, {student65} studenten/65+\'ers totale prijs: €{kind*5+volwassene*8+student65*6}. Plaatsen over: {capaciteit-(kind+volwassene+student65)}\n')


def resetlog():
    with open('Eindopdracht E/tickets.txt','w') as f:
        f.write(f'')

def film_veranderd(naam):
    global filmCapaciteiten,oudefilm
    
    film = str(app.getOptionBox('filmkeuzes'))
    tijdslot=str(app.getOptionBox('tijdslot'))
    if oudefilm!=film:
        app.changeOptionBox('tijdslot',list(filmCapaciteiten[film].keys()))
    oudefilm=film
    
    tijdslot=str(app.getOptionBox('tijdslot'))

    if (film in filmCapaciteiten):
        if tijdslot in filmCapaciteiten[film]:
            app.setLabel('capaciteit', f'Nog {filmCapaciteiten[film][tijdslot]} plaatsen beschikbaar')
    else:
        app.setLabel('capaciteit', 'Nog niets geselecteerd!')

def analyseer(klanten):
    app.hideLabel('intro')
    app.hideLabel('capaciteit')
    app.hideLabel('kindlabel')
    app.hideLabel('volwassenelabel')
    app.hideLabel('student/65+label')

    app.addLabel('kinderen',f'aantal kinderen: {klanten.kinderen}')
    app.addLabel('volwassenen',f'aantal kinderen: {klanten.volwassenen}')
    app.addLabel('studenten65',f'aantal kinderen: {klanten.studenten65}')
    app.addLabel('kinderen',f'aantal kinderen: {klanten.kinderen}')
    app.addLabel('film',f'aantal kinderen: {klanten.film}')
    app.addLabel('film',f'aantal kinderen: {klanten.tijdslot}')

    
oudefilm=''

app.setBg("#c7c7c7")


app.addLabel('intro','Bioscoopticketautomaat')
app.addLabel('capaciteit',f'Nog niets geselecteerd!')

app.addOptionBox('filmkeuzes',list(filmCapaciteiten.keys()))
app.addOptionBox('tijdslot',['-tijden-'])
film_veranderd('')
app.addLabel('kindlabel','Aantal kinderen (€5)')
app.addSpinBoxRange('kind',0,128)
app.addLabel('volwassenelabel','Aantal volwassenen (€8)')
app.addSpinBoxRange('volwassene',0,128)
app.addLabel('student/65+label','Aantal studenten/65+\'ers (€6)')
app.addSpinBoxRange('student/65+',0,128)
app.addButton('koop',koop)
app.addButton('reset tickets',resetlog)
app.addButton('analyse',analyseer)
app.setOptionBoxChangeFunction('filmkeuzes', film_veranderd)
app.setOptionBoxChangeFunction('tijdslot', film_veranderd)

simulateer=True
if simulateer:
    resetlog()
    klanten=simulatie.simuleer(20,filmCapaciteiten)
    for klant in klanten:
        koop('',True,klant)

    
app.go()



