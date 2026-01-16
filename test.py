from appJar import gui
import random
import string



def buttonKlik():
  app.setLabel('postcode',f'{random.randint(1000,9999)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}')

letter = random.choice(string.ascii_uppercase)

app = gui("Buttons", "300x150")

app.setBg("#c7c7c7")

app.addLabel("postcode", "Welkom!")
app.addButton("Klik mij!", buttonKlik)
app.go()