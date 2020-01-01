from tkinter import *

raiz = Tk()
raiz.title("Ventana de pruebas")
# raiz.resizable(True, 0)
raiz.iconbitmap("retriever.ico")
raiz.geometry("650x350")
raiz.config(bg = "#6666ff")
miFrame = Frame()
miFrame.pack(fill="y", expand="True")
miFrame.config(bg="#e6e6ff")
miFrame.config(width="650",height="350")
raiz.mainloop()
