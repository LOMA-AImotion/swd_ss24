###
# ReLU(x) = max(x, 0)
# Liefert eine Implementierung der ReLU-Funktion
# und durchläuft alle Werte von -10 bis +10 darin
###

# 1. Die Funktionsdefinition mit Parameter x
def relu(x : int):
    if x < 0 : 
        return 0
    else:
        return x
    
# 2. Der Funktionsaufruf mit Argumenten von -10 bis +10
for wert in range(-10, 11):
    ergebnis = relu(wert)
    print(f"Relu({wert}) = {ergebnis}")


print("Relu('Karlheinz')", relu('Karlheinz'))