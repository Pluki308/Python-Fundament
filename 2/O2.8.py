naam=input("Mijn naam is ")
print("Mijn naam bestaat uit " + str(len(naam)) + " letters")
print(naam.split(" ")[0].lower())
achternaam=""
for i in range(1, len(naam.split(" "))):
    achternaam=achternaam + naam.split(" ")[i].upper() + ' '
print(achternaam)