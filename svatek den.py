import time
mesic= str(time.localtime().tm_mon)
den= str(time.localtime ().tm_mday)
mesicden= mesic+"."+den
with open ("svatky.txt", encoding= "utf-8") as soubor:
    for radek in soubor:
        rozdeleni= radek.split (";")
        if mesicden== rozdeleni[0]:
            print (rozdeleni[1])