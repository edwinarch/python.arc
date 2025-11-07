
import random
import time
#import os

while True:
    espacio = " " #chunk
    print("1. Primer premio ")
    print("2. Segundo premio ")
    print("3. Tercer premio ")
    print("4. Reventado") 
    print("5. Salir")
    print(espacio)
    a = input("Ingresar premio: ")
    print(espacio)
    if a == '1':
        espacio = " " #chunk)
        print(espacio, espacio,espacio,espacio)
        print(espacio,espacio)
        block = "ESTE ES EL PREMIO: "
        print(espacio,espacio,espacio)
        print(espacio,espacio,espacio,espacio,espacio)
        print(espacio,espacio,espacio)
        print(block, " !PRIMER !")
        print(espacio,espacio,espacio,espacio)
        x1 = random.randrange(0, 99)
        print("EL numero noraml es: ", x1)
        x2 = random.randint(100, 999)
        print("numero serie es: ", x2)
        print(espacio)
        options = input("Ingresar cualquier letra para regresar al menu:  ")
        print(espacio)
    elif a == '2':
        espacio = " " #chunk)
        print(espacio, espacio,espacio,espacio)
        print(espacio,espacio)
        block = "ESTE ES EL PREMIO: "
        print(espacio,espacio,espacio)
        print(espacio,espacio,espacio,espacio,espacio)
        print(espacio,espacio,espacio)
        print(block, " !SEGUNDO !")
        print(espacio,espacio,espacio,espacio)
        x1 = random.randrange(0, 99)
        print("EL numero noraml es: ", x1)
        x2 = random.randint(100, 999)
        print("numero serie es: ", x2)
        print(espacio)
        options = input("Ingresar cualquier letra para regresar al menu:  ")
        print(espacio)
    elif a == '3':
        espacio = " " #chunk)
        print(espacio, espacio,espacio,espacio)
        print(espacio,espacio)
        block = "ESTE ES EL PREMIO: "
        print(espacio,espacio,espacio)
        print(espacio,espacio,espacio,espacio,espacio)
        print(espacio,espacio,espacio)
        print(block, " !TERCER !")
        print(espacio,espacio,espacio,espacio)
        x1 = random.randrange(0, 99)
        print("EL numero noraml es: ", x1)
        x2 = random.randint(100, 999)
        print("numero serie es: ", x2)
        print(espacio)
        options = input("Ingresar cualquier letra para regresar al menu:  ")
        print(espacio)
    elif a == '4':
        espacio = " " #chunk)
        espaciov2 = "" #chunk)
        print(espacio, espacio,espacio,espacio)
        print(espacio,espacio)
        x1 = random.randrange(1, 3)
        if x1 == 1:
            print(espaciov2)
            print("ES BOLA ES! ROJO! ")
            print(espacio, espaciov2)
        elif x1 == 2:
            print(espaciov2,espaciov2)
            print("ES BOLA ES! BLANCA! ")
            print(espacio, espaciov2)
        elif x1 == 3:
            print(espaciov2,espaciov2,espaciov2)
            print("ES BOLA ES! REVENTADO! ")
            print(espacio,espacio,espacio)
            print(espacio, espaciov2)
        options = input("Ingresar cualquier letra para regresar al menu:  ")
        print(espacio, espaciov2,espacio)
        print(espacio,espacio)
        print(espacio,espacio,espacio,espacio)
        print(espacio,espacio,espacio)
        print(espacio,espacio,espacio,espacio,espacio)
    elif a == '5':
        print("Saliendo del programa...")
        time.sleep(2)
        break