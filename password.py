import random 

numbers = '0123456789'
low_chars = 'abcdefghijklmnopqrstuvwxyz'
cap_chars = low_chars.upper()
specials = '?!@#,.'

all_together = [numbers, low_chars, cap_chars, specials]


# Manier 1:
password = []
n = 2

random.shuffle(all_together)
for chars in all_together:
    k = random.randint(1,n+1)
    password.extend(random.choices(chars, k=k))
    n -= k-1

random.shuffle(password)
print(''.join(password))


# Manier 2:
p1 = random.choices(low_chars, k=1)
p2 = random.choices(cap_chars, k=1)
p3 = random.choices(specials, k=1)
p4 = random.choices(numbers, k=1)
p5 = random.choices(numbers+low_chars+cap_chars+specials, k=2)

password = list(p1+p2+p3+p4+p5)
random.shuffle(password)
print(''.join(password))
