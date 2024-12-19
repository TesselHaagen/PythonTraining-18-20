import math
import math as m # De gehele library importeren
from math import pi # Alleen pi geimporteerd

r = float(input("Wat is de straal van de cirkel?"))

# Dit is hetzelfde als de vorige regel, alleen dan in stappen:
radius = input("Wat is de straal van de cirkel?")
r = float(radius)

# Het hangt er van af hoe je hebt geimporteerd welke pi je gebruikt
area = math.pi * r**2 # math.pi * math.pow(r,2)
area = m.pi * r**2
area = pi * r**2
circumference = 2 * math.pi * r

print(area, circumference)