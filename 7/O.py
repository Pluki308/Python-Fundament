def opdracht(a, b):
  if a < b:
    return 0
  return opdracht(a - b, b) + 1

def faculteit(num,result=1):
  if num==1 or num==0:
    return result 
    # Basiscasus: er is geen recursie meer nodig.

  result*=num
  return faculteit(num-1,result)



def verkrijgKinderen(naam: str):
  global oranje
  if naam in oranje:
    return oranje.get(naam.capitalize())
  return []

def verkrijgAfstammelingen(naam: str):
  global oranje
  if naam in oranje:
    return oranje.get()
  return []
oranje = {
    'Beatrix': ['Willem-Alexander', 'Friso', 'Constantijn'],
    'Bernardo': ['Isabel'],
    'Bernhard': ['Isabella', 'Samuel', 'Benjamin'],
    'Carlos': ['Carlos Jr.'],
    'Christina': ['Bernardo', 'Nicolás', 'Juliana Jr.'],
    'Constantijn': ['Eloise', 'Claus-Casimir', 'Leonore'],
    'Emma': ['Wilhelmina'],
    'Floris': ['Magali', 'Eliane'],
    'Friso': ['Luana', 'Zaria'],
    'Irene': ['Carlos', 'Margarita', 'Jaime'],
    'Juliana': ['Beatrix', 'Margriet', 'Irene', 'Christina'],
    'Margarita': ['Julia'],
    'Margriet': ['Maurits', 'Bernhard', 'Pieter-Christiaan', 'Floris'],
    'Maurits': ['Anna', 'Lucas', 'Felicia'],
    'Pieter-Christiaan': ['Emma Jr.', 'Pieter'],
    'Wilhelmina': ['Juliana'],
    'Willem-Alexander': ['Amalia', 'Alexia', 'Ariane']
}

