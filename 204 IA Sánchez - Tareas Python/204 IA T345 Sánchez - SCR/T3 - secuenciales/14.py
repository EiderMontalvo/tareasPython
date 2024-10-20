import math

num = []
for i in range(5):
    numero = float(input(f"ingrese el número {i + 1}: "))
    num.append(numero)

tres_mayores = sorted(num)[-3:]
promedio = sum(tres_mayores) / 3

print(f"los 3 números mayores son: {tres_mayores}")
print(f"el promedio de los 3 números mayores es: {math.ceil(promedio)}")

