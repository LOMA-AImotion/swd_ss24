# Frage nach Zahl k
# Gib alle gerade Zahlen von 1 bis k (inklusive) aus
k = int(input("Bis wohin zählen? "))
for laufvariable in range(1, k+1):
    if laufvariable % 2 == 0 : 
        print(laufvariable)