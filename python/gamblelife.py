import random
y = 6
skud = random.randint(1, y)
ssp = random.randint(1, 3)
forsøg = 0

if  ssp == 1:
        ssp = 'sten'

elif  ssp == 2:
        ssp = 'saks'

else:
        ssp = 'papir'



print ('Sten, Saks, Papir')
ssp1 = input()

while ssp1.lower() == ssp.lower():
        ssp = random.randint(1, 3)

        if  ssp == 1:
               ssp = 'sten'
    
        elif  ssp == 2:
               ssp = 'saks'
            
        else:
               ssp = 'papir'

        print('Sten, Saks, Papir')
        ssp1 = input()
    
if ssp1.lower() == 'sten' and ssp.lower() == 'saks':
        print('Jeg starter')
        x = 1

elif ssp1.lower() == 'saks' and ssp.lower() == 'papir':
        print('Jeg starter')
        x = 1

elif ssp1.lower() == 'papir' and ssp.lower() == 'sten':
        print ('Jeg starter')
        x = 1

elif ssp1.lower() == 'sten' and ssp.lower() == 'papir':
        print('Du starter')
        x = 0

elif ssp1.lower() == 'saks' and ssp.lower() == 'sten':
        print('Du starter')
        x = 0

else:
        print('Du starter')
        x = 0

while skud != 1:
        forsøg += 1
        y -= 1
        x += 1
        skud = random.randint(1, y)
        

if skud == 1 and x == 0:
        forsøg += 1
        print(f'Game Over {forsøg} attempts')

elif skud == 1 and x == 2:
        forsøg += 1
        print(f'Game Over {forsøg} attempts')

elif skud == 1 and x == 4:
        forsøg += 1
        print(f'Game Over {forsøg} attempts')
        

elif skud == 1 and x == 1:
        forsøg += 1 
        print(f'You Won {forsøg} attempts')


elif skud == 1 and x == 3:
        forsøg += 1 
        print(f'You Won {forsøg} attempts')


elif skud == 1 and x == 5:
        forsøg += 1 
        print(f'You Won {forsøg} attempts')