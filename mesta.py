with open ("mesta.csv", encoding= "utf-8") as soubor:
    pocet_mest_v_kraji = {
        # "Plzeňský kraj": 50,
        # "Moravskoslezský kraj": 300,
    }
    m=0
    p=0
    for radek in soubor:
        radek= radek.split (",")
        if radek[0] in pocet_mest_v_kraji:
            pocet_mest_v_kraji[radek[0]] = pocet_mest_v_kraji[radek[0]] + 1
        else:
            pocet_mest_v_kraji[radek[0]] = 1
        #if radek [0] == "Moravskoslezský kraj":
        #    m = m + 1
        #elif radek[0] == "Plzeňský kraj":
        #    p= p+1
#print (m, "je pocet mest v moravskoslezskem kraji")
print(pocet_mest_v_kraji)
