import pickle

listaNombres = ["Pedro", "Ana", "María", "Isabel"]
ficheroBinario = open("listaNombres","wb")
pickle.dump(listaNombres,ficheroBinario)
ficheroBinario.close()