from random import randint

def bigsmallguesses(gokken):
    gokken_groot=[]
    gokken_klein=[]
    if gokken:
        for gok in gokken:
            if gok[1]==True:
                gokken_groot.append(gok)
            elif gok[1]==False:
                gokken_klein.append(gok)
            else:
                continue
    return gokken_groot, gokken_klein


startgetal=int(input('Welk getal als ondergrens?: '))
eindgetal=int(input('Welk getal als bovengrens?: '))
computerGetal = randint(startgetal,eindgetal)
gameover = False
keer_geraden=0
gokken=[[startgetal-1,True],[eindgetal+1,False]]

while not gameover:
    
    gokken_groot, gokken_klein=bigsmallguesses(gokken)
    gebruikerGetal = int(input(f"Raad een getal tussen de {max(gokken_groot)[0]} en de {min(gokken_klein)[0]}: "))
    if gebruikerGetal>max(gokken_groot)[0] and gebruikerGetal<min(gokken_klein)[0]:
        keer_geraden+=1
        if keer_geraden>=8:
            print(f"Game over, het getal was {computerGetal}")
            gameover = True
        elif computerGetal < gebruikerGetal:
            print(f"Het getal van de computer is kleiner! Je hebt {8-keer_geraden} pogingen over.")
            groterDanGetal=False

        elif computerGetal > gebruikerGetal:
            print(f"Het getal van de computer is groter! Je hebt {8-keer_geraden} pogingen over.")
            groterDanGetal=True
        
        else:
            print("Je hebt het geraden!")
            groterDanGetal=None
            gameover = True
        gokken.append([gebruikerGetal,groterDanGetal])
    else:
        print(f'Dat getal zit niet tussen de {max(gokken_groot)[0]} en de {min(gokken_klein)[0]}. Probeer opniew.')
        
    
print(gokken)