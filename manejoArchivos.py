from io import open

archivoTexto = open("archivo.txt", "r")

archivoTexto.seek(len(archivoTexto.read())/2)
print(archivoTexto.read())


