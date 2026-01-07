

class Pijl():
    def __init__(self,nummer,punten,beurt):
        self.nummer=nummer
        self.punten=punten
        self.beurt=beurt



def vraagScore(pijl):
    score = int(input("Score van pijl " + str(pijl) + ": "))
    while (True):
        if score<=60 and score>=0:
            return score
        else:
            score = int(input("Tusen de 0 en 60 punten: Score van pijl " + str(pijl) + ": "))
    
    

punten=501
temppunten=0
beurt=0
pijlnummer=10
#pijlen=[]
beurtpijlen=[]
i=0
while punten>0:
    
    
    if pijlnummer>=3:
        beurtpijlen=[]
        punten-=temppunten
        temppunten=0
        beurt+=1
        print(f'\nBeurt {beurt}')
        print(f'aantal punten: {punten}')
        pijlnummer=0
    else:
        pijlnummer+=1
        temppijl=Pijl(pijlnummer,None,beurt)
        temppijl.punten=vraagScore(f'#{temppijl.nummer}')
        
        temppunten+=temppijl.punten
        #print(punten-temppunten)
        if punten-temppunten>0:
            
            #pijlen.append(temppijl)
            continue
        elif punten-temppunten<0:
            print(f'Je hebt nu {punten-temppunten} punten! Deze beurt telt niet.')
            #beurtpijlen=[p for p in pijlen if p.beurt == beurt]
            #for p in beurtpijlen:
            #    pijlen.remove(p)
            temppunten=0
            pijlnummer=10
            
            
        else:
            print('Je hebt precies goed! Je bent uit🎉')
            punten-=temppunten
            #pijlen.append(temppijl)

        
#print([f'{pijlen[i].beurt}.{pijlen[i].nummer}: {pijlen[i].punten}' for i in range(0,len(pijlen))])
