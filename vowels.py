text = input("Give some text: \n").lower()

# Manier 1, gaat 6 keer over de hele tekst, wel minder memory
vowels = 'aeiouy' 
total = 0
for v in vowels:
    v_count = text.count(v)
    total += v_count
    print(f'The vowel {v} occurs {v_count} times.')

print(f'Your text has a total of {len(text)} characters')
print(f'Your text has a total of {total} vowels')


# Manier 2, gaat 1 keer over de hele tekst, meer memory
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0
y_count = 0

for char in text:
    if char == 'a':
        a_count += 1
    if char == 'e':
        e_count += 1
    if char == 'o':
        o_count += 1
    if char == 'u':
        u_count += 1
    if char == 'i':
        i_count += 1
    if char == 'y':
        y_count += 1

print(f"The vowel 'a' occurs {a_count} times.")
print(f"The vowel 'e' occurs {e_count} times.")
print(f"The vowel 'o' occurs {o_count} times.")
print(f"The vowel 'u' occurs {u_count} times.")
print(f"The vowel 'i' occurs {i_count} times.")
print(f"The vowel 'y' occurs {y_count} times.")

print(f'Your text has a total of {len(text)} characters')
print(f'Your text has a total of {a_count+e_count+o_count+u_count+i_count+y_count} vowels')

# Manier 3, Datastructuren gebruiken
counts = {v: text.count(v) for v in vowels}
print('\n'.join([f'The vowel {v} occurs {c} times.' for v,c in counts.items()]))
print(f'Your text has a total of {len(text)} characters')
print(f'Your text has a total of {sum(list(counts.values()))} vowels')