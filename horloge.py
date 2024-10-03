from tkinter import *
from tkinter.ttk import *
 
# importe la function strftime pour récuperer l'heure du système
from time import strftime
 
# crée la fenêtre tinkter
root = Tk()
root.title('Clock')
 
# Fonction pour afficher l'heure sur le label
 
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)
 
 
# juste du graphique pour moins péter mes yeux lol ça fait mal le blanc quand il fait sombre dans ma chambre ptdr
lbl = Label(root, font=('calibri', 40, 'bold'),
            background='purple',
            foreground='white')
 
#place la fenêtre au centre de l'écran
lbl.pack(anchor='center')
time()
 
mainloop()
