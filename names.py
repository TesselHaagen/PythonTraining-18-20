# Initialize the empty list
names = []

# Manier 1
while True:
    name = input("Please provide a name: ")
    if name == '':
        break

    names.append(name)

# Manier 2, if en else gebruiken
while True:
    name = input("Please provide a name: ")
    if name: 
        names.append(name)
    else:
        break

# Zelfde als manier 1, maar een lege string wordt als False gezien door Python, 
# dus je hoeft dit niet gelijk te stellen
while True:
    name = input("Please provide a name: ")
    if not name: 
        break
    names.append(name)

names.sort() # .sort() gebruikt de method van de lijst, het modificeert de lijst
names_sorted = sorted(names) # sorted() is een build-in functie, maakt een nieuwe lijst aan

for name in names:
    print(name)