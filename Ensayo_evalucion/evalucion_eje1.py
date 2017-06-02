estatura = float(input("ingresar estatura:\n"))
num_person = 0
femenino = 0
prom_maraton = 0
prom_estatura = 0
tiempo_mayor = 0
edad_menor = 999999
num_fem = 0
prom_tiempo = 0
prom_edad = 0

while estatura > 0:
    tiempo = float(input("ingresar el tiempo:\n"))
    genero = input("ingrese genero:\n")
    prom_estatura += estatura
    edad = int(input("ingrese la edad:\n"))
    prom_edad += edad
    num_person += 1
    if genero == "femenino":
        femenino += 1
    if tiempo_mayor < tiempo:
        tiempo_mayor = tiempo
    if edad_menor > tiempo:
        edad_menor = tiempo
    prom_tiempo += tiempo
    print('-------------------------------')
    estatura = float(input("ingrese altura:\n"))

num_fem = femenino * 100 / num_person
prom_tiempo = prom_tiempo / num_person
prom_estatura = prom_estatura / num_person
prom_edad = prom_edad / num_person
print("El numero de personas que llegaron a la meta:" + str(num_person))
print("El tiempo promedio de la maraton es: {:.1f}".format(prom_tiempo))
print("El promedio de la altura es: {:.1f}".format(prom_estatura))
print("El promedio de la edad de los atletas es {:.1f}".format(prom_edad))
print("El tiempo mayor en llegar a la meta es {}".format(tiempo_mayor))
print("La edad menor es {} ".format(edad_menor))
print("El porcentaje de mujeres que participaron en la maraton es {}%".format(num_fem))