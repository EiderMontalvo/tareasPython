import os
os.system ("cls")

base = int (input ("ingrese la base: "))
exponente = int (input ("ingrese el exponente: "))

def potencia(base,exponente):
    if exponente == 0:
        return 1
    return base * potencia(base,exponente - 1)

print (f"el resultado de la potencia es: {potencia(base,exponente)}")