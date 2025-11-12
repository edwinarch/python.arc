import time
import os 

print("Ingrese la contraseña:")

# solo tiene 3 portunidades
contra = "123"
intentos = 3
while intentos > 0:
    entrada = input()
    if entrada == contra:
        print("Contraseña correcta. Acceso concedido.")
        time.sleep(1)
        os.system('cls')
        print("Bienvenido al sistema")
        time.sleep(1)
        os.system('cls')
        print("{Seleccione archivo}")
        print("1. form1 ")
        print("2. form2 ")
        print("3. privado (LOCKED!) ")
        print(" ")
        opcion = input("Elige una opcion: ")
        if opcion == "1":
            os.system('python form1/Examen Python.py')
        elif opcion == "2":
            os.system('python form2/Examen.py')
        elif opcion == "3":
            contra = "priv123"
            intentos = 3
            while intentos > 0:
                entrada_priv = input("Ingrese la contraseña para el archivo privado: ")
                if entrada_priv == contra:
                    print("Contraseña correcta. Acceso concedido al archivo privado.")
                    time.sleep(1)
                    os.system('cls')
                    os.system('python privado/Examen juntas soc.py')
                    break
                else:
                    intentos -= 1
                    if intentos > 0:
                        print(f"Contraseña incorrecta. Te quedan {intentos} intentos. Inténtalo de nuevo:")
                    else:
                        print("Contraseña incorrecta. No te quedan intentos. Acceso denegado al archivo privado.")
        break
    else:
        intentos -= 1
        if intentos > 0:
            print(f"Contraseña incorrecta. Te quedan {intentos} intentos. Inténtalo de nuevo:")
        else:
            print("Contraseña incorrecta. No te quedan intentos. Acceso denegado.")