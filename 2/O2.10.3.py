from datetime import datetime
datumtijd = datetime.now()
jaar = datumtijd.year
maand = datumtijd.month
dag = datumtijd.day
print(str(dag) + "-" + str(maand) + "-" + str(jaar))
