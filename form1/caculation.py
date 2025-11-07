\
\
# NETWORK LIBRARY
import time

print("------------------------------------------------------")
print("|   Quieres mostrar número entero o por decimales?   |")
print("------------------------------------------------------")
print("|  1. Entero   {int}                                 |")
print("|  2. Decimal  {float}                               |")
print("|                                                    |")
print("|  0.volver    [Return]                              |")
print("------------------------------------------------------")
print(" ")

a = input("Ingresar: ")
if a == '1':

    # inpuxing numbers
    print("Esta calculadora solo puede sumar dos numeros!")
    number1 = int(input("ingrese el primer numero: "))
    number2 = int(input("ingrese el segund numero: "))

    while True:
        print("--------------------------------------------------")
        print("|  Quieres sumar o restar?                       |")
        print("|  1.Sumar        {+}                            |")
        print("|  2.Restar       {-}                            |")
        print("|  3.Multiplicar  {*}                            |")
        print("|  4.Dividir      {/}                            |")
        print("|                                                |")
        print("|  5.Salir        [Exit]                         |")
        print("--------------------------------------------------")
        
        #<$>#
        opcion = input("Ingresar: ")
        #$1
        if opcion == '1':

            suma = number1 + number2
            print("La Sumar es: ", suma)
            #exit()
        #$2
        elif opcion == '2':

            restar = number1 + number2
            print("La Resta es: ", restar)
            #exit()
        #$3
        elif opcion == '3':
            
            multiplicar = number1 * number2
            print("La Multiplicacion es: ", multiplicar)
            #exit()
        #$4
        elif opcion == '4':
            
            if number2 != 0:
                dividir = number1 / number2
                print("La Division es: ", dividir)	
            #	exit()
        #$5
        elif opcion == '5':
            
            print("Saliendo del programa...")
            time.sleep(2)
            #exit()

        #error$
        else: #vew e most,>> error
            
            print("Porfavor, ingrese la opcion correcta...")
            print("espere...    volviendo al opcion")
            time.sleep(2)


#$2			
elif a == '2':
    
    # inpuxing numbers
    print("Esta calculadora solo puede sumar dos numeros!")
    number1 = float(input("ingrese el primer numero: "))
    number2 = float(input("ingrese el segund numero: "))

    while True:
        print("--------------------------------------------------")
        print("|  Quieres sumar o restar?                       |")
        print("|  1.Sumar        {+}                            |")
        print("|  2.Restar       {-}                            |")
        print("|  3.Multiplicar  {*}                            |")
        print("|  4.Dividir      {/}                            |")
        print("|                                                |")
        print("|  5.Salir        [Exit]                         |")
        print("--------------------------------------------------")
        
        #<$>#
        opcion = input("Ingresar: ")
        #$1
        if opcion == '1':

            suma = number1 + number2
            print("La Sumar es: ", suma)
            #exit()
        #$2
        elif opcion == '2':

            restar = number1 + number2
            print("La Resta es: ", restar)
            #exit()
        #$3
        elif opcion == '3':
            
            multiplicar = number1 * number2
            print("La Multiplicacion es: ", multiplicar)
            #exit()
        #$4
        elif opcion == '4':
            
            if number2 != 0:
                dividir = number1 / number2
                print("La Division es: ", dividir)	
                #exit()

        #$5
        elif opcion == '5':
            
            print("Saliendo del programa...")
            time.sleep(2)
            exit()

        #error$
        else: #vew e most,>> error
            
            print("Porfavor, ingrese la opcion correcta...")
            print("espere...    volviendo al opcion")
            time.sleep(2)