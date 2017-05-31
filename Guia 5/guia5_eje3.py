for i in range (2)
	h_trab = int(input("ingrese horas trabajadas\n"))
	v_hora = int(input("ingrese el valor de horas trabajadas\n"))
	n_carga = int(input("ingrese cantidad de cargas\n"))
	sueldo = h_trab * v_hora
	if n_carga >= 3:
		sueldo = sueldo * 1.1
	elif n_carga == 1 or n_carga == 2:
		sueldo = sueldo * 1.05
	sueldo_c += sueldo
	print("El sueldo del trabajador es: " + str(int(sueldo)))
print("El sueldo total a pagar es: + " + str(int(sueldo_c)))