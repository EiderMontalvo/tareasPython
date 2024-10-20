import os
os.system ("cls")

aporte_juan = float(input("Ingrese el aporte de Juan en dólares: "))
aporte_rosa = float(input("Ingrese el aporte de Rosa en dólares: "))
aporte_daniel_soles = float(input("Ingrese el aporte de Daniel en soles: "))

tasa_cambio = 3.00
aporte_daniel_dolares = aporte_daniel_soles / tasa_cambio

capital_total = aporte_juan + aporte_rosa + aporte_daniel_dolares

porcentaje_juan = (aporte_juan / capital_total) * 100
porcentaje_rosa = (aporte_rosa / capital_total) * 100
porcentaje_daniel = (aporte_daniel_dolares / capital_total) * 100

print(f"El capital total en dólares es: ${capital_total:.2f}")
print(f"Porcentaje de aporte de Juan: {porcentaje_juan:.2f}%")
print(f"Porcentaje de aporte de Rosa: {porcentaje_rosa:.2f}%")
print(f"Porcentaje de aporte de Daniel: {porcentaje_daniel:.2f}%")