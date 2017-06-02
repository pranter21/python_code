num = int(input("Ingrese numero:\n"))
resto = num % 2

if resto == 1:
    num -= 1

while num < 100:
    num += 2
    print(num)