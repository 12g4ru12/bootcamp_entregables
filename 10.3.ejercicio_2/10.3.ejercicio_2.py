"""
En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una
lista de elementos seleccionables, también debe de tener un label con el texto que queráis.
"""
import tkinter

window = tkinter.Tk()
label1 = tkinter.Label(window, text="lista de equipos seleccionables", fg="green")
label1.grid(column=0, row=0, sticky=tkinter.E, padx=20, pady=2)


lista = ['Barcelona.', 'Real Madrid.', 'Real Sociedad.', 'Atlético de Madrid.',
         'Villarreal.', 'Real Betis.', 'Osasuna.', 'Athletic Club.']

lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, height=10, width=30, listvariable=lista_items, bg='black', fg="white")
listbox.grid(column=0, row=1, sticky=tkinter.W, padx=20, pady=2)

tkinter.mainloop()
