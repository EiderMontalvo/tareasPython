import os 
os.system ("cls")

horasAucencia = float (input("horas ausencia: "))
tornillosMAlos = float (input("tornillos malos: "))
tornillosBuenos = float (input("tornillos buenos: "))

if not horasAucencia and not tornillosMAlos and not tornillosBuenos: print("grado 5")
if horasAucencia and not tornillosMAlos and not tornillosBuenos: print ("grado 7")
if not horasAucencia and tornillosMAlos and not tornillosBuenos: print ("grado 8")
if not horasAucencia and not tornillosMAlos and tornillosBuenos: print("grado 9")