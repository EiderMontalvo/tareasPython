import os
os.system ("cls")   

num = int (input("ingrese la cantidad en metros: "))

metros = 100 
cm = num * metros
pulgas = round ( num * 39.3701 , 2)
pies = round (num / 0.3048 , 2)
yardas = round (num * 1.09361 , 2)


print (f"en centimetros es: {cm} cm")
print (f"en pulgadas es: {pulgas} pulgadas")
print (f"en pies es: {pies} pies")
print (f"en yardas es: {yardas} yardas")