opcion = 100
while(opcion !="5"):
	print("menu principal\n")
	print("1.Ejecuta Ejecercio14\n")
	print("2.Ejecuta Ejercicio15\n")
	print("5.Salir")
	opcion = input("ingrese una opcion: ")
	if opcion == "1":
        Ejecercio14()
	elif opcion == "2":
        Ejercicio15()
	else:
	    print("opcion no correcta\n")
print("\nFin del programa")