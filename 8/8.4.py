from appJar import gui

def buttonKlik(name):
  app.setLabel("label", "Knop is ingedrukt")

app = gui("Buttons", "300x150")

app.setBg("lightblue")

app.addLabel("label", "Welkom!")
app.addButton("Klik mij!", buttonKlik)
app.go()