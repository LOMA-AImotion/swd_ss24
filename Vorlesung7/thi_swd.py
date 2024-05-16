def greet():
    print("Servus SWD")

def my_double(x : float) -> float:
    return 2*x

def lesen_woerter_von_datei(dateiname : str) -> list:
    # Öffne die Datei im Lese-Modus
    with open(dateiname, 'r', encoding="utf-8") as f:
        # Lese jede Zeile in der Datei
        words = f.readlines()

    # Entferne Whitespaces (einschließlich '\n') am Ende jeder Zeile
    words = [word.strip() for word in words]

    # Jetzt enthält die Liste "words" alle Wörter aus der Datei
    return words
