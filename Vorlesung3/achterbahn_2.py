# Überprüfe ob eine Person größer als 150 cm groß ist
# um mit der Achterbahn zu fahren.

groesse = int(input("Wie groß bist du?"))
zielgroesse = 150

if groesse > zielgroesse:
    print("Viel Spaß")

if groesse < zielgroesse:
    print("Leider zu klein")

if groesse == zielgroesse: 
    print("Gerade noch so")