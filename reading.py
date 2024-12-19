filename = 'data.txt'

# Interpretatie 1
with open(filename, 'r') as f:
    headers = f.readline().strip().split(',')
    
    # Lege dict
    d = {h:[] for h in headers}
    
    # Per regel
    for line in f.readlines():
        # Lees de values
        values = line.strip().split(',')

        # Per header-value paar:
        # Voeg de value toe aan de lijst van header in de dict
        for h,v in zip(headers,values):
            d[h].append(v)


print(d)


# Interpretatie 2
with open(filename, 'r') as f:
    # Lees eerste regel
    headers = f.readline().strip().split(',')

    dicts = []
    # Lees de ander regels
    for line in f.readlines():
        values = line.strip().split(',')
                
       
        d = dict(zip(headers, values))
        
        # Voeg de dict toe aan de lijst van dictionairies
        dicts.append(d)
    
    dicts = [dict(zip(headers, line.strip().split(','))) for line in f.readlines()]

print(dicts)


# Filter op een variable
for d in dicts:
    if d['var3'] == '"Y"':
        print(d)

print(list(filter(lambda d: d['var1'] == '"Y"', dicts)))
