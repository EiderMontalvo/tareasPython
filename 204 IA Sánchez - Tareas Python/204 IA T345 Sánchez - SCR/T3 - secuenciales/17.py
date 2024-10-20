import os
os.system ("cls")
Donacion = float (input("ingrese el monto anual a donar: "))
CentroSalud = 0.25 * Donacion
ComedorInfa = 0.35 * Donacion
EscuelaInfa = 0.25 * Donacion

AsiloAncian = Donacion - (CentroSalud + ComedorInfa + EscuelaInfa)

print (f"centro de salud:s/: {CentroSalud}")
print (f"comidor infantil:s/: {ComedorInfa}")
print (f"escuela infantil:s/: {EscuelaInfa}")
print (f"asilo ancianos:s/: {AsiloAncian}")
