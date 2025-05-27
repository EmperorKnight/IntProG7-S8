# Caso 4: Registro de participación estudiantil por carrera en la UAM
# Desarrolle un programa que registre la participación de estudiantes de la UAM en actividades
# extracurriculares por carrera. Considere tres carreras (por ejemplo: Sistemas, Marketing y
# Derecho), cada una con tres años académicos, y cada año con dos secciones. Por cada
# sección, se debe registrar cuántos estudiantes participaron. El programa debe mostrar el total
# por carrera y el total general de participantes. Utilice bucles anidados.

import os

carreras = []
total_por_carrera = []

os.system("cls || clear")

cant_carreras = int(input(f"Introduzca la cantidad de carreras a evaluar \n-> "))

i = 1 
while i <= cant_carreras:
    os.system("cls || clear")
    carrera = input(f"Escriba la carrera \n-> ").strip().capitalize()
    carreras.append(carrera)
    i += 1

total_general = 0

for i in carreras:
    os.system("cls || clear")
    print(f"Introduzca la cantidad de estudiantes de la carrera de {i}")
    total_carrera = 0
    for x in range(1,4):
        print(f"Año {x}")
        cant_estudiantes = int(input(f"-> "))
        total_carrera += cant_estudiantes
        print(" ")
        
        total_general += cant_estudiantes
    total_por_carrera.append(str(total_carrera))

os.system("cls || clear")
print(f"La cantidad total de estudiantes que participaron en actividades extracurriculares son: {total_general} estudiantes")

print("-------------------------------------------------------------------------------------------------------")


for m in carreras:
    posicion = 0
    for j in total_por_carrera:
        print(f"En la carrera de {m} participaron {j[posicion]} estudiantes")
        posicion += 1
        break
print("-------------------------------------------------------------------------------------------------------")