from io import open
archivoTexto = open("archivo.txt", "r")
texto = archivoTexto.read()
archivoTexto.close()
print(texto)
