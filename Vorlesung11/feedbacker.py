# Ein Beispiel für Polymorphismus

# Die Basisklasse Feedbacker
class Feedbacker: 
    def __init__(self) -> None:
        pass

    def positive(self, message: str) -> None:
        pass 

    def negative(self, message: str) -> None:
        pass 

# Für Devices, die kein Tkinter unterstützen
class PrintFeedbacker(Feedbacker):
    # hier überschreibe ich die Methode "positive" aus der Basisklasse Feedbacker
    def positive(self, message: str) -> None:
        print(message)

    def negative(self, message: str) -> None:
        print(message)

# Für Devices, die Tkinter unterstützen
import tkinter
from tkinter import messagebox

class TkinterFeedbacker(Feedbacker):
    def positive(self, message: str) -> None:
        tkinter.messagebox.showinfo("THI-SWD", message)

    def negative(self, message: str) -> None:
        tkinter.messagebox.showerror("THI-SWD", message)


if __name__ == "__main__":
    f:Feedbacker = None
    use_tkinter = False
    if use_tkinter:
        f = TkinterFeedbacker()
    else:
        f = PrintFeedbacker()

    f.positive("Hast du gut gemacht!")
    f.negative("Probier's nochmal")