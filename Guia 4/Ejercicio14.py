number1 = int(input('Ingrese numero \n'))
result_mod = number1 % 2
if result_mod == 0:
    result_mod = number1 + 1
    print('El impar siguiente es: ' + str(result_mod))
else:
    result_mod = number1 + 2
    print('El impar siguiente es: ' + str(result_mod))