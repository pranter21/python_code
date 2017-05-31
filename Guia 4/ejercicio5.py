number = int(input('Ingrese un numero \n'))
result = number % 2
if result == 0:
    mod_result = number - 1
    print('El antecesor de ' + str(number) + ' es ' + str(mod_result))
else:
    mod_result = number + 1
    print('El sucesor de ' + str(number) + ' es ' + str(mod_result))