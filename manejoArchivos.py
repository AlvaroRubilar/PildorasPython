from io import open

archivoTexto = open("archivo.txt", "r")
lineasTexto = archivoTexto.readlines()
archivoTexto.close()
print(lineasTexto)
