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

def reset():
    global selected
    selected='X'
    app.setButton('box1','')
    app.setButton('box2','')
    app.setButton('box3','')
    app.setButton('box4','')
    app.setButton('box5','')
    app.setButton('box6','')
    app.setButton('box7','')
    app.setButton('box8','')
    app.setButton('box9','')

def selectX():
    global selected
    selected='X'
def selectO():
    global selected
    selected='O'


app = gui("Tafels", "300x150")



app.setBg("#c7c7c7")

app.addLabel("intro", "TicTacToe",0,0,colspan=3)
app.addButton('box1',buttonClick,1,0)
app.addButton('box2',buttonClick,2,0)
app.addButton('box3',buttonClick,3,0)
app.addButton('box4',buttonClick,1,1)
app.addButton('box5',buttonClick,2,1)
app.addButton('box6',buttonClick,3,1)
app.addButton('box7',buttonClick,1,2)
app.addButton('box8',buttonClick,2,2)
app.addButton('box9',buttonClick,3,2)

reset()

app.addButton("reset", reset,4,1)
app.addButton("selectX", selectX,4,0)
app.addButton("selectO", selectO,4,2)

app.go()