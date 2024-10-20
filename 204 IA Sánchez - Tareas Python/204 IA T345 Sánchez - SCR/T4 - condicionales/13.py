import os
os.system ("cls")

num = int(input("ingresa un número de 3 cifras: "))

if num >= 100 and num <= 999:
    c1 = num // 100
    c2 = (num // 10) % 10
    c3 = num % 10

    if c1 == c2 - 1 and c2 == c3 - 1:
        print("las cifras son consecutivas en orden ascendente")
    elif c1 == c2 + 1 and c2 == c3 + 1:
        print("las cifras son consecutivas en orden descendente")
    else:
        print("las cifras no son consecutivas")
else:
    print("el número no tiene 3 cifras")

