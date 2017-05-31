num1 = int(input("Ingrese el numero 1:\n"))
num2 = int(input("Ingrese el numero 2:\n"))
num3 = int(input("Ingrese el numero 3:\n"))
if num1 > num2 and num1 < num3 or num1 > num3 and num1 < num2:
    print('El valor intermedio es ' + str(num1))
elif num2 > num3 and num2 < num1 or num2 > num1 and num2 < num3:
    print('El valor intermedio es ', str(num2))
elif num3 > num2 and num3 < num1 or num3 < num2 and num3 > num1:
    print('El valor intermedio es ' + str(num3))