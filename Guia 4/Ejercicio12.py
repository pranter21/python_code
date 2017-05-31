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