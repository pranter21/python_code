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