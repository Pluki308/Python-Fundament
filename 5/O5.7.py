def vraagKortingspercentage():
  percentage = float(input("Voer het kortingspercentage in:"))
  while percentage<0 or percentage>100:
    percentage = float(input("Voer het kortingspercentage in:"))
  return percentage

#Hoofdprogramma
prijs = float(input("Wat is de prijs?"))
kortingspercentage = vraagKortingspercentage()
teBetalen = (prijs - kortingspercentage / 100 * prijs)
print(f"Te betalen: {teBetalen:.2f} EUR.")