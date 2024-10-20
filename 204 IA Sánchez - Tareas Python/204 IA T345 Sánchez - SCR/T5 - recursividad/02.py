import os 
os.system ("cls")

cadena = input ("ingrese una cadena: ")

def revertir_C(cadena):
    if len (cadena) == 0:
        return cadena
    else:
        return revertir_C(cadena[1:]) + cadena[0]
    
print ("la cadena revertida es:",revertir_C(cadena))