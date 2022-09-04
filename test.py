nakup2= []
nakup=0
while True:
    nakup= input ("Co chces nakoupit?")
    if nakup=="nic":
        break
    nakup2.append (nakup)
    print (nakup2)
nakup2.sort ()
print (nakup2)
for polozka in nakup2:
    print ("- " + polozka)