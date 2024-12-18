# Ask the user for a year
year = int(input('Give a year: \n'))

# Check if the year is a leapyear
leapyear = 'a' if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 'NOT a'

# Print the outcome
print(f"{year} is {leapyear} leapyear")