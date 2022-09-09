datum= input ("zadej datum?")
with open ("svatky.txt", encoding= "utf-8") as soubor:
    for radek in soubor:
        rozdeleni= radek.split (";")
        if datum == rozdeleni[0]:
            print ("tvoje jmeno je:",rozdeleni [1])
            break

import time
print (time.localtime ())
mesic= str(time.localtime().tm_mon)
den= str(time.localtime ().tm_mday)
mesicden= mesic+"."+den