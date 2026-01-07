from math import ceil

streepjescode='00190198451385'
validLengths=[8,12,13,14,17,18]
sumSC=0
#even=start met 3x
#oneven=start met 1x
i=0
if len(str(streepjescode)) in validLengths:
    for num in str(streepjescode):
        if i+1<len(str(streepjescode)):
            if len(str(streepjescode))%2==0:
                num=int(num)
                if i%2==0:
                    sumSC+=num*3
                elif i%2==1:
                    sumSC+=num
            elif len(str(streepjescode))%2==1:
                num=int(num)
                if i%2==0:
                    sumSC+=num
                elif i%2==1:
                    sumSC+=num*3
        i+=1
else:
    print('Ongeldige code, niet een ven de mogelijke lengtes')

closestHighTen=ceil(sumSC/10)*10
if int(str(streepjescode)[len(str(streepjescode))-1])==closestHighTen-sumSC:
    print('Deze code is geldig!')
else:
    print('Ongeldige code, het laatste getal klopt niet')