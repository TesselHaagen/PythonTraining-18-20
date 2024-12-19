# Volgens de opdracht
with open('ca-500.csv', 'r') as f:
    # Lees de headers
    headers = f.readline().strip("\n").split(';')
    
    # Lees de lines
    for line in f.readlines():
        columns = line.strip("\n").split(';')
        d = dict(zip(headers, columns))

        # Print firstname, lastname, city en email als city Montreal is
        print(d)
        if d['city'] == 'Montreal':
            print(f"{d['first_name']} {d['last_name']} {d['city']} {d['email']}")
            
# Netter
with open('ca-500.csv', 'r') as f:
    # Lees de headers
    headers = f.readline().strip("\n").split(';')
    
    # Lees de lines
    filtered_lines = []
    for line in f.readlines():
        columns = line.strip("\n").split(';')
        d = dict(zip(headers, columns))

        # Print firstname, lastname, city en email als city Montreal is
        if d['city'] == 'Montreal':
            filtered_lines.append(d)


for d in filtered_lines:
    print(f"{d['first_name']}, {d['last_name']}, {d['city']}, {d['email']},")
