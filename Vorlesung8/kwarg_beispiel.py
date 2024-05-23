def flaeche(breite : float, hoehe : float, preis : float = 5.0, tiefe : float = 10.0):
    return breite * hoehe * preis * tiefe

print(flaeche(10, 10))
print(flaeche(10, 10, 8))
print(flaeche(10, 10, preis=7.5))
print(flaeche(10, 10, tiefe=5.0))