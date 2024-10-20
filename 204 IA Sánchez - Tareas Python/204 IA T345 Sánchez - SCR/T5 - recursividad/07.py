import os
os.system ("cls")

a = int (input ("ingrese el primer numero: "))
b = int (input ("ingrese el segundo numero: "))

def mcd(a,b):
    if b == 0:
        return a
    return mcd(b, a % b)

print (f"el MCD de {a} y {b} es: {mcd(a,b)}")