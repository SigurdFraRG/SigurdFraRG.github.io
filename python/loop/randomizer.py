import random
r = random.randint(1, 20)
forsøg = 0


print('Jeg tænker på et tal fra 1 til 20 prøv at se om du kan gætte det')
tal = input()

while tal > r:
    print('Mindre')
    tal = input()
    forsøg += 1

while tal < r:
    print('Større')
    tal = input()
    forsøg += 1

if tal == r:
    forsøg += 1
    print(f'Korrekt og du brugte {forsøg} forsøg')
