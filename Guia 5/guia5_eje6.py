tiempo = float(input('Ingrese tiempo:\n '))
num_person = 0
prom_tiempo = 0
tiempo_min = 100000
tiempo_max = 0
while tiempo > 0:
    num_person += 1
    prom_tiempo += tiempo
    if tiempo_min > tiempo:
        tiempo_min = tiempo
    if tiempo_max < tiempo:
        tiempo_max = tiempo
    tiempo = float(input('Ingrese tiempo:\n '))
    prom_tiempo = prom_tiempo / num_person
print('El numero de personas que llegaron fueron: ' + str(num_person))
print('El tiempo promedio de la maraton es: ' + str(prom_tiempo))
print('El tiempo menor es: ' + str(tiempo_min))
print('El tiempo mayor de la maraton es: ' + str(tiempo_max))
