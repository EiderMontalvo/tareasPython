import os
os.system ("cls")

n = int (input("introduce el número de niveles de la pirámide: "))

def piramide(n):
    if n > 0:
        piramide(n-1)
        print ("*" * n)
    
piramide(n)