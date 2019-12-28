from io import open

archivoTexto = open("archivo.txt", "r+")

#print(archivoTexto.readlines())
lineasTexto = archivoTexto.readlines()
lineasTexto[1]=" Esta línea ha sido incluida desde el exterior\n"
archivoTexto.seek(0)
archivoTexto.writelines(lineasTexto)
archivoTexto.close()



