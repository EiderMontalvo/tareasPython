import os
os.system("cls")

num = int(input("Ingrese un número de 4 cifras: "))

if 1000 <= num <= 9999:
    cifra1 = num // 1000
    cifra2 = (num // 100) % 10
    cifra3 = (num // 10) % 10
    cifra4 = num % 10
    print(f"El número ordenado es: {cifra4}{cifra3}{cifra2}{cifra1}")
else:
    print("El número no tiene 4 cifras.")