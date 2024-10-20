import os
os.system ("cls")

tramo1 = float (input("ingrese la longitud del primer tramo en kilometros: "))
tramo2 = float (input("ingrese la longitud del segundo tramo en pies: "))
tramo3 = float (input("ingrese la longitud del tercer tramo en millas: "))
metros = 0
yardas = 0

metros = tramo1 * 1000 + tramo2 / 3.2808 + tramo3 * 1609
yardas = metros * 1.09361

print (f"la longitud total recorrida en metros es: {metros:.2f} m")
print (f"la longitud total recorrida en yardas es: {yardas:.2f} yardas")
