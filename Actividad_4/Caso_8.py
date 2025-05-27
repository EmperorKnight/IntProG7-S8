# Caso 8: Registro de consumo eléctrico por edificio en la UAM
# Desarrolle un programa que permita registrar el consumo eléctrico de cinco edificios del campus
# UAM (como aulas, biblioteca, administración, laboratorios y cafetería) durante tres turnos del
# día (mañana, tarde y noche), por una semana. El programa debe mostrar el consumo por edificio
# y el total general semanal.

import os

edificios = 5
semana = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
semanal = []

for i in range(1,edificios+1):
    total_semana = 0
    for j in semana:
        turno_mañana = 0
        turno_nocturno = 0
        turno_tarde = 0
        os.system("cls || clear")
        print(f"En el edificio {i}, Dia: {j}")
        turno_mañana = float(input(f"Introduzca el consumo electrico del turno de la mañana \n-> "))
        turno_tarde = float(input(f"Introduzca el consumo electrico del turno de la tarde \n-> "))
        turno_nocturno = float(input(f"Introduzca el consumo electrico del turno nocturno \n-> "))
        
        total_semana += (turno_mañana + turno_tarde + turno_nocturno)
    semanal.append(total_semana)

os.system("cls || clear")

posicion = 0
for i in range(1,edificios+1):
    print(f"El consumo electrico del edificio {i} en la semana es de: {semanal[posicion]:,} kW")
    posicion += 1

total_semanal = 0
for j in semanal:
    total_semanal += j

print("---------------------------------------------------------------------")
print(f"El total general es de: {total_semanal:,} kW")