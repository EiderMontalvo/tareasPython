import os
os.system ("cls")

angulo = float (input("ingrese el angulo en grados: "))

if angulo == 0:
    clasificacion = "nulo"
elif 0 < angulo < 90:
    clasificacion = "agudo"
elif angulo == 90:
    clasificacion = "recto"
elif 90 < angulo < 180:
    clasificacion = "obtuso"
elif angulo == 180:
    clasificacion = "llano"
elif 180 < angulo < 360:
    clasificacion = "concavo"
elif angulo == 360:
    clasificacion = "completo"
else:
    print ("angulo invalido")

print (f"la clasificacion del angulo es: {clasificacion}")
