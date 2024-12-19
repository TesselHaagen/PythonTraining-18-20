import re
text = """Van 2021 tot en met 2023 zijn 95 zorgmedewerkers ontslagen omdat ze medicijnen uit de voorraadkast hadden meegenomen. Dat blijkt uit cijfers van de Inspectie Gezondheidszorg en Jeugd.

In ziekenhuizen gebeurde dit het vaakst. In 50 procent van alle ontslagen in ziekenhuizen was dit de reden voor het ontslag. In verpleeghuizen en in de thuiszorg gold dit voor 15 procent van alle ontslagen.

De meldingen erover bij de inspectie gaan vaak over het meenemen van benzodiazepines. Dat zijn zwaar verslavende medicijnen die worden voorgeschreven bij slaapproblemen of paniekaanvallen. Ook worden pijnstillers als tramadol of opiaten zoals morfine of oxycodon meegenomen.

'Zorgaanbieder heeft het vaak niet door'
Of dit het topje van de ijsberg is, wil de inspectie niet zeggen. "We denken dat het er nog wel meer zijn. Veel zorgpersoneel vindt het gebruikelijk om medicijnen te gebruiken en de zorgaanbieder heeft het vaak niet door", zegt Janet Helder, hoofdinspecteur van de Inspectie Gezondheidszorg en Jeugd.

In hoeveel gevallen er sprake is van het meenemen van een eenmalige tablet of van het stelen voor langdurig gebruik is niet duidelijk. Wel zijn deze middelen een enkele keer gestolen om erin te handelen. Ziekenhuizen maken vaak geen onderscheid; in bijna alle gevallen wordt de medewerker die wordt betrapt, ontslagen."""

text = re.sub('[^a-z\s]', '', text.lower())
uniques = set(text.split())

# One liner
counts = {word: text.count(word) for word in uniques}


for word, n in counts.items():
    print(word, n)

# Print in one liner
print('\n'.join([f'{word}: {n}' for word, n in counts.items()]))