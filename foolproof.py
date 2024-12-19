

def foolproof_input(lower_bound, upper_bound):
    """
    Function to ask the user for a number between two bounds.

    Args:
    - lower_bound (int): the lower bound, the number must be higher
    - lower_bound (int): the higher bound, the number must lower
    """
    while True:        
        response = input(f'Give me a number between {lower_bound} and {upper_bound}: \n')
        
        try:
            number = int(response) # -> hier kan een error door komen

            if lower_bound <= number <= upper_bound:
                # Als het getal tussen de twee bounds zijn, break de loop
                break
            else:
                print(f'{number} is not between {lower_bound} and {upper_bound}.')

        except ValueError:
            print(f'"{response}" is not a number.')

    
    return number



if __name__ == "__main__":
    number = foolproof_input(1, 10)
    print(f'The number you entered ({number}) is OK')