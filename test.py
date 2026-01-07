from appJar import gui
from random import randint
app = gui("Buttons", "300x150")
nummer1 = 0
nummer2 = 0
antwoord = 0
streak = 0
def nieuwesom():
    global nummer1,nummer2
    nummer1 = randint(1,10)
    nummer2 = randint(1,10)
    uitkomst = nummer1 * nummer2
    app.setLabel("som", f"{nummer1} * {nummer2} =")
    app.clearEntry("Uitkomst")
    app.setLabel("goed", "")
    
def controleer(name):
    global antwoord, streak
    antwoord = app.getEntry("Uitkomst")
    antwoord = int(app.getEntry("Uitkomst"))
    if antwoord == nummer1 * nummer2:
      
      streak += 1
      app.setLabel("goed", f"goed (streak #{streak})")
      app.after(2000, nieuwesom)
      
    else:
        app.setLabel("goed", "fout")
        streak = 0
app.addLabelEntry("Uitkomst")
app.addButton("controleer", controleer)
app.addButton("genereer", nieuwesom)
app.addLabel("som", "")
app.addLabel("goed", "")
app.go()