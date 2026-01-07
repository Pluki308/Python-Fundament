def vraagNaam():
  voornaam=input('wat is je voornaam?: ')
  achternaam=input('wat is je achternaam?: ')
  return voornaam + " " + achternaam

#Hoofdprogramma
naam = vraagNaam()
print("Jouw naam is " + naam)