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