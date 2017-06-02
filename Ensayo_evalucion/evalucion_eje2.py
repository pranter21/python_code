nota_entre = 0
nota_roja = 0
nota_azul = 0
alumnos = 40
for i in range(alumnos):
    nota = float(input("ingrese nota del alumno:\n"))
    if nota < 4.0:
        nota_roja += 1
    else:
        nota_azul += 1
    if nota > 3.5 and nota < 4.0:
        nota_entre += 1
por_nota_roja = nota_roja * 100 / alumnos
por_nota_azul = nota_azul * 100 / alumnos
print("porcentaje de notas rojas es: %",(por_nota_roja))
print("porcertaje de notas azules es: %",(por_nota_azul))
print("numero de notas entre el 3.5 y 4.0 es:",(nota_entre))