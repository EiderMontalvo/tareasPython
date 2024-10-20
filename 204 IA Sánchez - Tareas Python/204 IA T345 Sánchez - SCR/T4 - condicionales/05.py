import os
os.system ("cls")

num = int(input("Ingresa un número de 4 cifras: "))

if 1000 <= num <= 9999:
    cifras = [int(digito) for digito in str(num)]
    mayor = max(cifras)
    menor = min(cifras)
    num1 = int(str(mayor) + str(menor))
    num2 = int(str(menor) + str(mayor))
    resultado = max(num1, num2)
    print(f"El mayor número posible usando las cifras es: {resultado}")
else:
    print("El número ingresado no es de 4 cifras. Por favor, inténtalo de nuevo.")

