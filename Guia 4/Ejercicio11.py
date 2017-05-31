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