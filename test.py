from appJar import gui
import random
  
def genereerWachtwoord(name):
  lengte = int(app.getOptionBox("lengte"))
  tekens = ""
  wachtwoord = ""
  
  # Kleine letters?
  if app.getCheckBox("Kleine letters"):
    tekens = tekens + "abcdefghijklmnopqrstuvwxyz"
  # Hoofdletters
  if app.getCheckBox("Hoofdletters"):
    tekens = tekens + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  # Cijfers
  if app.getCheckBox("Cijfers"):
    tekens = tekens + "0123456789"
  # Tekensn
  if app.getCheckBox("Tekens"):
    tekens = tekens + "!@#$%^&amp;*()-+{}[];:\|/?"
  
  # Genereer
  for x in range(lengte):
    teken = random.choice(tekens)
    wachtwoord = wachtwoord + teken
  
  # Plaats in textbox
  app.setEntry("ww", wachtwoord)
  
  
# De app
app = gui("Wachtwoordgenerator", "400x200")
  
app.addLabel("lb1", "Wachtwoordgenerator", 0, 0, 2, 0)
app.addEntry("ww", 1, 0, 2, 0)
app.addOptionBox("lengte", ["- Lengte -", "16", "20", "24", "28", "32"], 2, 0)
app.addButton("Genereren", genereerWachtwoord, 4, 0)
app.addCheckBox("Kleine letters", 2, 1)
app.addCheckBox("Hoofdletters", 3, 1)
app.addCheckBox("Cijfers", 4, 1)
app.addCheckBox("Tekens", 5, 1)
  
app.go()