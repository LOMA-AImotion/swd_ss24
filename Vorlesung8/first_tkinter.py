import tkinter 
haupt_fenster = tkinter.Tk()
haupt_fenster.title = "THI"
leinwand = tkinter.Canvas(haupt_fenster, width=800, height=600)
leinwand.grid(row=0, column=0, rowspan=2, columnspan=2)

label = tkinter.Label(haupt_fenster, text="Meine erste GUI")
#label.pack()
label.grid(column=0, row=0)

button = tkinter.Button(haupt_fenster, text="OK")
button.grid(row=0, column=1)
#button.pack()
button2 = tkinter.Button()
haupt_fenster.mainloop()