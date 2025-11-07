numero = int (input("Escriba un número: "))
if numero < 0:
    print("El numero digitado es negativo!")

if numero > 1 and numero < 10:
    print("El numero digitado esta entre 1 y el 10")

if numero == 0:
    print("El numero es cero")  
    print(f"Ha escrito el numero {numero}")
    numero = int(input("escriba un numero: "))
    if numero > 10:
        print(" SALUDOS!")
