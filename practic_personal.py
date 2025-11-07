\
\
#library for system
import time #import the library time

#library for local files
#import form1.password # option mode is /form1/password.py


while True:

	print(" __________________________________________________________________")
	print(" |          Bienvenido a la CMD/comando de App de xixi            |")
	print(" |````````````````````````````````````````````````````````````````|")
	print(" |       Seleccione un opcion de modo para abrir apps-cmd         |")
	print(" ——————————————————————————————————————————————————————————————————")
	print(" .              1. Calculadora básica de xixi                     .")
	print(" .              2. un contraseña de xixi (con libreria)           .")
	print("                                                                   ")
	print(" .              0. Salir de la cmd-app                            .")
	print(" .               a. [info] de la app de xixi                      .")
	print(" ——————————————————————————————————————————————————————————————————")
	print(" ")
	#select option
	select_option= input("Ingrese la opcion: ")
	print(" ")


	# app mode .1
	if select_option == '1':
		
		print("------------------------------------------------------")
		print("|   Quieres mostrar número entero o por decimales?   |")
		print("------------------------------------------------------")
		print("|  1. Entero   {int}                                 |")
		print("|  2. Decimal  {float}                               |")
		print("|                                                    |")
		print("|  0.volver     [Exit]                               |")
		print("------------------------------------------------------")
		print(" ")
		#<$>#
		select_number = input("Ingresar: ")
		
		#$1
		if select_number == '1':

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
		elif select_number == '2':
			
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

		# exit app mode .0
		elif select_option == '0':
		
			print("Saliendo de la cmd-app...")
			time.sleep(2)
			exit()

	# app mode .2
	elif select_option == '2':
		print("end ")


	

	if select_option == 'a':

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
			exit = input("Presione Enter para volver al inicio...      >> ")  # return to the .main menu
			print(" ") #space

			if exit == '1':
				print("Volviendo al inicio...")
				time.sleep(2)
				break
			#error$
			else:
				print(" ! Porfavor, ingrese la opcion correcta... !")
				print("espere...    volviendo al opcion")
				time.sleep(2)


	#$0
	elif select_option == '0':
					
		print("Saliendo del programa...")
		time.sleep(2)
		exit()

	#$0s
	elif select_option == '0':
					
		print("Saliendo del programa...")
		time.sleep(2)
		exit()

	#error$
	else: #vew e most,>> error
				
		print("Porfavor, ingrese la opcion correcta...")
		print("espere...    volviendo al opcion")
		time.sleep(2)







