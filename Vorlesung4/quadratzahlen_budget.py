# Gib ein Budget k an
# Jede Quadratzahl i*i kostet dich genau i Euro
# Gib an, welche Summe noch in das Budget k passt und die längste mögliche Seite

budget = int(input("Budget k? "))

restbudget = budget 
seite = 1
while restbudget >= (seite * seite):
    restbudget = restbudget - (seite * seite) 
    seite = seite + 1

# wir gehen eines zu weit mit seite, dann fliegen wir schon aus der Schleife
seite = seite - 1
ausgegeben = budget - restbudget
print("Mein Restbudget ist: ", restbudget)
print("Ausgegeben haben wir ", budget - restbudget)
print("Der Rest (berechnet) ist ", budget - ausgegeben)
print("Die längste Seite war ", seite)