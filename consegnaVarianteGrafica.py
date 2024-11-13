import tkinter as tkint
from tkinter import messagebox

def generaNome():
    citta = cittaEntry.get()
    animale = bestiaEntry.get()
    
    if citta and animale:
        nomeBand = f"{citta} {animale}"
        messagebox.showinfo("Nome della Band", f"La tua band ora si chiama: {nomeBand}")
    else:
        messagebox.showwarning("ERRORE!!", "HEY BRODER FAI IL SERIO")

laraDiceh = tkint.Tk()
laraDiceh.title("GENERATORE NIUBBO PER NOMI BAND")

direttive = tkint.Label(laraDiceh, text="Inserisci i seguenti dettagli per generare il nome della tua band:")
direttive.pack(pady=20)


cittaGrafica = tkint.Label(laraDiceh, text="Dimmi dove sei nato hermano (solo nomi stupidini):")
cittaGrafica.pack()
cittaEntry = tkint.Entry(laraDiceh, width=40)
cittaEntry.pack()

bestiaGrafica = tkint.Label(laraDiceh, text="Inserisci il nome della tua bestia:")
bestiaGrafica.pack()
bestiaEntry = tkint.Entry(laraDiceh, width=40)
bestiaEntry.pack()

bottoneDellaNonna = tkint.Button(laraDiceh, text="DAJE", command=generaNome)
bottoneDellaNonna.pack(pady=20)

laraDiceh.mainloop()
