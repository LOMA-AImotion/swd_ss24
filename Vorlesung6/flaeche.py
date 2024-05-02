def flaeche(breite : int, hoehe : int) -> int:
    flaecheninhalt = breite * hoehe
    print("In Funktion Flaeche")
    #print(flaecheninhalt)
    return flaecheninhalt

print("Hallo ")
print(f"Die Flache (5, 100) ist: {flaeche(5, 100)}")
a = flaeche(10, 10)
print(a)