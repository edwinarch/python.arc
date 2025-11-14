

import os #for borrar pantalla
import time # agrg tiemp 
import getpass # ocultar el textp o contr
#from colorama import rojo # color en consola
import random

def mainPos():
    esp = " " #chunk
    #~~~~~~Definir códigos de color ANSI，  CONFIG COLOR
    class ColoresMain:
        # Código para resetear el color
        RESET = "\033[0m"
        #Códigos de colores
        ROJO = '\033[31m'
        NEGRO = '\033[30m'
        AMARILLO = '\033[33m'
        AZUL = '\033[34m'
        VERDE = '\033[32m'
        MAGENTA = '\033[35m'
        CIAN = '\033[36m'
        BLANCO = '\033[37m'
        SUBRAYADO = '\033[4m'
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~public static
    os.system('cls')
    print(ColoresMain.AZUL + "Bienvenido, Selecciones el maquina de POS" + ColoresMain.RESET)
    print(esp)
    print("1. POS-1")
    print("2. POS-2")
    print(esp)
    selectPOS = input(">> ")
    while True:
        if selectPOS == "1":
            time.sleep(0.08)
            main()
        elif selectPOS == "2":
            time.sleep(0.08)
            loginMax()
        else:
            print("Incorrecto>! ")
            exit()

def loginMax():
    #chunk[
    esp = " "
    #~~~~~~Definir códigos de color ANSI，  CONFIG COLOR
    class ColoresMain:
        # Código para resetear el color
        RESET = "\033[0m"
        #Códigos de colores
        ROJO = '\033[31m'
        NEGRO = '\033[30m'
        AMARILLO = '\033[33m'
        AZUL = '\033[34m'
        VERDE = '\033[32m'
        MAGENTA = '\033[35m'
        CIAN = '\033[36m'
        BLANCO = '\033[37m'
        SUBRAYADO = '\033[4m'
    #end chunk]
    
    # verificacion CAPTCHAT de Edwin
    def VerficationCAPTCHATForEdmin():
        randNum1 = random.randrange(0, 20)
        randNum2 = random.randrange(0, 10) 
        resultado_correcto = randNum1 + randNum2
        try:
            respuesta_usuario = int(input(f"¿Cuánto es {randNum1} + {randNum2}? "))
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")
            exit() # Salir del programa si la entrada no es un número

        # Verificamos si la respuesta del usuario es correcta
        if respuesta_usuario == resultado_correcto:
            print("¡Correcto! Has acertado.")
        else:
            print(f"Incorrecto. La respuesta correcta era {resultado_correcto}.")   
    
    # verificacion CAPTCHAT de Edwin       
    def VerficationCAPTCHATForEdmin2():
        intentos = 4
        while intentos >= 0:
            
            LineFault = "----------------------------------------------"
            randNum1 = random.randrange(0, 20)
            randNum2 = random.randrange(0, 10)
            outnumResultFix = randNum1 + randNum2 #fix result
            print(ColoresMain.AZUL + "|||||| CAPTCAHT! ||||||" + ColoresMain.RESET)
            print(ColoresMain.MAGENTA,"》",ColoresMain.RESET,"Eres robot o humano?")
            if intentos == 3:
                print(esp)
                print(ColoresMain.ROJO,LineFault,ColoresMain.RESET)
                print(">>>","Te quedan",ColoresMain.VERDE, 3 ,ColoresMain.RESET,"intentos.")
                print(ColoresMain.ROJO,LineFault,ColoresMain.RESET)
            elif intentos == 2:
                print(esp)
                print(ColoresMain.ROJO,LineFault,ColoresMain.RESET)
                print(">>>","Te quedan",ColoresMain.AMARILLO, 2 ,ColoresMain.RESET,"intentos.")
                print(ColoresMain.ROJO,LineFault,ColoresMain.RESET)
            elif intentos == 1:
                print(esp)
                print(ColoresMain.ROJO,LineFault,ColoresMain.RESET)
                print(">>>","Te quedan",ColoresMain.ROJO, 1 ,ColoresMain.RESET,"intentos.")
                print(ColoresMain.ROJO,LineFault,ColoresMain.RESET)
            #print(" 001    <<<<<Write to Exit System.")
            #print(" 002    <<<<<Write to Return Main.")
            print(ColoresMain.RESET)
            print(esp)
            print("Cuanto es",randNum1,"+",randNum2,"?")
            print(esp)
        
            inputnumResultFix = int(input("Ingrese> "))
            if inputnumResultFix == outnumResultFix:
                os.system('cls')
                print(LineFault)
                print(ColoresMain.VERDE,"Capt-CHAT Verificado Correcto.",ColoresMain.RESET)
                print(LineFault)
                time.sleep(2)
                os.system('cls')
            elif inputnumResultFix == "001":
                os.system('cls')
                print("Success exit system!.")
            elif inputnumResultFix == "002":
                time.sleep(0.05)
                return
            else:
                intentos -= 1
                if intentos > 0:
                    if intentos == 3:
                        os.system('cls')
                        print(LineFault)
                        print(ColoresMain.RESET,"CAPT-CHAT:> Te quedan",ColoresMain.VERDE,intentos,ColoresMain.RESET," incorrecto intente de nuevo!.",ColoresMain.AMARILLO,"3s",ColoresMain.RESET)
                        print(LineFault)
                        time.sleep(1)
                        os.system('cls')
                        print(LineFault)
                        print(ColoresMain.RESET,"CAPT-CHAT:> Te quedan",ColoresMain.VERDE,intentos,ColoresMain.RESET," incorrecto intente de nuevo!.",ColoresMain.AMARILLO,"2s",ColoresMain.RESET)
                        print(LineFault)
                        time.sleep(1)
                        os.system('cls')
                        print(LineFault)
                        print(ColoresMain.RESET,"CAPT-CHAT:> Te quedan",ColoresMain.VERDE,intentos,ColoresMain.RESET," incorrecto intente de nuevo!.",ColoresMain.AMARILLO,"1s",ColoresMain.RESET)
                        print(LineFault)
                        time.sleep(1)
                        os.system('cls')
                    elif intentos == 2:
                        os.system('cls')
                        print(LineFault)
                        print(ColoresMain.RESET,"CAPT-CHAT:> Te quedan",ColoresMain.AMARILLO,intentos,ColoresMain.RESET," incorrecto intente de nuevo!.",ColoresMain.AMARILLO,"3s",ColoresMain.RESET)
                        print(LineFault)
                        time.sleep(1)
                        os.system('cls')
                        print(LineFault)
                        print(ColoresMain.RESET,"CAPT-CHAT:> Te quedan",ColoresMain.AMARILLO,intentos,ColoresMain.RESET," incorrecto intente de nuevo!.",ColoresMain.AMARILLO,"2s",ColoresMain.RESET)
                        print(LineFault)
                        time.sleep(1)
                        os.system('cls')
                        print(LineFault)
                        print(ColoresMain.RESET,"CAPT-CHAT:> Te quedan",ColoresMain.AMARILLO,intentos,ColoresMain.RESET," incorrecto intente de nuevo!.",ColoresMain.AMARILLO,"1s",ColoresMain.RESET)
                        print(LineFault)
                        time.sleep(1)
                        os.system('cls')
                    elif intentos == 1:
                        os.system('cls')
                        print(LineFault)
                        print(ColoresMain.RESET,"CAPT-CHAT:> Te quedan",ColoresMain.ROJO,intentos,ColoresMain.RESET," incorrecto intente de nuevo!.",ColoresMain.AMARILLO,"3s",ColoresMain.RESET)
                        print(LineFault)
                        time.sleep(1)
                        os.system('cls')
                        print(LineFault)
                        print(ColoresMain.RESET,"CAPT-CHAT:> Te quedan",ColoresMain.ROJO,intentos,ColoresMain.RESET," incorrecto intente de nuevo!.",ColoresMain.AMARILLO,"2s",ColoresMain.RESET)
                        print(LineFault)
                        time.sleep(1)
                        os.system('cls')
                        print(LineFault)
                        print(ColoresMain.RESET,"CAPT-CHAT:> Te quedan",ColoresMain.ROJO,intentos,ColoresMain.RESET," incorrecto intente de nuevo!.",ColoresMain.AMARILLO,"1s",ColoresMain.RESET)
                        print(LineFault)
                        time.sleep(1)
                        os.system('cls')
                    else:
                        #por si sale error en algo, sale el Debug,
                        print("Error de calculos portunidad!. ")
                    # return in capt,  reset
                    #os.system('cls')
                    #VerficationCAPTCHATForEdmin2()
                else: 
                    # cuando se te acaba la portunidad
                    os.system('cls') 
                    print(LineFault)
                    print(ColoresMain.ROJO,"CAPT-CHAT:> Te quedan","0"," incorrecto intente de nuevo!.",ColoresMain.AMARILLO,"0s",ColoresMain.RESET)
                    print(LineFault)
                    print(esp)
                    time.sleep(1)
                    exit() 
            
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~public stateic
    while True: 
        os.system('cls')
        print(ColoresMain.MAGENTA,"---Acceso---",ColoresMain.RESET)
        print(esp)
        entradaAccount = input("Ingrese la cuenta: ")
        entradaPwd = getpass.getpass("Ingrese la contraseña")
                  
        PosVerification = entradaAccount + entradaPwd # El POS Verifica la cuenta y pwd %$
        
        if PosVerification == "admin1234":
            print(esp)
            VerficationCAPTCHATForEdmin2() # verificar BOT!?
            print(ColoresMain.VERDE + "Correcto!, " + ColoresMain.RESET)
            print(esp)
            exit()
        else:
            print(esp)
            VerficationCAPTCHATForEdmin2()
            print(ColoresMain.ROJO + "Incorrecto!> " + ColoresMain.RESET)
            exit()
      
def main(): 
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~Definir códigos de color ANSI，  CONFIG COLOR
    class ColoresMain:
        # Código para resetear el color
        RESET = "\033[0m"
        #Códigos de colores
        ROJO = '\033[31m'
        NEGRO = '\033[30m'
        AMARILLO = '\033[33m'
        AZUL = '\033[34m'
        VERDE = '\033[32m'
        MAGENTA = '\033[35m'
        CIAN = '\033[36m'
        BLANCO = '\033[37m'
        SUBRAYADO = '\033[4m'            
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~public static
    contra = "123"
    contrasegundoplano = "python"
    contrachikycroos = "chiky"
    contrarandomLoteria = "loteria"
    intentos = 4 #4vece
    while intentos > 0:
        # Ingresar contra
        esp = " " # chunk
        
        # los cargas new
        for numero in range(1, 26):
            #Cargando sumulator |falso|
            print("Cargando...", numero,"/25")
            time.sleep(0.01)
        for numero in range(1, 71):
            #Cargando sumulator |falso|
            print("Descargando shaders", numero,"/70")
            time.sleep(0.01)
        for numero in range(1, 26):
            #Cargando sumulator |falso|
            print("Descargando pack", numero,"/25")
            time.sleep(0.02)
                
        while True:
            time.sleep(1)
            print(esp)
            print(ColoresMain.VERDE,"Preparando...",ColoresMain.RESET)
            time.sleep(2)
            os.system('cls')
            print(ColoresMain.AZUL)
            print("__ __LOGIN-POS__ __")
            print(ColoresMain.RESET)
            print(esp)

            while True:
                # Consome.ReadLine()
                print(ColoresMain.AZUL,"-------------------------------------------------------------------",ColoresMain.RESET)
                entrada = getpass.getpass("Ingresa tu contraseña: ")
                print(ColoresMain.AZUL,"---------------------------------------------------------------",ColoresMain.RESET)
                
                #primer plano
                if entrada == contra:
                    print(esp)
                    print(ColoresMain.VERDE,"Contraseña correcta. Acceso concedido.", ColoresMain.RESET)
                    time.sleep(2)
                    os.system('cls')
                    #print(ColoresMain.SUBRAYADO)
                    print("Bienvenido al sistema")
                    #print(ColoresMain.RESET)
                    time.sleep(1)
                    os.system('cls')
                    main2() # transportar a "main2()
                elif entrada == contrasegundoplano: # contra segundo plano
                    print(esp)
                    print(ColoresMain.VERDE,"Contraseña correcta. Acceso concedido al segundo plano.", ColoresMain.RESET)
                    time.sleep(2)
                    os.system('cls')
                    edwinarch() # transportar a "edwinarch()
                elif entrada == contrachikycroos: # contra chiky croos
                    print(esp)
                    print(ColoresMain.VERDE,"Contraseña correcta. Acceso concedido al plano chiky croos.", ColoresMain.RESET)
                    time.sleep(2)
                    os.system('cls')
                    chikycroos() # transportar a "chikycroos()  
                elif entrada == contrarandomLoteria:
                    print(esp)
                    print(ColoresMain.VERDE,"Contraseña correcta. Acceso concedido al LOTERIA.", ColoresMain.RESET)
                    time.sleep(2) 
                    os.system('cls')
                    randomLoteria() # trasnport loteria()          
                else: # contra incorrecta y cuenta
                    
                    intentos -= 1
                    if intentos > 0:
                        os.system('cls')
                        print(ColoresMain.AZUL)
                        print("__ __LOGIN-POS__ __")
                        print(ColoresMain.RESET)
                        print(esp)
                        print(ColoresMain.AZUL,"---------------------------------------------------------------------",ColoresMain.RESET)
                        print(ColoresMain.AMARILLO + "Contraseña incorrecta. Te quedan ", intentos, " intentos. Inténtalo de nuevo: ", ColoresMain.RESET )
                        #print(esp)
                    else:
                        print(esp)
                        print(esp)
                        print(esp)
                        print(esp)
                        print(esp)
                        print(esp)
                        os.system('cls')
                        print(ColoresMain.AZUL,"---------------------------------------------------------------------",ColoresMain.RESET)
                        print(ColoresMain.ROJO + "Contraseña incorrecta. Te quedanron 0 intentos.", ColoresMain.RESET )
                        print(ColoresMain.AZUL,"---------------------------------------------------------------------",ColoresMain.RESET)
                        print(esp)
                        print(ColoresMain.ROJO,"!~!~!~!~!~!~!~!~",ColoresMain.RESET)
                        print("Contraseña incorrecta.",ColoresMain.ROJO,"No te quedan intentos. Acceso denegado.", ColoresMain.RESET)
                        print(ColoresMain.ROJO,"!~!~!~!~!~!~!~!~",ColoresMain.RESET)
                        print(esp)
                        print(esp)
                        print(esp)
                        exit()

# datos
nombProducto = []
cantProducto = []
precioProducto = []
# variables globales
total_venta = 0.0
descuento = 0.0
def main2(): # static void main(); // eso de c#
    
    while True: # while(true) {} // eso de c#
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~Definir códigos de color ANSI，  CONFIG COLOR
        class ColoresMain:
            # Código para resetear el color
            RESET = "\033[0m"
            #Códigos de colores
            ROJO = '\033[31m'
            NEGRO = '\033[30m'
            AMARILLO = '\033[33m'
            AZUL = '\033[34m'
            VERDE = '\033[32m'
            MAGENTA = '\033[35m'
            CIAN = '\033[36m'
            BLANCO = '\033[37m'
            SUBRAYADO = '\033[4m'            
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~public static
        esp = " "#chunk
        print(ColoresMain.CIAN,"~~~ MENU DE OPCIONES ~~~",ColoresMain.RESET,)
        print(esp)
        print("1. Agregar producto")
        print("2. Calcular total de la venta")
        print("3. Mostrar resumen de la venta")
        print("4. Salir")
        print(esp)
        select = input("Seleccione una opción: ")
        # limpiar pantalla
        time.sleep(1)
        os.system('cls')
        if select == '1':
            agregar_producto()
        elif select == '2':
            calcular_total()
            print("Total calculado exitosamente.")
        elif select == '3':
            mostrar_resumen()
        elif select == '4':
            print("saliendo del programa...")
            exit()
        else:
            print("Opción no válida. Intente de nuevo.")

# Agregar producto            
def agregar_producto():
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~Definir códigos de color ANSI，  CONFIG COLOR
    class ColoresMain:
        # Código para resetear el color
        RESET = "\033[0m"
        #Códigos de colores
        ROJO = '\033[31m'
        NEGRO = '\033[30m'
        AMARILLO = '\033[33m'
        AZUL = '\033[34m'
        VERDE = '\033[32m'
        MAGENTA = '\033[35m'
        CIAN = '\033[36m'
        BLANCO = '\033[37m'
        SUBRAYADO = '\033[4m'            
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~public static
    print(ColoresMain.CIAN)#color cyan
    producto = input("Ingrese el nombre del producto: ")
    print(ColoresMain.VERDE)#color verde
    cantidad = int(input("Ingrese la cantidad del producto: "))
    print(ColoresMain.MAGENTA)#color violeta
    precio = float(input("Ingrese el precio del producto: "))
    print(ColoresMain.RESET)#resetiar color
    nombProducto.append(producto)
    cantProducto.append(cantidad)
    precioProducto.append(precio)
    os.system('cls')
    print(ColoresMain.AMARILLO)
    print("El producto", producto, "fue agregado exitosamente.")
    print(ColoresMain.RESET)
    
def calcular_total():
    global total_venta, descuento
    total_venta = sum(cantProducto[i] * precioProducto[i] for i in range(len(nombProducto)))
    if total_venta > 100:
        descuento = total_venta * 0.1
        total_venta -= descuento

def mostrar_resumen():
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~Definir códigos de color ANSI，  CONFIG COLOR
    class ColoresMain:
        # Código para resetear el color
        RESET = "\033[0m"
        #Códigos de colores
        ROJO = '\033[31m'
        NEGRO = '\033[30m'
        AMARILLO = '\033[33m'
        AZUL = '\033[34m'
        VERDE = '\033[32m'
        MAGENTA = '\033[35m'
        CIAN = '\033[36m'
        BLANCO = '\033[37m'
        SUBRAYADO = '\033[4m'            
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~public static
    print(ColoresMain.VERDE)
    print("\nResumen de la venta:")
    for i in range(len(nombProducto)):
        print(ColoresMain.AMARILLO)
        print(f"{nombProducto[i]} - Cantidad: {cantProducto[i]}, Precio: {precioProducto[i]}")
    
    esp = " "
    print(esp)
    #DEteminado
    #for por
    print("---------------------------------------")

    print(f"Descuento aplicado: ${descuento:.12f}")
    print(f"Total de la venta: ${total_venta:.2f}")
    print(ColoresMain.RESET)
    exit()
    
def edwinarch():
    #chunk
    myworld = "Hellow this is seccond plan2"
    esp = " "
    class ColoresMain:
        # Código para resetear el color
        RESET = "\033[0m"
        #Códigos de colores
        ROJO = '\033[31m'
        NEGRO = '\033[30m'
        AMARILLO = '\033[33m'
        AZUL = '\033[34m'
        VERDE = '\033[32m'
        MAGENTA = '\033[35m'
        CIAN = '\033[36m'
        BLANCO = '\033[37m'
        SUBRAYADO = '\033[4m'
    #end chunk
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~public static
    print(ColoresMain.CIAN,myworld,ColoresMain.RESET) 
    print(esp)
    exit()

def chikycroos():
    #chunk
    myworld = "THI IS CHIKY WOLRD"
    esp = " "
    class ColoresMain:
        # Código para resetear el color
        RESET = "\033[0m"
        #Códigos de colores
        ROJO = '\033[31m'
        NEGRO = '\033[30m'
        AMARILLO = '\033[33m'
        AZUL = '\033[34m'
        VERDE = '\033[32m'
        MAGENTA = '\033[35m'
        CIAN = '\033[36m'
        BLANCO = '\033[37m'
        SUBRAYADO = '\033[4m'
    #end chunk
    print(ColoresMain.AZUL,myworld,ColoresMain.RESET)
    print(esp)
    exit()

def randomLoteria():
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
        if a=='1':
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
            os.system('cls')
        elif a=='2':
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
        elif a=='3':
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
        elif a=='4':
            espacio = " " #chunk)
            espaciov2 = "" #chunk)
            print(espacio, espacio,espacio,espacio)
            print(espacio,espacio)
            x1 = random.randrange(1, 3)
            if x1==1:
                print(espaciov2)
                print("ES BOLA ES! ROJO! ")
                print(espacio, espaciov2)
            elif x1==2:
                print(espaciov2,espaciov2)
                print("ES BOLA ES! BLANCA! ")
                print(espacio, espaciov2)
            elif x1==3:
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
        elif a=='5':
            print("Saliendo del programa...")
            time.sleep(2)
            exit()
    
# Cuando inicia el programa para que inicie el |def| de "main()"
if __name__ == "__main__":
    mainPos()
