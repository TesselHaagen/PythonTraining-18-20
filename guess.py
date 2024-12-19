import random
secret_number = random.randint(1,100)

count = 0
while True:
    # ASk the user for input
    guess = int(input('Guess a number between 1 and 100: '))
    count += 1 # Increase the count of guesses

    if guess < secret_number:
        # If the guess is lower, say the user needs to guess higher
        print('Higher..')
    elif guess > secret_number:
        # Else f the guess is higher, say the user needs to guess lower
        print('Lower..')
    else:
        # Otherwise it must be equal, the user won the game
        print(f'Correct! Guessed in {count} times')
        break