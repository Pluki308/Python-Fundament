
def genereren():
    antwoord = app.getEntry("antwoord")
    if str(antwoord) == str(nummer2*nummer1):
        streak+=1
        app.setLabel('evaluation',f'Goed antwoord! Streak: #{streak}')
        app.setBg("#41ec85")
        nummer1=random.randint(1,10)
        nummer2=random.randint(1,10)
        app.setLabel('antwoord',f'{nummer1} x {nummer2} = ')
        app.clearEntry('antwoord')
        
    else:
        streak=0
        app.setLabel('evaluation',f'Verkeerd antwoord! Streak: #{streak}')
        app.setBg("#ec4141")
        app.clearEntry('antwoord')
        