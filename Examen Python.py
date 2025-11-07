import time 
import random

while True:
        print("Bienvenido al juego")
        time.sleep(1)
        print("Junta  de Proteccion Social")
        print("=====Menu Principal=====")
        print("1.Primer Premio")
        print("2.Segundo Premio")
        print("3.Tercer Premio")
        print("4.Reventado")
        print("5.Salir")
        
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            print("Este es el primer premio")
            random1    = random.randrange(0, 99)
            random2   = random.randrange(100, 999)
            print("Numero normal: ", random1)
            print("Numero serie: ", random2)    
            regresar = int("Ingrese cualquier letra para Regresar menu")
            
        elif opcion == "2":
            print("Este es el segundo premio")
            random1  = random.randrange(0, 99)
            random2 = random.randrange(100, 999)
            print("Numero normal: " , random1)
            print("Numero serie: ", random2)    
            regresar = int("Ingrese cualquier letra para Regresar menu")

        elif opcion == "3":
            print("Este es el tercer premio")
            random1    = random.randrange(0, 99)
            random2   = random.randrange(100, 999)
            print("Numero normal: ", random1)
            print("Numero serie: ", random2)    
            regresar = int("Ingrese cualquier letra para Regresar menu")

        elif opcion == "4":
            randomColor = random.randrange(1, 3)
            if randomColor == 1:
                print("Bola Roja")
                
            elif randomColor == 2:
                print("Bola Blanca")
                
            elif randomColor == 3:
                print("Bola Reventada")
            opcion = input("Ingrese cualquier letra para regresar al menu: ")
        elif opcion == "5":
            break
       
