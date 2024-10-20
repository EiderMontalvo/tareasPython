import random
import string
import os
os.system("cls")

print ("---generador de contraseñas seguras---")

def generar_contrasena(longitud=12):
    minusculas = string.ascii_lowercase
    mayusculas = string.ascii_uppercase
    digitos = string.digits
    simbolos = string.punctuation

    caracteres = minusculas + mayusculas + digitos + simbolos

    contraseña = [
        random.choice(minusculas),
        random.choice(mayusculas),
        random.choice(digitos),
        random.choice(simbolos)
    ]

    contraseña += random.choices(caracteres, k=longitud - 4)
    random.shuffle(contraseña)
    return "".join(contraseña)

def main():
    longitud = int(input("ingresa la longitud de la contraseña en número (mínimo 8): "))
    if longitud < 8:
        print("la longitud mínima es 8.")
    else:
        contraseña = generar_contrasena(longitud)
        print(f"tu contraseña segura es: {contraseña}")

if __name__ == '__main__':
    main()  
