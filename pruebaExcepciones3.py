import math as m

def calculaRaiz(num1):
    if num1<0:
        raise ValueError("El número no puede ser negativo")
    else:
        return m.sqrt(num1)
op1=(int(input("Introduce un número: ")))

print(calculaRaiz(op1))

