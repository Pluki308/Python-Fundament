'''#import datetime


jaar=0#datetime.datetime.now().year
saldo=100

while saldo<400:
    saldo*=1.1
    jaar+=1
print(f'saldo: {saldo}, jaar: {jaar}')'''

levenlang=False
jaar=0
saldo=150000
while saldo>0:
    saldo=1.04*saldo-5000
    jaar+=1
    if jaar>150:
        levenlang=True
        break
if levenlang:
    print(f'je kan de rest van je leven hiervan leven (meer dan 150 jaar. saldo: {saldo} jaar: {jaar})')
else:       

    print(f'saldo: {(saldo+5000)/1.04}, jaar: {jaar-1}')