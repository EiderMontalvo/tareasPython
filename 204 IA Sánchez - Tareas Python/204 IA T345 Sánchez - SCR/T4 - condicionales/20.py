import os
os.system ("cls")

a = int (input("ingrese el primer numero: "))
b = int (input("ingrese el segundo numero: "))
c = int (input("ingrese el tercer numero: "))

if a < b and b < c:
    print ("estan en orden acendente")
elif a > b and b > c:
    print ("estan en orden desendente")
else:
    print ("estan desordenados")