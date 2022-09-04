print('Slyšela jsem tuto básničku:')
print()

with open('basnicka.txt', encoding='utf-8') as soubor:
    for radek in soubor:
        print('    ' + radek[0:-1])

print()
print('Jak se ti líbí?')