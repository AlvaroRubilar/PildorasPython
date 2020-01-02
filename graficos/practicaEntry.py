from tkinter import *

raiz = Tk()
miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()
cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=0,column=1,padx=10,pady=10)
cuadroNombre.config(fg="blue",justify="center")
cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1,column=1,padx=10,pady=10)
cuadroPass.config(fg="blue",justify="center",show="*")
cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=2,column=1,padx=10,pady=10)
cuadroDireccion.config(fg="blue",justify="center")

nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="w",padx=10,pady=10)

passLabel = Label(miFrame, text="Contraseña: ")
passLabel.grid(row=1, column=0, sticky="w",padx=10,pady=10)

direccionLabel = Label(miFrame, text="Dirección de Casa: ")
direccionLabel.grid(row=2, column=0, sticky="w",padx=10,pady=10)
raiz.mainloop()
