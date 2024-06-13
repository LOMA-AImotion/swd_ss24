class Flasche:
    def __init__(self, inhalt, typ, fuellstand) -> None:
        self.inhalt = inhalt
        self.typ = typ
        self.fuellstand = fuellstand

    def __repr__(self) -> str:
        return f"{self.inhalt} | {self.typ} : {self.fuellstand*100} %"
    
    def ist_quasi_leer(self) -> bool:
        if self.fuellstand <= 0.05:
            return True
        else: 
            return False

if __name__ == "__main__":
    flasche_instanz_1 = Flasche("Löschlösung", "Sprühflasche", 0.95)
    flasche_instanz_2 = Flasche("Spezi", "Glasflasche", 0.05)

    for flasche in [flasche_instanz_1, flasche_instanz_2]:
       print(flasche)
       print(f"Ist quasi leer? {flasche.ist_quasi_leer()}")
    