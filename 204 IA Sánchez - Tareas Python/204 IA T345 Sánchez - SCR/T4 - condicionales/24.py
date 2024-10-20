import os
os.system ("cls")

montoVendido = float (input("ingrese el monto vendido: "))

sueldo_base = montoVendido * 0.10
bonificacion = 0

if montoVendido > 5000:
    bonificacion = ((montoVendido - 5000) // 500) * 25

sueldo_total = sueldo_base + bonificacion
print(f"El sueldo total del vendedor es: S/. {sueldo_total:.2f}")