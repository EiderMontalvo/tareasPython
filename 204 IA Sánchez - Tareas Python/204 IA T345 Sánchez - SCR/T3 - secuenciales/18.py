import os
os.system ("cls")

unidades = int (input("unidades: "))
precio = float (input("precio: "))

compra = unidades * precio
descuento1 = 0.15 * compra
descuento2 = 0.15 * (compra - descuento1)

descuento = descuento1 + descuento2

print (f"compra = {compra:.2f}")
print (f"descuento = {descuento:.2f}")
print (f"total = {(compra - descuento):.2f}")