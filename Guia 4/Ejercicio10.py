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