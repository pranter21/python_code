horas_trab = float(input("Horas trabajadas:\n"))
n_trab = 0
suldo_prom = 0
prom_h = 0

while horas_trab > 0:
        valor_hora = float(input("Valor por hora trabajada:\n"))
        cargas = int(input(" Ingrese el numero de cargas:\n"))
        sueldo_n = horas_trab * valor_hora
        if cargas > 3:
            sueldo_n *= 1.12
        if cargas == 1 or cargas == 2:
            sueldo_n *= 1.07
        suldo_prom += sueldo_n
        prom_h += horas_trab
        print("El sueldo de trabajador es:", (sueldo_n))
        n_trab += 1
        horas_trab = float(input("Horas trabajadas:\n"))
prom_h / n_trab
print("El sueldo promedio de los trabajadores es:",(suldo_prom))
print("El promedio de horas trabajadas es:",(prom_h))