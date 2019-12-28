from io import open

archivoTexto = open("archivo.txt", "r")

#archivoTexto.seek(11)
print(archivoTexto.read(11))

