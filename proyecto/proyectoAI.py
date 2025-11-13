
#*Formula los objetivos específicos(3)#
#1.Permitir al usuario ingresar productos, cantidades y precios.
#2.Calcular automaticamente el total de la venta y aplicar descuentos si corresponde.
#3.Mostrar un resumen de la venta con los datos ingresados.
import time
#import os
productos = []
cantidades = []
precios = []
total_venta = 0.0
descuento = 0.0
def agregar_producto():
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    productos.append(producto)
    cantidades.append(cantidad)
    precios.append(precio)
    print(f"Producto {producto} agregado exitosamente.")
def calcular_total():
    global total_venta, descuento
    total_venta = sum(cantidades[i] * precios[i] for i in range(len(productos)))
    if total_venta > 100:
        descuento = total_venta * 0.1
        total_venta -= descuento
def mostrar_resumen():
    print("\nResumen de la venta:")
    for i in range(len(productos)):
        print(f"{productos[i]} - Cantidad: {cantidades[i]}, Precio: {precios[i]}")
    print(f"Descuento aplicado: ${descuento:.2f}")
    print(f"Total de la venta: ${total_venta:.2f}")
def main():
    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Calcular total de la venta")
        print("3. Mostrar resumen de la venta")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            calcular_total()
            print("Total calculado exitosamente.")
        elif opcion == "3":
            mostrar_resumen()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
if __name__ == "__main__":
    main()