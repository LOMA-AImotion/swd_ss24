# Nimm eine Reihe von Messwerten
messwerte = [0, 1, 4, 5, 7, 8]

# gib die Zeitdifferenzen in Minuten zurück
# z.B. [1, 3, 1, 2, 1]

# messwerte[i+1]
# 1. über for-Schleife
differenzen = []
for i in range(1, len(messwerte)): 
    differenz = messwerte[i] - messwerte[i-1]
    differenzen.append(differenz)

print(differenzen)

# 2. Als list comprehension
# [ ausdruck for laufvariable in iterable if bedingung]
differenzen2 = [messwerte[i] - messwerte[i-1] for i in range(1, len(messwerte))]

print(differenzen2)

# 3. mit Index 0 als Startwert
differenzen3 = [messwerte[i] - messwerte[i-1] for i in range(0, len(messwerte))]
print(differenzen3)