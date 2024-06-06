import tkinter
import tkinter.messagebox 
from functools import partial

haupt_fenster = tkinter.Tk()
haupt_fenster.title = "THI"
leinwand = tkinter.Canvas(haupt_fenster, width=400, height=300)
leinwand.grid(row=0, column=0, rowspan=3, columnspan=3)

def sag_zahl(button_zahl : int):
    tkinter.messagebox.showinfo("THI Quiz", f"Button {button_zahl} gedrückt")

# alternative: zaehler = 1
from functools import partial
for zeile in range(3):
    for spalte in range(3):
        label_text = str(spalte + zeile*3 + 1)
        label_zahl = spalte + zeile*3 + 1
        # alternative label_text = str(zaehler)
        button = tkinter.Button(haupt_fenster, text=label_text, 
                                width=10, height=5,
                                command = partial(sag_zahl, label_zahl))
        button.grid(column=spalte, row=zeile)
        # alternative zaehler += 1

haupt_fenster.mainloop()