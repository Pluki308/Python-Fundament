from appJar import gui


def buttonClick(naam):
    global selected
    
    if not app.getButton(naam):
        if selected=='X':
            app.setButton(naam,'X')
            selected='O'
        elif selected=='O':
            app.setButton(naam,'O')
            selected='X'
    else:
        app.setLabel('intro','Al ingevoerd.')
        app.after(1000,lambda: app.setLabel('intro','TikTacToe'))
    checkWin()

def checkWin():
    winning_sets=['OOO______','___OOO___','______OOO','O__O__O__','_O__O__O_','__O__O__O','O___O___O','__O_O_O__']
    current_set=''
    for i in range(9):
        if app.getButton(f'box{i+1}'):
            current_set+=(app.getButton(f'box{i+1}'))
        else:
            current_set+='_'
    print(current_set)


''' de boxes zijn zo:
147
258
369

OOO     ___     ___     O__     _O_     __O     O__     __O
___     OOO     ___     O__     _O_     __O     _O_     _O_
___     ___     OOO     O__     _O_     __O     __O     O__

'''

def reset():
    global selected
    selected='X'
    for i in range(9):
        app.setButton(f'box{i+1}','')

def selectX():
    global selected
    selected='X'
def selectO():
    global selected
    selected='O'


app = gui("Tafels", "300x150")



app.setBg("#c7c7c7")

app.addLabel("intro", "TicTacToe",0,0,colspan=3)
for i in range(9):
    app.addButton(f'box{i+1}',buttonClick,i%3+1,i//3)


reset()
checkWin()
app.addButton("reset", reset,4,1)
app.addButton("selectX", selectX,4,0)
app.addButton("selectO", selectO,4,2)

app.go()