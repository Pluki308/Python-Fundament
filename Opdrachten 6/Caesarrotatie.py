sleutel=input('Wil je versleutelen (0) of ontsleutelen (1)? kies 0 of 1: ')
if sleutel=='0':tekst = input('welke tekst wil je versleutelen? ')
if sleutel=='1':tekst = input('welke tekst wil je ontsleutelen? ')
alfabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters_nieuw=[]

xyzVersleutel = {
    'x': 'a', 'y': 'b', 'z': 'c',
    'X': 'A', 'Y': 'B', 'Z': 'C'
}
abcOntsleutel = {
    'a': 'x', 'b': 'y', 'c': 'z',
    'A': 'X', 'B': 'Y', 'C': 'Z'
}
for letter in tekst:
    if letter in alfabet:
        if sleutel=='0':
            if (letter.lower()=='x' or letter.lower()=='y' or letter.lower()=='z') and sleutel=='0':
                letters_nieuw.append(xyzVersleutel.get(letter, letter))
            else:
                letterPositie = ord(letter)			# Waarde is: 65
                letterPositie_nieuw = letterPositie + 3;	# Waarde is: 68
                letters_nieuw.append(chr(letterPositie_nieuw));	# Waarde is: D
        elif sleutel=='1':
            if (letter.lower()=='a' or letter.lower()=='b' or letter.lower()=='c') and sleutel=='1':
                letters_nieuw.append(abcOntsleutel.get(letter, letter))
            else:
                letterPositie = ord(letter)			# Waarde is: 65
                letterPositie_nieuw = letterPositie - 3;	# Waarde is: 68
                letters_nieuw.append(chr(letterPositie_nieuw));	# Waarde is: D
        
    else:
        letters_nieuw.append(letter)

tekst_nieuw=''
for letter in letters_nieuw:
    tekst_nieuw=f'{tekst_nieuw}{letter}'

print(tekst_nieuw)