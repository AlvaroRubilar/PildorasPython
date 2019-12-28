import pickle


fichero = open("listaNombres","rb")
lista = pickle.load(fichero)
print(lista)
