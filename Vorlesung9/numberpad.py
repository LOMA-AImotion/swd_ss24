import tkinter 
haupt_fenster = tkinter.Tk()
haupt_fenster.title = "THI"
leinwand = tkinter.Canvas(haupt_fenster, width=400, height=300)
leinwand.grid(row=0, column=0, rowspan=3, columnspan=3)
# alternative: zaehler = 1
for zeile in range(3):
    for spalte in range(3):
        label_text = str(spalte + zeile*3 + 1)
        # alternative label_text = str(zaehler)
        button = tkinter.Button(haupt_fenster, text=label_text, width=10, height=5)
        button.grid(column=spalte, row=zeile)
        # alternative zaehler += 1

haupt_fenster.mainloop()