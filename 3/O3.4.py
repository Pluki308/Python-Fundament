'''origineleprijs = int(input("Hoe duur is uw product?: "))
if origineleprijs > 150:
    prijs = origineleprijs * 1.19
elif origineleprijs < 55:
    prijs = origineleprijs * 1.11
else:
    prijs = origineleprijs * 1.16
print(f'Nieuwe prijs is: {prijs}.')
'''
'''kost=1500
spaargeld=int(input('hoeveel geld heb je om uit te geven?: '))
if kost-spaargeld > 500:
    print(f'je kunt het niet kopen en moet nog €{-spaargeld+kost} verdienen. Een bijbaantje is misschien slim')
elif kost-spaargeld <= 500 and kost-spaargeld>0:
    print(f'je kunt het niet kopen en moet nog €{-spaargeld+kost} verdienen. je bent er bijna')
elif spaargeld>kost:
    print(f'je kunt het kopen met nog €{spaargeld-kost} over')
else:
    print('er is iets fout gegaan')'''
import datetime

uur=datetime.datetime.now().hour
temp=1
luchtvochtigheid=0
if uur==17 or (temp<20 and luchtvochtigheid<0.85):
    print('airco aan')
else: 
    print('airco uit')