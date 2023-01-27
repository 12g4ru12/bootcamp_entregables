"""
En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción
que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.
Al principio no tiene que haber una opción seleccionada.
"""

import tkinter

window = tkinter.Tk()
window.title("OpenBootcamp")

selected = tkinter.StringVar()
rbutton1 = tkinter.Radiobutton(window, text='Option 1', value='1', variable=selected, fg="blue")
rbutton2 = tkinter.Radiobutton(window, text='Option 2', value='2', variable=selected, fg="blue")
rbutton3 = tkinter.Radiobutton(window, text='Option 3', value='3', variable=selected, fg="blue")
rbutton4 = tkinter.Radiobutton(window, text='Option 4', value='4', variable=selected, fg="blue")

rbutton1.grid(column=0, row=1, padx=20, pady=3)
rbutton2.grid(column=0, row=2, padx=20, pady=3)
rbutton3.grid(column=0, row=3, padx=20, pady=3)
rbutton4.grid(column=0, row=4, padx=20, pady=3)


def restart(event):
    selected.set('')


botonrestart = tkinter.Button(window, text='» Reset »', fg="white", bg="blue")
botonrestart.bind('<Button-1>', restart)
botonrestart.grid(column=1, row=4, padx=20, pady=3)

window.mainloop()
