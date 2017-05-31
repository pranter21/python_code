num = int(input('Ingrese numero:\n'))
resul_mod = num % 2
if resul_mod == 0:
    num -= 1
for i in range(1, 100):
    num += 2
    if num < 100:
        print(num)
