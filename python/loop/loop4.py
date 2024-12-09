# Skriv et program, som for ligningen y=3x^2+6x+9 udskriver værdierne af y for x=0, x=1,x= 2, x=3 ... x=10. Ret det derefter programmet til at skrive ud for x=0,x=10,x=20,x=30...x=100.

for x in range(0,11):
    y = 3 * x * x + 6 * x + 9
    print(y)