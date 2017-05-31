def suma_1(A, B):
	return A + B
def suma_2 (A, B):
    total = A + B
    print("El Resultado Es:", total)

num1 = int(input("ingrese el valor de numero 1:"))
num2 = int(input("ingrese el valor del numero 2:"))

print("suma dos numeros, metodo 1")
print("El resultado es: ", suma_1(num1,num2))

print("\nSuma dos numeros, metodo 2")
suma_2(num1, num2)