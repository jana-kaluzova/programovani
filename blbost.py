seznam = ['jahoda', 'boruvka', 'kiwi', 'banan']
while True:
    noveslovo= input ("zadej prikaz\n")
    if noveslovo[0]=="+":
        if noveslovo[1:] in seznam:
            print ("tohle slovo jiz je v seznamu")
        else:
            seznam.append(noveslovo[1:])
    elif noveslovo[0]=="-":
        if noveslovo[1:] in seznam:
            seznam.remove(noveslovo[1:])
        else: 
            print (noveslovo +" neni v seznamu")
    elif noveslovo[0]=="?":
        pocet= seznam.count(noveslovo[1:])
        print (pocet)
        if pocet==0:
            print ("neni v seznamu")
        else:
            print ("je v seznamu")
    elif noveslovo=="konec":
        break
    print (seznam)
