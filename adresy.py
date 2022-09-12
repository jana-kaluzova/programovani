with open ("adresy.csv",encoding="utf-8") as soubor:
    n=[]
    for radek in soubor:
        seznam= radek.split (",")
        if seznam[2] not in n:
            n.append (seznam[2])
n.sort()          
for ulice in n:
    print ("-",ulice)


print ("pocet ulice je:",len (n))
