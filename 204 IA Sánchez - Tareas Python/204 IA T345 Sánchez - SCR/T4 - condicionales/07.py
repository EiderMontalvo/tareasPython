import os 
os.system ("cls")

num1 = int (input("ingrese el primer numero: "))
num2 = int (input("ingrese el segundo numero: "))
num3 = int (input("ingrese el tercer numero: "))

numIntermedio = num1 + num2 + num3 - max(num1, num2, num3) - min(num1, num2, num3)

print (f"el numero intermedio es: {numIntermedio}")