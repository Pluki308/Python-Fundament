    if aantalKeer >= 8:
        app.setLabel("lbStatus", "Game over!")
        app.setImage("hangman", "hangman8.gif")
        
    elif computerGetal < gebruikerGetal:
        app.setLabel("lbStatus", "Het getal van de computer is kleiner!")
        app.setImage("hangman", "hangman" + str(aantalKeer) + ".gif")
        
    elif computerGetal > gebruikerGetal:
        app.setLabel("lbStatus", "Het getal van de computer is groter!")
        app.setImage("hangman", "hangman" + str(aantalKeer) + ".gif")
        
    else:
        app.setLabel("lbStatus", "Je hebt het geraden!")
    