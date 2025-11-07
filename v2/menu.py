
import os

def saludar():
    print("\n✍️Hola, bienvenido al programa :3 ")
    os.system("start cmd /max /k python Hola_Mundo.py")
def sumar():
    a = int(input("Ingresa el primer numero："))
    b = int(input("Ingresa el segundo numero："))
    print(f"La suma es: {a + b}")

def despedir():
    print("\n✍ Gracias por usar el programa. Hasta luego. ")

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Saludar")
        print("2. Sumar dos numeros")
        print("3.Despedirse y salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            saludar()
        elif opcion == "2":
            sumar()
        elif opcion == "3":
            despedir()
            break
        else:
            print ("⚠️ Opción no válida, intenta de nuevo.")

# Ejecutar el menú
menu()
