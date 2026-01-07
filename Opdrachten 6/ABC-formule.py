print('De ABC formule!')

a=int(input('Welke waarde heeft: a? '))
b=int(input('Welke waarde heeft: b? '))
c=int(input('Welke waarde heeft: c? '))

D=(b**2-4*a*c)
Xeen=(-b+D**0.5)/(2*a)
Xtwee=(-b-D**0.5)/(2*a)

print(f'D: {D}')
print(f'x1: {Xeen:.1f}')
print(f'x2: {Xtwee:.1f}')