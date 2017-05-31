canti_estud = int(input('Ingrese numero de estudiantes \n'))
cant_notas = 0
cant_roja = 0
porcentaje_notas_rojas = 0
for i in range(canti_estud):
    notas_estud = float(input('Ingrese nota \n'))
    if notas_estud < 4.0:
        cant_roja += 1
    cant_notas += notas_estud
porcentaje_notas_roja = cant_roja * 100 / canti_estud
prom_estud = cant_notas / canti_estud

print('Porcentaje de notas rojas ' + str(porcentaje_notas_roja) + "%")
print('El promedio de los estudiantes es ' + str(prom_estud))
