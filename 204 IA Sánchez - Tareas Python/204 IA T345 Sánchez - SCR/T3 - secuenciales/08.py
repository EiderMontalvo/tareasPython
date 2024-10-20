import os
os.system ("cls")

import math

radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

area_base = math.pi * radio ** 2
area_lateral = 2 * math.pi * radio * altura
area_total = 2 * area_base + area_lateral

print(f"Área de la base: {area_base:.2f}")
print(f"Área lateral: {area_lateral:.2f}")
print(f"Área total: {area_total:.2f}")