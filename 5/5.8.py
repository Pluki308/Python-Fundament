def berekenKorting(prijsExclKorting, korting=0):
    if korting<0 or korting>100:
        prijsInclKorting=prijsExclKorting
    else:
        prijsInclKorting=prijsExclKorting*korting/100
    if prijsInclKorting>-1:
        return prijsInclKorting
    else:
        return 0

#Hoofdprogramma
prijsExclKorting = float(input("Geef de prijs:"))
prijsInclKorting = berekenKorting(prijsExclKorting, 150)
print("Prijs inclusief 15% korting: " + str(prijsInclKorting))