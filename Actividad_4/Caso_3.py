# Caso 3: Cálculo de promedio académico en la UAM
# Elabore un programa que procese las calificaciones de varios estudiantes de la carrera de
# Ingeniería en Sistemas de la Información en la UAM. Por cada estudiante, se ingresarán las
# calificaciones de tres asignaturas, y cada asignatura incluirá tres tareas y un examen. El
# programa debe calcular el promedio por asignatura y el promedio general del estudiante. Utilice
# estructuras cíclicas anidadas para manejar estudiantes, asignaturas y evaluaciones.

import os

os.system("cls || clear")
cant_estudiantes = int(input(f"Introduzca la cantidad de estudiantes a calificar \n-> "))

cant_asignaturas = 3
i = 1
promedio_por_asignatura = []
promedios_generales = []

os.system("cls || clear")

while i <= cant_estudiantes:
    promedio_general = 0
    print(f"Introduzca las notas del estudiante {i}\n ")
    for j in range(1,cant_asignaturas+1):
        promedio_asignatura = 0
        print(f"Asignatura {j}")
        tarea_1 = float(input(f"Introduzca la nota de la tarea 1 \n-> "))
        tarea_2 = float(input(f"Introduzca la nota de la tarea 2 \n-> "))
        tarea_3 = float(input(f"Introduzca la nota de la tarea 3 \n-> "))
        examen = float(input(f"Introduzca la nota del examen de la asignatura \n-> "))
        print(" ")
        
        promedio_asignatura = tarea_1 + tarea_2 + tarea_3 + examen
        promedio_general += promedio_asignatura
        promedio_por_asignatura.append(str(promedio_asignatura))
    
    promedios_generales.append(str(promedio_general/3))
    i += 1
    os.system("cls || clear")

print("-------------------------------------------------------")

m = 1
for x in promedios_generales:
    print(f"El promedio general del estudiante {m} es {x}")
    m += 1

print("-------------------------------------------------------")

a = 0
k = 1

for j in promedio_por_asignatura:
    a += 1
    print(f"En la asignatura {a} el estudiante {k} obtuvo {j}")
    if a == 3:
        a = 0
        k += 1
        print("-------------------------------------------------------")
    