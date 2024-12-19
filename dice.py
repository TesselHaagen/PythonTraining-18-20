import random

# Eerste opdracht

# Create 5 dices
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
dice3 = random.randint(1,6)
dice4 = random.randint(1,6)
dice5 = random.randint(1,6)

print(f'Sum of the dice are {dice1+dice2+dice3+dice4+dice5}')
# Check for Yathzee

if dice1 == dice2 == dice3 == dice4 == dice5:
    print('Yathzee!')
else:
    print('No Yathzee')



# Met een While loop and list
dice = []
for i in range(5):
    dice.append(random.randint(1,6))

print(f'Sum of the dice are {sum(dice)}')

# Check for Yathzee! list version
yathzee = 'Yathzee'
for i in range(1,5):
    if dice[0] != dice[1]:
        yathzee = 'No Yathzee'
        break

print(yathzee)

# Check for Grote straat
grote_straat = 'Grote straat' if all([i in dice for i in range(2,6)]) and (1 in dice or 6 in dice) else 'No Grote Straat'
print(grote_straat)
