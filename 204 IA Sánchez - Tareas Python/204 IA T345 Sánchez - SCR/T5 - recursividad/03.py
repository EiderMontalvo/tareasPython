import os
os.system ("cls")

lista = list (map(int,input("ingrese una lista de números: ").split()))
num = int (input ("ingrese un número a buscar: "))

def buscar_num(lista,num):
    if len (lista) == 0:
        return False
    if lista [0] == num:
        return True
    return buscar_num (lista[1:], num)
        
if buscar_num(lista,num) == True:
    print (f"el número {num} se encuentra en la lista")
else:
    print (f"el número {num} no se encuentra en la lista")

