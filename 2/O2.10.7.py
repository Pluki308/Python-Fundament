from datetime import datetime
datumtijd = datetime.now()
jaar = datumtijd.year
maand = datumtijd.month
dag = datumtijd.day
geboortedatum=datetime(2009, 3, 10)
dezedatum=datetime(jaar,maand,dag)
leeftijd=dezedatum-geboortedatum
print(leeftijd.days/365.25)
