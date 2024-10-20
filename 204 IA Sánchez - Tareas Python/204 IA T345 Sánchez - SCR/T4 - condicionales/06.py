import os
os.system("cls")

edad1 = int (input("ingrese la edad de la persona nr°1: "))
edad2 = int (input("ingrese la edad de la persona nr°2: "))
edad3 = int (input("ingrese la edad de la persona nr°3: ")) 

mayor = max (edad1, edad2, edad3) 
menor = min (edad1, edad2, edad3) 

print (f"la edad mayor es: {mayor}")
print (f"la edad menor es: {menor}")