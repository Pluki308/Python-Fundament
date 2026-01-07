def hextodec(hexnum):
    hexdigits='0123456789abcdef'
    hexnum_dec=[]
    i=0
    for digit in hexnum:
        for i in range (0,16):
            if str(digit).lower() == str(hexdigits[i]):
                hexnum_dec.append(i)
    total=0
    j=len(hexnum_dec)-1
    for digit in hexnum_dec:
        total+=16**(j)*int(digit)
        j-=1
    return total


rgbNum='216C43'
rNum=f'{rgbNum[0]}{rgbNum[1]}'
gNum=f'{rgbNum[2]}{rgbNum[3]}'
bNum=f'{rgbNum[4]}{rgbNum[5]}'

averageNum=hex(int(round((hextodec(rNum)+hextodec(gNum)+hextodec(bNum))/3,0)))

print(f'{hex(hextodec(averageNum))[2:]}{hex(hextodec(averageNum))[2:]}{hex(hextodec(averageNum))[2:]}'.upper())