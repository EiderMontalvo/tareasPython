import os
os.system ("cls")

horas_trabajadas = float(input("ingrese el número total de horas trabajadas: "))
tarifa_horaria = float(input("ingrese la tarifa horaria: "))

sueldo_basico = horas_trabajadas * tarifa_horaria
bonificacion = sueldo_basico * 0.20
sueldo_bruto = sueldo_basico + bonificacion
descuento = sueldo_bruto * 0.10
sueldo_neto = sueldo_bruto - descuento

print(f"sueldo básico: {sueldo_basico}")
print(f"sueldo bruto: {sueldo_bruto}")
print(f"sueldo neto: {sueldo_neto}")
