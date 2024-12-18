# Ask the age to the user
t = int(input('What is your age? '))

# Check and print the lifestage for different ages
if t < 2:
    print('Baby')
elif t < 4:
    # Don't need to use 2 here again, since that is alredy checked
    print('Toddler')
elif t < 13:
    print('Kid')
elif t < 20:
    print('Teenager')
elif t < 65:
    print('Adult')
else:
    print('Elder')

# In a one-liner
lifestage = 'Baby' if t < 2 else 'Toddler' if t < 4 else 'Kid' if t < 13 else 'Teenager' if t < 20 else 'Adult' if t < 65 else 'Elder'
print(lifestage)