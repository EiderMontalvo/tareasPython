import os
os.system ("cls")

num = int (input ("ingrese un número: "))

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)
    
print ("la suma de digitos es:",suma_digitos(num)) 