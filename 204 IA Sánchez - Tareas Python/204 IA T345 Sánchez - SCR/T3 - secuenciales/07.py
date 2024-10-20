import os
os.system ("cls")

print ("--calculador de área y perimetro de un rectangulo--")
base = int(input("ingrese la base: "))
altura = int (input("ingrese la altura: "))

area = base * altura
perimetro = 2* (base + altura)

print (f"el área de un rectangulo es {area}")
print (f"el perimetro de un triangulo es {perimetro}")