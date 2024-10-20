cantidad = int (input("ingrese la cantidad de dinero: "))

billetes = [200, 100, 50, 20, 10]
monedas = [5, 2, 1]

print ("descomposicion de billetes: ")
for billete in billetes:
    cantidad_billetes = cantidad // billete
    cantidad %= billete
    if cantidad_billetes > 0 :
        print (f"{cantidad_billetes} billete(s) de s/.{billete}")

print ("descomposicion de monedas: ")
for moneda in monedas:
    cantidad_monedas = cantidad // moneda
    cantidad %= moneda
    if cantidad_monedas > 0:
        print (f"{cantidad_monedas} moneda(s) de s/.{moneda}")

