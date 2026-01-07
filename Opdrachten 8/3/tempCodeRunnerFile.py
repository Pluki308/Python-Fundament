    else:
            strikes+=1
            hangman()
            app.setLabel('evaluation',f'Verkeerd antwoord! fouten: #{strikes}')
            app.setBg("#ec4141")
            app.clearEntry('antwoord')