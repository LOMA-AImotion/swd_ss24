import tkinter
import tkinter.messagebox 
haupt_fenster = tkinter.Tk()
def sag_hallo():
    print("Hallo SWD")
    tkinter.messagebox.showinfo("Hallo THI", "Hallo")

btn = tkinter.Button(haupt_fenster, text="Sag Hallo", command = sag_hallo)
btn.pack()
haupt_fenster.mainloop()