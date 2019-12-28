from io import open

archivoTexto = open("archivo.txt", "r")
print(archivoTexto.read())
archivoTexto.seek(11)
print(archivoTexto.read())

