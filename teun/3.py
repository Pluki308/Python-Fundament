from appJar import gui
import random

app=gui('Galgje','600x300')

def raden(naam):
    global nummer

    
def reset():
    global nummer
    nummer=random.randint(1,10)

reset()

app.addButton('raden',raden,3,0)
app.addButton('reset',reset)
app.addLabel('label1','raad een getal tussen de 1 en de 100',0,0,2)
app.addLabel('label2','skhjfdakjlhsd',1,0)
app.addEntry('')
app.addImage('hangman','hangman8.gif',1,1)

app.go()