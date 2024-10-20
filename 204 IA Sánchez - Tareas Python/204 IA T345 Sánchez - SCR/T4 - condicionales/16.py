import os
os.system ("cls")

ingresoMensual = int (input("ingreso mensual: "))
costoCasa = int (input("ingrese costo de la casa: "))

#if ingresoMensual < 1250:
#   coutaInicial = 0.15 * costoCasa
#    coutaMensual = (0.85 * costoCasa) / 120
#else:
#   coutaInicial = 0.30 * costoCasa
#     coutaMensual = (0.70 * costoCasa) / 75

coutaInicial = (0.15 if ingresoMensual < 1250 else 0.30) * costoCasa
coutaMensual = (0.85 if ingresoMensual < 1250 else 0.70) * costoCasa / (120 if ingresoMensual < 1250 else 75)

print (f"cuota inicial = {coutaInicial:.2f}")
print (f"couta mensual = {coutaMensual:.2f}")