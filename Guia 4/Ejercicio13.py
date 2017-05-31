salary = int(input('Ingrese Sueldo \n'))
number_cargo = int(input('Ingrese Numero de cargas \n'))
if number_cargo >= 2:
    salary = salary * 1.2
    print('El salario es: $' + str(salary))
elif number_cargo == 1:
    salary = salary * 1.1
    print('El salario es: $' + str(salary))
else:
    salary = salary * 1.05
    print('El salario es: $' + str(salary))