num=int(input('Geef een positief decimaal getal: '))
hexs=[]
digit=0


remaining=num
len_hex=0


while 16**len_hex<=num:
    len_hex+=1
i=len_hex-1

while len(hexs)<len_hex:
    digit=remaining//(16**i)
    hexs.append(digit)
    remaining-=(16**i)*digit
    i-=1


hex_digits='0123456789ABCDEF'
hexs_str=''
for hex in hexs:
    hexs_str=f'{hexs_str}{hex_digits[hex]}'

print(f'Het decimale getal {num} is hexadecimaal: {hexs_str}')