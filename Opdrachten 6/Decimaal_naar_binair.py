num=int(input('Geef een positief decimaal getal: '))
bits=[]


remaining=num
len_bin=0


while 2**len_bin<num:
    len_bin+=1
i=len_bin-1

while len(bits)<len_bin:
    if 2**i<=remaining:
        bits.append(1)
        remaining-=2**i
    else:
        bits.append(0)
    
    i-=1



bits_str=''
for bit in bits:
    bits_str=f'{bits_str}{bit}'

print(f'Het decimale getal {num} is binair: {bits_str}')