from appJar import gui

def buttonKlik(name):
  global kliks
  kliks+=1
  app.setLabel("label", f"{kliks}x geklikt")

app = gui("Buttons", "300x150")

app.setBg("lightblue")
kliks=0
app.addLabel("label", "Welkom!")
app.addButton("Klik mij!", buttonKlik)
app.go()

