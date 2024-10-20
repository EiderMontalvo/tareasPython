import os 
os.system ("cls")

nota1 = int (input("ingrese la nota nr1: "))
nota2 = int(input("ingrese la nota nr2: "))
nota3 = int(input("ingrese la nota nr3: "))
nota4 = int(input("ingrese la nota nr4: "))
nota5 = int (input("ingrese la nota nr5: "))

notaMayor = max (nota1, nota2, nota3, nota4, nota5)
notaMenor = min (nota1, nota2, nota3, nota4, nota5)

notas = [nota1, nota2, nota3, nota4, nota5]

notas.remove(notaMayor)
notas.remove(notaMenor)
notasEliminadas = notas 

promedio = sum(notas) / len(notas)

print (f"el promedio de las notas es: {promedio:.2f}")
print (f"la nota mayor es: {notaMayor}")
print (f"la nota menor es: {notaMenor}")