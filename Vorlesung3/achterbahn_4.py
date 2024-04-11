# Überprüfe ob eine Person größer als 150 cm groß ist
# um mit der Achterbahn zu fahren.

groesse = int(input("Wie groß bist du?"))
zielgroesse = 150

if groesse > zielgroesse:
    print("Viel Spaß")
elif groesse == zielgroesse:
    print("Gerade noch so")
    print("...")
else :
    print("Leider zu klein")
