import os 
os.system ("cls")

num1 = int(input("Ingrese el primer número de 3 cifras: "))
num2 = int(input("Ingrese el segundo número de 3 cifras: "))

if 100 <= num1 <= 999 and 100 <= num2 <= 999:
    num1_cifra1 = num1 // 100
    num1_cifra2 = (num1 // 10) % 10
    num1_cifra3 = num1 % 10

    num2_cifra1 = num2 // 100
    num2_cifra2 = (num2 // 10) % 10
    num2_cifra3 = num2 % 10

    nuevo_num1 = num2_cifra1 * 100 + num1_cifra2 * 10 + num2_cifra3
    nuevo_num2 = num1_cifra1 * 100 + num2_cifra2 * 10 + num1_cifra3

    print(f"Los números con las cifras intercambiadas son: {nuevo_num1} y {nuevo_num2}")
else:
    print("Ambos números deben ser de 3 cifras.")
