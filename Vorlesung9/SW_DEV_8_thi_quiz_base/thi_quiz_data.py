# -*- coding: utf-8 -*-
"""
thi_quiz_data.py

Created on Tue Nov 23 22:27:53 2021

@author: 
"""
import os

def read_quiz_file(dateiname : str) -> list:
    # Öffne die Datei im Lese-Modus
    with open(dateiname, 'r', encoding="utf-8") as f:
        # Lese jede Zeile in der Datei
        zeilen = f.readlines()

    # Entferne Whitespaces (einschließlich '\n') am Ende jeder Zeile
    zeilen = [zeile.strip() for zeile in zeilen]

    anzahl_fragen = int(zeilen[0])
    akt_zeile = 1
    quiz_fragen = []
    for i in range(anzahl_fragen):
        naechste_frage = zeilen[akt_zeile]
        akt_zeile += 1 

        antwort_moeglichkeiten = []
        for i in range(4):
            naechste_antwort_moeglichkeit = zeilen[akt_zeile + i]
            if "CORRECT" in naechste_antwort_moeglichkeit:
                correct_index = i 
                naechste_antwort_moeglichkeit = naechste_antwort_moeglichkeit.replace("CORRECT:", "")
            antwort_moeglichkeiten += [naechste_antwort_moeglichkeit]

        akt_zeile += 4
        quiz_frage = (naechste_frage, antwort_moeglichkeiten, correct_index)
        quiz_fragen += [quiz_frage]
    # Jetzt enthält die Liste "words" alle Wörter aus der Datei
    return quiz_fragen


if __name__ == "__main__":
    quiz_file_name = os.path.join(os.path.dirname(__file__), 'quiz_functions.txt')
    quizzes = read_quiz_file(quiz_file_name)
    print(quizzes)