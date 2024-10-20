import os
os.system ("cls")

estatura_ingles = input("Ingrese la estatura en formato inglés (ejm. 3' 2\"): ")

pies, pulgadas = estatura_ingles.split("' ")
pies = int(pies)
pulgadas = int(pulgadas.replace('"', ''))

pies_a_metros = pies * 0.3048
pulgadas_a_metros = pulgadas * 0.0254

estatura_metros = pies_a_metros + pulgadas_a_metros


print(f"La estatura en metros es: {estatura_metros:.2f} m")


