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

filmCapaciteiten={
            'Oppenheimer':40,
            'Dune':30,
            'Avatar':50,
        }

def koop(name,gesimuleerd=False,klant=None):
    global filmCapaciteiten

    if gesimuleerd and klant:
        filmkeuze=klant.film
        kind=klant.kinderen
        volwassene=klant.volwassenen
        student65=klant.studenten65
    else:
        filmkeuze=str(app.getOptionBox('filmkeuzes'))
        kind=int(app.getSpinBox('kind'))
        volwassene=int(app.getSpinBox('volwassene'))
        student65=int(app.getSpinBox('student/65+'))

    if filmkeuze:
        capaciteit=filmCapaciteiten[filmkeuze]
    else:
        capaciteit=0
    
    
    if kind+volwassene+student65<=capaciteit:
        filmCapaciteiten[filmkeuze]-=kind+volwassene+student65
        if not gesimuleerd:
            app.setLabel('capaciteit',f'Nog {filmCapaciteiten[filmkeuze]} plaatsen beschikbaar')
            app.setLabel('intro','Transactie succesvol!')
            app.after(3000, lambda: app.setLabel('intro','Bioscoopticketautomaat'))
        with open('Eindopdracht E/tickets.txt','a') as f:
            f.write(f'{filmkeuze}: {kind} kinderen, {volwassene} volwassenen, {student65} studenten/65+\'ers totale prijs: €{kind*5+volwassene*8+student65*6}. Plaatsen over: {filmCapaciteiten[filmkeuze]}\n')

            #f.write(f'{filmkeuze}, {kind}, {volwassene}, {student65}\n')
    else:
        if not gesimuleerd:
            app.setLabel('intro','Transactie onsuccesvol! Er zijn niet genoeg plaatsen bij de film.')
            app.after(5000, lambda: app.setLabel('intro','Bioscoopticketautomaat'))
        with open('Eindopdracht E/tickets.txt','a') as f:
            f.write(f'GEFAALD, TE WEINIG PLAATSEN: {filmkeuze}: {kind} kinderen, {volwassene} volwassenen, {student65} studenten/65+\'ers totale prijs: €{kind*5+volwassene*8+student65*6}. Plaatsen over: {filmCapaciteiten[filmkeuze]-(kind+volwassene+student65)}\n')


def resetlog():
    with open('Eindopdracht E/tickets.txt','w') as f:
        f.write(f'')


app.setBg("#c7c7c7")


app.addLabel('intro','Bioscoopticketautomaat')
app.addLabel('capaciteit',f'Nog niets geselecteerd!')
app.addOptionBox('filmkeuzes',['-Films-','Oppenheimer','Help!','Avatar'])
app.addLabel('kindlabel','Aantal kinderen (€5)')
app.addSpinBoxRange('kind',0,128)
app.addLabel('volwassenelabel','Aantal volwassenen (€8)')
app.addSpinBoxRange('volwassene',0,128)
app.addLabel('student/65+label','Aantal studenten/65+\'ers (€6)')
app.addSpinBoxRange('student/65+',0,128)
app.addButton('koop',koop)
app.addButton('reset tickets',resetlog)

simuleren=True
aantalklanten=20
if simuleren:
    klanten=simulatie.simulateer(aantalklanten,list(filmCapaciteiten.keys()))
    for klant in klanten:
        koop('',True,klant)
    print(filmCapaciteiten)

app.go()

