import os 
os.system ("cls")

cadena = input ("ingrese una cadena: ")

def contar_vocales(cadena):
    if len (cadena) == 0:
        return 0
    if cadena[0] in "aeiouAEIOU":
        return 1 + contar_vocales(cadena[1:])
    else:
        return contar_vocales(cadena[1:])
    
print (f"el número de vocales en la cadena es: {contar_vocales(cadena)}")