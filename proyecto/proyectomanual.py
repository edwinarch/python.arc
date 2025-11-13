

import os #for borrar pantalla
import time # agrg tiemp 
import getpass # ocultar el textp o contr
#from colorama import rojo # color en consola

# datos
nombProducto = []
cantProducto = []
precioProducto = []
# variables globales
total_venta = 0.0
descuento = 0.0

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
            time.sleep(0.01)
                
        while True:
            time.sleep(1)
            print(esp)
            print(ColoresMain.VERDE,"Preparando...",ColoresMain.RESET)
            time.sleep(2)
            os.system('cls')
            print(ColoresMain.AZUL)
            print("__LOGIN-POS__")
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
                else: # contra incorrecta y cuenta
                    
                    intentos -= 1
                    if intentos > 0:
                        os.system('cls')
                        print(ColoresMain.AZUL,"---------------------------------------------------------------------",ColoresMain.RESET)
                        print(ColoresMain.ROJO + "Contraseña incorrecta. Te quedan ", intentos, " intentos. Inténtalo de nuevo: ", ColoresMain.RESET )
                        #print(esp)
                    else:
                        print(esp)
                        print("Contraseña incorrecta.",ColoresMain.ROJO,"No te quedan intentos. Acceso denegado.", ColoresMain.RESET)
                        print(esp)
                        exit()
                
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
    
# Cuando inicia el programa para que inicie el |def| de "main()"
if __name__ == "__main__":
    main()
