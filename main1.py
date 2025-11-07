\
\
# library for network operations
import os
import time

while True:
    print("  __________________________________________________________________")
    print("  |          Bienvenido a la CMD/comando de App de carlos          |")
    print("  |        Seleccione un opcion de modo para abrir apps-cmd        |")
    print("  ——————————————————————————————————————————————————————————————————")
    print("  .              1. Calculadora básica nivel 1                     .")
    print("  .              2. un contraseña de xixi (con libreria)           .")
    print("                                                                    ")
    print(" .               a. [info] de la app de xixi                       .")
    print("  .              0. Salir de la cmd-app                            .")
    print(" ———————————————————————————————————————————————————————————————————")
    print(" ")

    var_1 = input("Ingrese el modo: ")
    # form1
    if var_1 == '1':
        import form1.caculation  #/form1/caculation.py

    elif var_1 == '2':
        import form1.password #/form1/password.py

    # config
    elif var_1 == 'a':
        import form1.config.information  #/form1/config/information.py

    # config main
    elif var_1 == '0':
        print("Saliendo de la aplicación...")
        time.sleep(1)
        exit()

    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        time.sleep(1)
