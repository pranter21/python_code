horas_trab = int(input('Ingrese horas de trabajo \n'))
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