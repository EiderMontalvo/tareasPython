import os
os.system ("cls")

examenesAprobados= int(input("Ingrese el número de exámenes aprobados: "))

propinaM = 20
propinaA = 5

propina_total = propinaM + (propinaA * examenesAprobados)

print(f"El monto total de la propina es: S/. {propina_total}")

