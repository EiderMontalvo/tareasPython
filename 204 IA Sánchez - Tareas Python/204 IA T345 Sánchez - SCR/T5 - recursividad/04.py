import os 
os.system ("cls")

lista = list (map(int,input("ingrese una lista de números separados por espacios: ").split()))

def contar_elementos(lista):
    if len (lista) == 0:
        return 0
    return +1 + contar_elementos(lista[1:])

print (f"el número de elementos de la lista es:{contar_elementos(lista)}")