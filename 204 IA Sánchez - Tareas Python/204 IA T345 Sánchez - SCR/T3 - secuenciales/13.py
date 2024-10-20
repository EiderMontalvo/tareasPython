import math
import os
os.system ("cls")

a = int (input("ingrese la longitud del primer cateto(a): ")) 
b = int (input("ingrese la longitud del segundo cateto(b): "))

hipotenusa = math.sqrt(a**2 + b**2)
print (f"la hipotenusa del triangulo es: {hipotenusa}")