SALDO_CRC = 45897.00
NUR = "admin"
CR = "123"

# --- UTILIDADES ---

def limpiar_consola():
    """Simula la limpieza de la consola imprimiendo muchas líneas nuevas."""
    print('\n' * 50) 

def mostrar_mensaje_bienvenida():
    print("="*40)
    print("      ¡Banco Colom!       ")
    print("="*40)

def iniciar_sesion():
 
    limpiar_consola()
    print("--- INICIO DE SESIÓN ---")
    
    NUI = input("Ingrese su nombre de usuario : ")
    CI = input("Ingrese su contraseña : ")

    if NUI == NUR and CI == CR:
        print("\n¡Inicio de sesión exitoso!")

        return True
    else:
        print("\nError. Usuario o contraseña incorrectos.")

        return False

# --- OPERACIONES BANCARIAS ---

def consultar_saldo():
    """Muestra el saldo actual."""
    limpiar_consola()
    print("\n--- CONSULTA DE SALDO ---")
    # Utilizamos 'global' para acceder a la variable de saldo global
    print(f"\nSu saldo actual es: ₡{SALDO_CRC:,.2f} Colones.")
   

def depositar():
  
    while True:
        try:
            print("Saldo actual:45897 ₡ Colones.")
            monto = float(input("Ingrese la cantidad a depositar: "))

            if monto <= 0:
                print("Error: La cantidad debe ser positiva.")
                continue

            SALDO_CRC += monto
            print(f"\nDepósito de ₡{monto:,.2f} exitoso.")
            print(f"Nuevo saldo: ₡{SALDO_CRC:,.2f} Colones.")
        
            return
        except ValueError:
            print("Error: Ingrese un número válido.")

def retirar():
  
    global SALDO_CRC
    limpiar_consola()
    print("\n--- RETIRO DE DINERO ---")
    
    while True:
        try:
            print(f"Saldo actual: ₡{SALDO_CRC:,.2f} Colones.")
            monto = float(input("Ingrese la cantidad a retirar: "))

            if monto <= 0:
                print("Error: La cantidad debe ser positiva.")
            elif monto > SALDO_CRC:
                print("Error: Saldo insuficiente.")
            else:
                SALDO_CRC -= monto
                print(f"\nRetiro de ₡{monto:,.2f} exitoso.")
                print(f"Nuevo saldo: ₡{SALDO_CRC:,.2f} Colones.")
                input("Presione ENTER para volver al menú...")
                return
        except ValueError:
            print("Error: Ingrese un número válido.")

# --- BUCLE PRINCIPAL ---

def programa_principal():
    """Función principal que ejecuta el programa."""
    mostrar_mensaje_bienvenida()

    if not iniciar_sesion():
        return # Sale si el inicio de sesión falla

    while True:
        limpiar_consola()
        print("\n--- MENÚ BANCARIO Colom ---")
        print("1. Consultar Saldo")
        print("2. Depositar Dinero")
        print("3. Retirar Dinero")
        print("-" * 30)
        print("Presione 'X' para Salir del sistema.")
        print("-" * 30)

        opcion = input("Por favor, elija una opción (1, 2, 3 o X): ").strip().lower()

        if opcion == 'x':
            limpiar_consola()
            print("\nGracias por usar el Banco Simple. ¡Hasta luego!")
            break

        if opcion == '1':
            consultar_saldo()
        elif opcion == '2':
            depositar()
        elif opcion == '3':
            retirar()
        else:
            limpiar_consola()
            print("\nOpción inválida. Intente de nuevo.")

if __name__ == "__main__":
    programa_principal()
