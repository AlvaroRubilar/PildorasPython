import math as m

print("Programa de cálculo de raiz cuadrada")
numero= int(input("Introduce un número por favor: "))
intentos=0
while numero<0:
    print("No se puede calcular la raiz de un número negativo")

    if intentos==2:
        print("Has superado el número de intentos. El programa a finalizado")
        break
    numero=int(input("Introduce un número, por favor: "))
    if numero<0:
        intentos=intentos+1

if intentos<2:
    solucion=m.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es " + str(solucion) )