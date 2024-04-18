gaeste = input("Wen einladen? <niemand> um aufzuhalten")
gaeste_liste = []
while gaeste != "niemand":
    gaeste_liste.append(gaeste)
    gaeste = input("Wen einladen? <niemand> um aufzuhalten")

print("Alle Gäste:", gaeste_liste)