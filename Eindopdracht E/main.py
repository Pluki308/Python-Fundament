"""
Variant E – Bioscoopticketautomaat

Laat gebruikers een film kiezen (3 opties) en een tijdslot. 
Tickets verschillen in prijs per leeftijdscategorie: 
kind (€5), volwassene (€8), student/65+ (€6). Elke film heeft een maximumcapaciteit. 
Simuleer 30 klanten en geef inzicht in: hoeveel tickets per film, welke categorieën het meest kopen, 
en hoe vaak 'uitverkocht' voorkomt. 
"""

from appJar import gui
app=gui('Bioscoopticketautomaat','600x300')

filmCapaciteiten=None

def koop(name):
    global filmCapaciteiten
    filmkeuze=str(app.getOptionBox('filmkeuzes'))
    if filmkeuze and filmCapaciteiten==None:
        filmCapaciteiten={
            'Oppenheimer':30,
            'Help!':20,
            'Avatar':50,
        }
        capaciteit=filmCapaciteiten[filmkeuze]
    elif filmkeuze:
        capaciteit=filmCapaciteiten[filmkeuze]
    else:
        capaciteit=0
    
    kind=int(app.getSpinBox('kind'))
    volwassene=int(app.getSpinBox('volwassene'))
    student65=int(app.getSpinBox('student/65+'))
    if kind+volwassene+student65<=capaciteit:
        filmCapaciteiten[filmkeuze]-=kind+volwassene+student65
        app.setLabel('capaciteit',f'Nog {filmCapaciteiten[filmkeuze]} plaatsen beschikbaar')
        app.setLabel('intro','Transactie succesvol!')
        app.after(3000, lambda: app.setLabel('intro','Bioscoopticketautomaat'))
        with open('Eindopdracht E/tickets.txt','a') as f:
            #f.write(f'{filmkeuze}: {kind} kinderen, {volwassene} volwassenen, {student65} studenten/65+\'ers totale prijs: €{kind*5+volwassene*8+student65*6}\n')
            f.write(f'{filmkeuze}, {kind}, {volwassene}, {student65}\n')

def resetTickets(name):
    with open('Eindopdracht E/tickets.txt','w') as f:
        f.write(f'')


app.setBg("#c7c7c7")


app.addLabel('intro','Bioscoopticketautomaat')
app.addLabel('capaciteit','Nog 0 plaatsen beschikbaar')
app.addOptionBox('filmkeuzes',['-Films-','Oppenheimer','Help!','Avatar'])
app.addLabel('kindlabel','Aantal kinderen (€5)')
app.addSpinBoxRange('kind',0,128)
app.addLabel('volwassenelabel','Aantal volwassenen (€8)')
app.addSpinBoxRange('volwassene',0,128)
app.addLabel('student/65+label','Aantal studenten/65+\'ers (€6)')
app.addSpinBoxRange('student/65+',0,128)
app.addButton('koop',koop)
app.addButton('reset tickets',resetTickets)


app.go()