import os
os.system ("cls")

n = int (input("ingrese un número: "))

def imprimir_hasta_n(n):
    if n == 0:
        return
    imprimir_hasta_n(n-1)
    print(n,end=" ")

imprimir_hasta_n(n)