import os
os.system ("cls")

unidadesProducto = int(input("Ingrese la cantidad a comprar: "))

if 1 <= unidadesProducto <= 25:
    precioUnitario = 27
elif 26 <= unidadesProducto <= 50:
    precioUnitario = 25
elif unidadesProducto > 50:
    precioUnitario = 23
else:
    print("Cantidad de unidades no válida.")
    exit()

importeTotal = unidadesProducto * precioUnitario

if unidadesProducto > 50:
    descuento = 0.15 * importeTotal
else:
    descuento = 0.05 * importeTotal

totalAPagar = importeTotal - descuento

print(f"Importe total: S/. {importeTotal:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Total a pagar: S/. {totalAPagar:.2f}")
