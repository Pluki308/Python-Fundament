from appJar import gui
import random

app = gui("Hangman", "600x300")

def hangman():
    global cnum,strikes,dood
    if strikes<8:
        app.setImage('hangman',f'hangman{strikes}.gif')
    elif strikes==8:
        app.setImage('hangman',f'hangman{strikes}.gif')
        app.setLabel('evaluation',f'Game over! Je bent dood.')
        dood=True
    else:
        app.setLabel('evaluation',f'Game over! Je bent dood.')
        dood=True
def raden():
    global dood
    if not dood:
        global cnum,strikes
        antwoord = app.getEntry("antwoord")
        if str(antwoord) == str(cnum):
            app.setLabel('evaluation',f'Goed antwoord ({cnum})! fouten: #{strikes}')
            app.setBg("#41ec85")
            app.clearEntry('antwoord')
            hangman()
        
        
        else:
            strikes+=1
            
            app.setLabel('evaluation',f'Verkeerd antwoord! fouten: #{strikes}')
            app.setBg("#ec4141")
            app.clearEntry('antwoord')
            hangman()
    else:
        app.setLabel('evaluation',f'Game over! Je bent dood.')
        
def reset():
    global cnum,strikes,dood
    strikes=0
    cnum=random.randint(1,10)
    app.setImage("hangman",'hangman0.gif')
    app.setBg("#c7c7c7")
    app.clearEntry('antwoord')
    app.setLabel('evaluation',f'Verkeerd antwoord! fouten: #{strikes}')
    
    dood=False

begin=1
eind=10
app.setBg("#c7c7c7")
cnum=random.randint(begin,eind)
app.addLabel("intro", f"Raad het getal tussen de {begin} en {eind}",0,0,2)

dood=False
strikes=0



#app.addLabel("som", f'{nummer1} x {nummer2} = ?')

app.addLabel("evaluation", "",1,0)

app.addLabelEntry("antwoord",2,0)
app.setLabel('antwoord','')
app.addImage("hangman",'hangman0.gif',1,1,0,3)
#app.setLabel('antwoord','')

app.addButton("Raden", raden,3,0)
app.addButton("Reset", reset,4,0)
app.go()