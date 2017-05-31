def ejercicio_1():
    radio = int(input("ingrese el radio\n"))
    pi = 3.14
    diametro = 2 * radio
    perimetro = 2*radio * pi
    area = pi * radio ** 2
    print("el diametro es:" + str(diametro))
    print("el perimetro es:" + str(perimetro))
    print("el area es:" + str(area))

def ejercicio_2():	
	numero1 = int(input("inegrese el Numero 1:\n"))
	numero2 = int(input("ingrese el Numero 2:\n"))
	numero3 = int(input("ingrese el Nummero 3:\n"))
	suma = numero1 + numero2
	suma2 = numero1 + numero3
	div_suma2 = suma2 / numero2
	elevado = numero1 ** numero2 / numero3
	numero_par = numero1 % numero2
	print("Este es el resultado de la suma de N 1 y N 2:\n" + str(suma))
	print("Este el resultado de suma N 1 y N 3 divido por n 2:\n" + str(int(div_suma2)))
	print("Esta es el resultado de N 1 elevado por n 2 y dividido por n 3:\n" + str(int(elevado)))
	print("numeros par:\n" + str(numero_par))

def ejercicio_3():
	prom_nota_alum = float(input("Ingrese el Promedio de Nota Del Alumno:\n"))
	nota_exam = float(input("Ingrese la calificacion del examen del alumno:\n"))
	Nota_final = prom_nota_alum * 0.7 + nota_exam * 0.3
	if Nota_final >= 4:
		print("Aprobado")
	else:
		print("Reprobado")

def ejercicio_4():
	number = int(input('Ingrese un numero \n'))
	result = number % 2
	if result == 0:
		print('El numero ' + str(number) + ' es par')
	else:
		print('El numero ' + str(number) + ' es impar')

def ejercicio_5():
	number = int(input('Ingrese un numero \n'))
	result = number % 2
	if result == 0:
        mod_result = number - 1
        print('El antecesor de ' + str(number) + ' es ' + str(mod_result))
	else:
        mod_result = number + 1
        print('El sucesor de ' + str(number) + ' es ' + str(mod_result))

def ejercicio_6():
	num1 = int(input("Ingrese Numero 1:\n"))
	num2 = int(input("Ingrese Numero 2:\n"))
	if num1 > num2:
        print('El numero ' + str(num2) + ' es menor que ' + str(num1))
	else:
    	print('El numero ' + str(num1) + ' es menor que ' + str(num2))

def ejercicio_7():
	horas_trab = int(input('Ingrese hocmdras de trabajo \n'))
	valor_hora = int(input('Ingrese valor de hora \n'))
	num_cargas = int(input('Ingrese numero de carga \n'))
	suledo = horas_trab * valor_hora
	if num_cargas >= 3:
    	con_bono = suledo * 1.1
    	print('El salario final es $' + str(int(con_bono)))
	elif num_cargas == 2:
    	con_bono = suledo * 1.05
    	print('El salario final es $' + str(int(con_bono)))
	else:
    	con_bono = suledo * 1.03
    	print('El salario final es $' + str(int(con_bono)))

def ejercicio_8():
	num1 = int(input('Ingrese numero \n'))
	num2 = int(input('Ingrese numero \n'))
	num3 = int(input('Ingrese numero \n'))
	num4 = int(input('Ingrese numero \n'))
	if  num1 < num2 and num1 < num3 and num1 < num4:
    	print('El numero menor es ' + str(num1))
	elif num2 < num1 and num2 < num3 and num2 < num4:
    	print('El numero menor es ' + str(num2))
	elif num3 < num2 and num3 < num1 and num3 < num4:
    	print('El numero menor es ' + str(num3))
	elif num4 < num2 and num4 < num3 and num4 < num1:
    	print('El numero menor es ' + str(num4))

def ejercicio_9():
	num1 = int(input("ingrese el numero 1:\n"))
	num2 = int(input("ingrese el numero 2:\n"))
	num3 = int(input("ingrese el numero 3:\n"))
	num4 = int(input("ingrese el numero 4:\n"))
	if  num1 > num2 and num1 > num3 and num1 > num4:
	  print('El numero mayor es ' + str(num1))
	elif num2 > num1 and num2 > num3 and num2 > num4:
    	print('El numero mayor es ' + str(num2))
	elif num3 > num2 and num3 > num1 and num3 > num4:
    	print('El numero mayor es ' + str(num3))
	elif num4 > num2 and num4 > num3 and num4 > num1:
    	print('El numero mayor es ' + str(num4))

def ejercicio_10():
	horas_trab = int(input('Ingrese horas de trabajo \n'))
	valor_hr = int(input('Ingrese valor de hora \n'))
	num_cargas = int(input('Ingrese numero de carga \n'))
	mujer = input('Ingrese su genero \n')
	sueldo = horas_trab * valor_hr

	if mujer == 'femenino':
    	sueldo = sueldo * 1.05
    	print('Salario con reajuste de genero $' + str(sueldo))
	else:
    	sueldo = sueldo * 1.03
    	print('Salario con reajuste de genero $' + str(sueldo))

	if num_cargas >= 3:
    	sueldo_bono = sueldo * 1.1
    	print('El salario final es $' + str(int(sueldo_bono)))
	elif num_carga == 2:
    	sueldo_bono = sueldo * 1.05
    	print('El salario final es $' + str(int(sueldo_bono)))
	else:
    	sueldo_bono = sueldo * 1.03
    	print('El salario final es $' + str(int(sueldo_bono)))

def ejercicio_11():
	num1 = int(input('Ingrese numero \n'))
	num2 = int(input('Ingrese numero \n'))
	print('Ingrese operacion a realizar \n 1: suma \n 2: resta \n 3: multiplicacion \n 4: division')
	opcion = int(input('Ingresar opcion : '))
	if opcion == 1:
    	resultado = num1 + num2
    	print(' * El resultado es ' + str(resultado))
	elif opcion == 2:
    	resultado = num1 - num2
    	print(' * El resultado es ' + str(resultado))
	elif opcion == 3:
    	resultado = num1 * num2
    	print(' * El resultado es ' + str(resultado))
	elif opcion == 4:
    	resultado = num1 / num2
    	print(' * El resultado es ' + str(resultado))
	else:
    	print('ninguna opcion elegida')

def ejercicio_12():
	number1 = int(input('Ingrese un numero \n'))
	number2 = int(input('Ingrese un numero \n'))
	if number1 > number2:
    	result = number1 * number2
    	print('El resultado es ' + str(result))
	if number2 > number1 and number2 != 0:
    	result = number1 / number2
    	print('El resultado es ' + str(result))
	if number2 == 0:
    	print('No se puede calcular')

def ejercicio_14():
    number1 = int(input('Ingrese numero \n'))
    result_mod = number1 % 2
    if result_mod == 0:
        result_mod = number1 + 1
        print('El impar siguiente es: ' + str(result_mod))
    else:
        result_mod = number1 + 2
        print('El impar siguiente es: ' + str(result_mod))

def ejercicio_15():
    num1 = int(input("Ingrese el numero 1:\n"))
    num2 = int(input("Ingrese el numero 2:\n"))
    num3 = int(input("Ingrese el numero 3:\n"))
    if num1 > num2 and num1 < num3 or num1 > num3 and num1 < num2:
        print('El valor intermedio es ' + str(num1))
    elif num2 > num3 and num2 < num1 or num2 > num1 and num2 < num3:
        print('El valor intermedio es ', str(num2))
    elif num3 > num2 and num3 < num1 or num3 < num2 and num3 > num1:
        print('El valor intermedio es ' + str(num3))
opcion = 100
while(opcion !="16"):
    print("menu principal\n")
    print("1. Ejecutar Ejecercio_1\n")
    print("2. Ejecutar Ejercicio_2\n")
    print("3. Ejecutar Ejercicio_3\n")
    print("4. Ejecutar Ejercicio_4\n")
    print("5. Ejecutar Ejercicio_5\n")
    print("6. Ejecutar Ejercicio_6\n")
    print("7. Ejecutar Ejercicio_7\n")
    print("8. Ejecutar Ejercicio_8\n")
    print("9. Ejecutar Ejercicio_9\n")
    print("10. Ejecutar Ejercicio_10\n")
    print("11. Ejecutar Ejercicio_11\n")
    print("12. Ejecutar Ejercicio_12\n")
    print("13. Ejecutar Ejercicio_13\n")
    print("14. Ejecutar Ejercicio_14\n")
    print("15. Ejecutar Ejercicio_15\n")
    print("16. Salir")
    opcion = input("ingrese una opcion:\n ")
    if opcion == "1":
        ejercicio_1()
    elif opcion == "2":
        ejercicio_2()
    elif opcion == "3":
    	ejercicio_3()
    elif opcion == "4":
    	ejercicio_4()
    elif opcion == "5":
        ejercicio_5()
    elif opcion == "6":
        ejercicio_6()
    elif opcion == "7":
        ejercicio_7()
    elif opcion == "8":
        ejercicio_8()
    elif opcion == "9":
        ejercicio_9()
    elif opcion == "10":
        ejercicio_10()
    elif opcion == "11":
        ejercicio_11()
    elif opcion == "12":
        ejercicio_12()
    elif opcion == "13":
        ejercicio_13()
    elif opcion == "14":
        ejercicio_14()
    elif opcion == "15":
        ejercicio_15()
    else:
        print("opcion no correcta\n")
print("\nFin del programa")
