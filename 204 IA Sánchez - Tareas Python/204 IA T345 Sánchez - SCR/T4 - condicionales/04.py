import os
os.system ("cls")

nota1 = int (input("ingrese la nota nr°1: "))
nota2 = int (input("ingrese la nota nr°2: "))
nota3 = int (input("ingrese la nota nr°3: "))

if nota3 >= 10:
    nota3 += 2

promedio = (nota1 + nota2 + nota3) /3 

print (f"el promedio de la nota es: {promedio:.2f}")
