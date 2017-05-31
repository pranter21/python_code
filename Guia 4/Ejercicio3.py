prom_nota_alum = float(input("Ingrese el Promedio de Nota Del Alumno:\n"))
nota_exam = float(input("Ingrese la calificacion del examen del alumno:\n"))
Nota_final = prom_nota_alum * 0.7 + nota_exam * 0.3
if Nota_final >= 4:
    print("Aprobado")
else:
    print("Reprobado")