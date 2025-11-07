num1 = float(input('Intruduce su primer numero: '))           
num2 = float(input('Introduce un segundo numero: '))

cr=divmod (num1, num2)
print('El resultado es de.....',cr)

coin = input('Desea continuar? (s/n): ')


if coin == 's':
    num1 = float(input('Intruduce su primer numero: '))           
    num2 = float(input('Introduce un segundo numero: '))
elif coin == 'n':
    print('Gracias por usar el programa')