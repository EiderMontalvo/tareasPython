import os
os.system ("cls")

varones = int (input("varones: "))
mujeres = int (input("mujeres: "))
total = varones + mujeres

Pvaro = (varones / total) * 100.0
Pmuje = (mujeres / total) * 100.0

print(f"\nel porcentaje de varones es: {Pvaro}%") 
print(f"el porcentaje de mujeres es: {Pmuje}%")