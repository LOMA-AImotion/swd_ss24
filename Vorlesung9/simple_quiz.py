# eine einfache Übersicht, ein Label, 4 Buttons und dann die Rückfrage

import tkinter
import tkinter.messagebox

haupt_fenster = tkinter.Tk()
leinwand = tkinter.Canvas(haupt_fenster, width=400, height=300)
leinwand.grid(row=0, column=0, rowspan=3, columnspan=2)

frage = tkinter.Label(haupt_fenster, text="Welchen Typ kann man als Schlüssel für ein Dictionary nehmen?")
frage.config(font=("Arial 14"))
frage.grid(row=0, column=0, columnspan=2)

antwort_moeglichkeiten = [ "List", "int", "Set", "Dict"]
korrekte_antwort_index = 1
antwort_formatierung = ["A)", "B)", "C)", "D)"]

def frage_beantwortet(korrekter_index : int, gegebenen_index : int) -> None:
    if korrekter_index == gegebenen_index:
        tkinter.messagebox.showinfo("THI Quiz", "Korrekt!")
    else: 
        tkinter.messagebox.showerror("THI Quiz", "Versuch's nochmal!")
        
from functools import partial

for zeile in range(2):
    for spalte in range(2):
        antwort_index = spalte + zeile*2 
        label_text = f"{antwort_formatierung[antwort_index]} {antwort_moeglichkeiten[antwort_index]}"
        button = tkinter.Button(haupt_fenster, 
                                text=label_text, 
                                width=10, height=5,
                                command=partial(frage_beantwortet, 
                                                korrekte_antwort_index,
                                                antwort_index)
                                )
        button.grid(column=spalte, row=zeile + 1)

haupt_fenster.mainloop()