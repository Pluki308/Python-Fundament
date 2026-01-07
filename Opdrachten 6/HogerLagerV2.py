import random

begin,eind=0,101
geraden=1
while True:
    computergok=random.randint(begin+1,eind-1)
    print(f"Computer denkt {computergok} tussen {begin} en {eind}")
    vraag = input("Is het goed (g), hoger (h) of lager (l) ").lower()

    if vraag == "g" or vraag=='goed':
        geraden+=1
        print(f'🎉 de computer heeft het in {geraden} keer geraden!')
        break

    elif vraag == "h" or vraag=='hoger':
        geraden+=1
        begin=computergok
        

    elif vraag == "l" or vraag=='lager':
        geraden+=1
        eind=computergok
    else:
        print('ongeldig')
        

print(f'🎉 de computer heeft het in {geraden} keer geraden!')
