\
\
import time

while True:
    print("-------------------------------------------------------")
    print("|  -Esta es una app de xixi, Sistema de comando       |")
    print("|   aquí puede ver la información de la app-          |")
    print("|                                                     |")
    print("|  Creado por: *carlos Xixi*                          |")
    print("|  Verción:    *V1.0*                                 |")
    print("|                                                     |")
    print("|.            1.  Volver al inicio     .              |")
    print("------------------------------------------------------")
    print(" ") #space
    type = input("Presione Enter para volver al inicio...      >> ")  # return to the .main menu
    print(" ") #space

    if type == '1':
        print("Volviendo al inicio...")
        time.sleep(2)
        break
        
    #error$
    else:
        print(" ! Porfavor, ingrese la opcion correcta... !")
        print("espere...    volviendo al informacion")
        time.sleep(2)