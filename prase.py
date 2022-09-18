# Umi prase letat?
# ================

# Zadani:

# Napis hru "Umi prase letat?", ktera bude fungovat nasledovne:

# 1) Zvirata a jejich vlastnosti budou ulozeny ve slovniku, kde klic bude jmeno zvirete a hodnota bude seznam retezcu.
#    Retezce budou napriklad:
#      - leta
#      - plave
#      - savec
#      - zobak
#      - ocas
#      - ...
# 2) Na zacatku hry pocitac nahodne vybere jedno ze zvirat a vypise jej.
# 3) Uzivateli se zobrazi seznam vsech vlastnosti ktere hra podporuje, aby vedel z ceho vybirat.
# 4) Uzivatel ma za ukol vybrat prave takove vlastnosti, ktere zvire skutecne ma. Vyber probiha tak,
#    ze uzivatel ve funkci input zada primo dany retez (napriklad "leta", nebo "plave").
# 5) Pokud je uzivatel hotov, zada "hotovo" a program vyhodnoti, jestli zadane vlastnosti skutecne patri zvireti.
# 6) Za kazdou pravdivou vlastnost prida uzivateli bod, za kazdou nepravdivou bod ubere.
# 7) Hra se opakuje dokola od bodu 2) dokud uzivatel nezada "konec".
import random
print ("Vitej ve hre \"Umi prase letat?\"")

prase= {
    "kocka":["savec","ocas","eu","zuby","srst"],
    "sykorka":["leta","vejce","eu","ocas"],
    "mravenec":["les","vejce","spolecenstvi","eu"]
}
print ("Pocitac vybral toto zvire:")

vyber= random.choice(list(prase.keys()))
print (vyber)

seznam= []
for polozka in prase.values ():
    for polozka2 in polozka:
        if polozka2 not in seznam:
            seznam.append (polozka2)

print (seznam)
body=0
ODPOved= input ("vyber jednu nebo vice vlastnosti, ktere ma dane zvire")
odpoved2= ODPOved.split ()
hodnota= prase[vyber]
for odpoved3 in odpoved2:
    if odpoved3 in hodnota:
        body= body+1
    else:
        body= body-1
print ("tvuj stav bodu je:", body)







