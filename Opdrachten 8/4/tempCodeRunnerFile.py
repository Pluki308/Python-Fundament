from appJar import gui
import random

def buttonClick():
    chars=int(app.getSpinBox('nummers'))
    klein=app.getCheckBox('Kleine letters')
    groot=app.getCheckBox('Hoofdletters')
    cijfer=app.getCheckBox('Cijfers')
    teken=app.getCheckBox('Tekens')
    app.setEntry('wachtwoord',f'{generate(chars,klein,groot,cijfer,teken)}')

def generate2(klein:bool,hoofd:bool,cijfer:bool,teken:bool):
    newteken=''
    typ=random.randint(1,4)
    alphabet_small='abcdefghijklmnopqrstuvwxyz'
    alphabet_big='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    leestekens=r"""`~!@#$%^&*()-_=+[]{}\|;:'",.<>/?"""
    if typ==1 and klein: #alfabet klein
        randomnum=random.randint(1,24)
        newteken=f'{alphabet_small[randomnum-1]}'
    elif typ==2 and hoofd: #alfabet groot
        randomnum=random.randint(1,24)
        newteken=f'{alphabet_big[randomnum-1]}'
    elif typ==3 and cijfer: #cijfer
        randomnum=random.randint(1,9)
        newteken=f'{randomnum}'
    elif typ==4 and teken: #leesteken
        randomnum=random.randint(1,32)
        newteken=f'{leestekens[randomnum-1]}'
    return newteken

def generate(chars:int,klein:bool,hoofd:bool,cijfer:bool,teken:bool):
    tekst=''
    if klein+hoofd+cijfer+teken>0:
        for i in range(chars+1):
            
            newteken=generate2(klein,hoofd,cijfer,teken)
            while newteken=='':
                newteken=generate2(klein,hoofd,cijfer,teken)
            
            tekst=f'{tekst}{newteken}'

        return tekst
    else:
        return 'Geen mogelijkheden!'


app = gui("Tafels", "300x150")


app.setBg("#c7c7c7")

#app.addLabel("som", f'{nummer1} x {nummer2} = ?')
app.addLabel("intro", "Wachtwoordengenerator",0,0,colspan=2)
app.addLabelEntry("wachtwoord",1,0,colspan=2,label=False)
'''with open('Opdrachten 8/4/text.txt', 'r') as f:
    listVoorAantalLetters=[line.strip() for line in f]
    app.addOptionBox('aantalLetters',listVoorAantalLetters,2,0)'''
app.addSpinBoxRange('nummers',1,1024,2,0)
app.addCheckBox('Kleine letters',2,1)
app.addCheckBox('Hoofdletters',3,1)
app.addCheckBox('Cijfers',4,1)
app.addCheckBox('Tekens',5,1)


#app.setLabel('antwoord','')

app.addButton("Genereren", buttonClick,3,0)
app.go()