# Caso 2: Registro semanal de gastos de estudiantes UAM
# Cree un programa que simule el control de gastos semanales de un grupo de estudiantes de
# primer año de la UAM. El sistema debe procesar datos de 4 semanas, y por cada semana,
# ingresar el gasto realizado cada día (7 días por semana). El programa debe calcular el total
# gastado por semana y el total acumulado del mes. Utilice bucles anidados para recorrer
# semanas y días.

import os

semanas = 4
dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
gasto_semana = []
dia = ""
total_mes = 0

os.system("cls || clear")
print(f"Bienvenidos primer año de la Universidad UAM")
for i in range(1,semanas+1):
    total_semana = 0
    print(f"Introduzca el gasto realizado durante la semana") 
    print(f"Semana {i}")
    for dia in dias:
        gasto_dia = float(input(f"{dia} -> C$"))
        total_semana += gasto_dia
    
    total_mes += total_semana
    gasto_semana.append(total_semana)

    os.system("cls || clear")

os.system("cls || clear")
print(f"-------------------------------------------------------------")
print(f"Total del mes: C${total_mes:,}")
print(f"-------------------------------------------------------------")

m = 1
for x in gasto_semana:
    print(f"El gasto total de la semana {m}: C${x:,}")
    m += 1
print(f"-------------------------------------------------------------")


    