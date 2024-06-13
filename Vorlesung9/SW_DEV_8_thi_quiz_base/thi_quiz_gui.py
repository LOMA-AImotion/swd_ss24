# -*- coding: utf-8 -*-
"""
thi_quiz_gui.py

Created on Tue Nov 23 22:27:53 2021

@author: 
"""
# eine einfache Übersicht, ein Label, 4 Buttons und dann die Rückfrage

import tkinter
import tkinter.messagebox
import os 

from functools import partial
from thi_quiz_data import read_quiz_file

haupt_fenster = tkinter.Tk()
leinwand = tkinter.Canvas(haupt_fenster, width=400, height=300)
leinwand.grid(row=0, column=0, rowspan=3, columnspan=2)

frage_label = tkinter.Label(haupt_fenster, text="Welchen Typ kann man als Schlüssel für ein Dictionary nehmen?")
frage_label.config(font=("Arial 14"))
frage_label.grid(row=0, column=0, columnspan=2)

antwort_moeglichkeiten = [ "List", "int", "Set", "Dict"]
korrekte_antwort_index = 1
antwort_formatierung = ["A)", "B)", "C)", "D)"]

def frage_beantwortet(korrekter_index : int, gegebenen_index : int) -> None:
    # ohne "global" würden wir eine neue lokale Variable anlegen
    # so sagen wir Python, dass es die globale überschreiben darf und soll 
    global aktueller_fragen_index
    if korrekter_index == gegebenen_index:
        tkinter.messagebox.showinfo("THI Quiz", "Korrekt!")
        aktueller_fragen_index = aktueller_fragen_index + 1
        # bei quizzes *lesen* wir nur eine globale Variable - da brauchen wir kein global!
        # quizzes ist auch eine globale Variable aus dem Hauptprogramm
        if aktueller_fragen_index == len(quizzes):
            aktueller_fragen_index = 0

        naechste_frage = quizzes[aktueller_fragen_index]
        ueberschreibe_frage(naechste_frage)
    else: 
        tkinter.messagebox.showerror("THI Quiz", "Versuch's nochmal!")

buttons = []
for zeile in range(2):
    for spalte in range(2):
        antwort_index = spalte + zeile*2 
        label_text = f"{antwort_formatierung[antwort_index]} {antwort_moeglichkeiten[antwort_index]}"
        button = tkinter.Button(haupt_fenster, 
                                text=label_text, 
                                height=5,
                                command=partial(frage_beantwortet, 
                                                korrekte_antwort_index,
                                                antwort_index)
                                )
        button.grid(column=spalte, row=zeile + 1)
        buttons.append(button)

def ueberschreibe_frage(quizfrage : tuple):
    frage, antworten, korrekter_index = quizfrage 
    frage_label.config(text = frage)
    for index, antwort_moeglichkeit in enumerate(antworten):
        print(index, antwort_moeglichkeit)
        buttons[index].config(text = antwort_moeglichkeit)

    for index, btn in enumerate(buttons): 
        btn.config(command = partial(frage_beantwortet, korrekter_index, index) )

aktueller_fragen_index = 0

if __name__ == "__main__":
    # lade Fragen
    quiz_file_name = os.path.join(os.path.dirname(__file__), 'quiz_functions.txt')
    quizzes = read_quiz_file(quiz_file_name)

    # zeige die erste Frage an
    erste_frage = quizzes[0]
    ueberschreibe_frage(erste_frage)
    

    # wechsle bei korrekter Antwort auf die nächste Frage
    haupt_fenster.mainloop()



