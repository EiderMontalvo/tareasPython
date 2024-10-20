import os
os.system ("cls")

palabra = input ("ingrese una palabra: ")

def palindromo(cadena):
    if len (cadena) <= 1:
        return True
    if cadena [0] != cadena [-1]:
        return False
    return palindromo(cadena[1:-1])

if palindromo (palabra):
    print (f"la palabra {palabra} es un palindromo")
else:
    print (f"la palabra {palabra} no es un palindromo")