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
    print(f'{current_set[0]+current_set[1]+current_set[2]}\n{current_set[3]+current_set[4]+current_set[5]}\n{current_set[6]+current_set[7]+current_set[8]}\n')


''' de boxes zijn zo:
123
456
789

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
    app.addButton(f'box{i+1}',buttonClick,i//3+1,i%3)

'''
app.addButton('box1',buttonClick,1,0)
app.addButton('box4',buttonClick,1,1)
app.addButton('box7',buttonClick,1,2)
app.addButton('box2',buttonClick,2,0)
app.addButton('box5',buttonClick,2,1)
app.addButton('box8',buttonClick,2,2)
app.addButton('box3',buttonClick,3,0)
app.addButton('box6',buttonClick,3,1)
app.addButton('box9',buttonClick,3,2)
'''

reset()
checkWin()
app.addButton("reset", reset,4,1)
app.addButton("selectX", selectX,4,0)
app.addButton("selectO", selectO,4,2)

app.go()