
import os,math 
os.system ("cls")

radio = int (input("radio: "))
altura = int (input("altura: "))

area = 2* math.pi * radio * (radio + altura)
volumen = math.pi * math.pow (radio,2) * altura

print (f"area: {area:.2f}")
print (f"volumen: {volumen:.2f}")

print (math.pi)

