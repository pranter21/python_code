numero1 = int(input("inegrese el Numero 1:\n"))
numero2 = int(input("ingrese el Numero 2:\n"))
numero3 = int(input("ingrese el Nummero 3:\n"))
suma = numero1 + numero2
suma2 = numero1 + numero3
div_suma2 = suma2 / numero2
elevado = numero1 ** numero2 / numero3
numero_par = numero1 % numero2
print("Este es el resultado de la suma de N 1 y N 2:\n" + str(suma))
print("Este el resultado de suma N 1 y N 3 divido por n 2:\n" + str(int(div_suma2)))
print("Esta es el resultado de N 1 elevado por n 2 y dividido por n 3:\n" + str(int(elevado)))
print("numeros par:\n" + str(numero_par))
