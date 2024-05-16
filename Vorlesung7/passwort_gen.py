import random 
from string import punctuation

from thi_swd import lesen_woerter_von_datei

# Verwendung der Funktion
nomen = lesen_woerter_von_datei('nomen.txt')
adjektive = lesen_woerter_von_datei("adjektive.txt")
print(nomen)
print(adjektive)

anzahl_pw = int(input("Wie viele Passwörter benötigst du?"))
for i in range(anzahl_pw):
    print(f"Passwort #{i+1}") 
    # wähle Nomen
    # 1. mit Choice
    nomen_wahl = random.choice(nomen)
    # 2. mit Index und zufälligem Integer
    #nomen_index = random.randint(0, len(nomen) - 1)
    #nomen_wahl = nomen[nomen_index]
    
    # wähle Adjektiv
    adjektiv_wahl = random.choice(adjektive)
    # wähle Zahl
    zahl_wahl = random.randint(0, 100)

    # wähle Sonderzeichen
    sonderzeichen_wahl = random.choice(punctuation)

    # kombiniere und gebe aus 
    bestandteile = [adjektiv_wahl, nomen_wahl, str(zahl_wahl), sonderzeichen_wahl]
    random.shuffle(bestandteile)

    passwort = bestandteile[0] + bestandteile[1] + bestandteile[2] + bestandteile[3]
    #print(bestandteile)
    print(passwort)
