\
\
#import library for system

#import library for local files\
import form1.password  # option mode is /form1/password.py
import form1.caculation # option mode is /form1/caculation.py

select_option = input("Ingrese la opcion: ")

while True:

    print("__________________________________________________________________")
    print("|          Bienvenido a la CMD/comando de App de xixi            |")
    print("|````````````````````````````````````````````````````````````````|")
    print("|       Seleccione un opcion de modo para abrir apps-cmd         |")
    print("——————————————————————————————————————————————————————————————————")
    print(".              1. Calculadora básica de xixi                     .")
    print(".              2. un contraseña de xixi (con libreria)           .")
    print("                                                                  ")
    print(".              0. Salir de la cmd-app                            .")
    print("———————————————————————————————————————————————————————————————————")
    print(" ")
    print(" ")
	#select option
    select_option= input("Ingrese la opcion: ")
    print(" ")



    # app mode .1
    if select_option == '1':
        
        form1.caculation.main()