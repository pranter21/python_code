num = int(input("ingrese el numero\n"))
factorial = 1
while num > 1:
	factorial = factorial * num
	num -= 1
print(factorial)