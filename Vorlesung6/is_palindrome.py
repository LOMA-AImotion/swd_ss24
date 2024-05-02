# Definiere eine Funktion, die mit Berücksichtung von
# Groß- und Kleinschreibung feststellt, ob eine Zeichenkette
# ein Palindrom ist oder nicht

def is_palindrome(zeichenkette : str) -> bool: 
    # ist zeichenkette rückwärts und vorwärts das Gleiche?
    return zeichenkette[::-1] == zeichenkette

def is_palindrome2(zeichenkette : str) -> bool: 
    # mit For-Schleife
    for i in range(0, len(zeichenkette) // 2) : 
        # sind Zeichen i und Zeichen len - i ungleich? 
        if zeichenkette[i] != zeichenkette[len(zeichenkette) - 1 - i]:
            return False
    return True

zeichenkette = input("Zeichenkette? ")
print(f"{zeichenkette} ist ein Palindrom?`{is_palindrome(zeichenkette)}")
print(f"{zeichenkette} ist ein Palindrom?`{is_palindrome2(zeichenkette)}")