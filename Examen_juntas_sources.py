
import random
import time
#import os

while True:
    print("1. Primer premio ")
    print("2. Segundo premio ")
    print("3. Tercer premio ")
    print("4. Reventado") 
    print("5. Salir")

    print(" ")# espacio

    options123 = input("Ingresar premio: ")

    print(" ")# espacio


    if options123 == '1':
        
        print("ESTE ES EL PREMIO:  !PRIMER !")
        
        x1 = random.randrange(0, 99)
        print("EL numero noraml es: ", x1)
        x2 = random.randint(100, 999)
        print("numero serie es: ", x2)
        
        options = input("Ingresar cualquier letra para regresar al menu:  ")
    elif options123 == '2':
        
        print("ESTE ES EL PREMIO:  !PRIMER !")
        
        x1 = random.randrange(0, 99)
        print("EL numero noraml es: ", x1)
        x2 = random.randint(100, 999)
        print("numero serie es: ", x2)
        
        options = input("Ingresar cualquier letra para regresar al menu:  ")
