sueldoB = 500
Pcomision = 0.09
Pdescuento = 0.11

monto_vendido = float (input("ingrese el monto total vendido: s/. "))

comision = monto_vendido * Pcomision
sueldoBruto = sueldoB + comision
descuento = sueldoBruto * Pdescuento
sueldoNeto = sueldoBruto - descuento

print (F"\nresultados: ")
print (f"comision: s/.{comision}")
print (f"sueldo bruto: s/.{sueldoBruto}")
print (f"descuento: s/.{descuento}")
print (f"sueldo neto: s/.{sueldoNeto}")