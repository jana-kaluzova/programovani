from random import randrange

print ("Ahoj, myslim si cislo, zkus ho uhadnout")
cislo= randrange (1,100)
hcislo=0
while hcislo!=cislo:
    hcislo= int(input ("Na jake cislo myslim?\n"))
    if hcislo==cislo:
        print ("vyhral jsi!")
        break
    elif hcislo <cislo:
        print ("Tohle neni spravne cislo, zkus hadat vyssi hodnoty!")
    else:
        print ("Tohle neni spravne cislo, zkus hadat nizsi cislo!")



