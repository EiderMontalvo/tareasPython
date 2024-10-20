
import os
os.system("cls")

import math

a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

discriminante = b**2 - 4 * a * c

if discriminante < 0:
    print("El discriminante es negativo. No hay soluciones reales.")
else:
    x1 = (-b + math.sqrt(discriminante)) / (2 * a)
    x2 = (-b - math.sqrt(discriminante)) / (2 * a)
    print(f"Las soluciones calculadas son: x1 = {x1} y x2 = {x2}")





