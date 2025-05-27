# Caso 5: Encuesta sobre transporte estudiantil en la UAM
# Implemente un programa que simule una encuesta realizada en la UAM para conocer los medios
# de transporte utilizados por los estudiantes. Considere tres facultades, cada una con dos
# carreras, y en cada carrera se entrevistarán a cinco estudiantes. Por cada estudiante se debe
# registrar si utiliza bus, motocicleta, taxi, bicicleta o camina. Al final, se mostrarán los totales por
# medio de transporte, desglosados por facultad y el total general. Utilice estructuras cíclicas
# anidadas.

import os

facultades = ["1","2","3"]
uso_bus = []
uso_moto = []
uso_taxi = []
uso_bici = []
camina = []
total_general_bus = 0
total_general_moto = 0
total_general_taxi = 0
total_general_bici = 0
total_general_camina = 0

for i in facultades:
    os.system("cls || clear")
    total_bus = 0
    total_moto = 0
    total_taxi = 0
    total_bici = 0
    total_camina = 0
    print(f"En la facultad {i}")

    for j in range(1,3):
        print(f"En la carrera {j}")
        
        for m in range(1,6):
            print(f"Estudiante {m}")
            print(f"¿Que medio de transporte usas para llegar a la UAM?")
            print(f"Bus = B || Moto = M || Taxi = T || Bici = BC || Camina = C")
            aclaracion = input("-> ").strip().upper()
            if aclaracion == "B":
                total_bus += 1
            elif aclaracion == "M":
                total_moto += 1
            elif aclaracion == "T":
                total_taxi += 1
            elif aclaracion == "BC":
                total_bici += 1
            elif aclaracion == "C":
                total_camina += 1
        print(" ")
    
    uso_bus.append(str(total_bus))
    uso_moto.append(str(total_moto))
    uso_taxi.append(str(total_taxi))
    uso_bici.append(str(total_bici))
    camina.append(str(total_camina))

    total_general_bus += total_bus
    total_general_moto += total_moto
    total_general_taxi += total_taxi
    total_general_bici += total_bici
    total_general_camina += total_camina

uso_bus.append(str(total_general_bus))
uso_moto.append(str(total_general_moto))
uso_taxi.append(str(total_general_taxi))
uso_bici.append(str(total_general_bici))
camina.append(str(total_general_camina))

os.system("cls || clear")

posicion = 0
for l in facultades:
    print("---------------------------------------------------------------------")
    print(f"En la facultad {l}")
    print(f"Cantidad de estudiantes que hacen uso del bus: {uso_bus[posicion]}")        
    print(f"Cantidad de estudiantes que usan motos: {uso_moto[posicion]}")
    print(f"Cantidad de estudiantes que hacen uso de taxis: {uso_taxi[posicion]}")
    print(f"Cantidad de estudiantes que usan bicis: {uso_bici[posicion]}")
    print(f"Cantidad de estudiantes que caminan: {camina[posicion]}")
    posicion += 1
print("----------------------------------------------------------------------")
print(f"Cantidad general de estudiantes que hacen uso del bus: {uso_bus[3]}")
print(f"Cantidad general de estudiantes que usan motos: {uso_moto[3]}")
print(f"Cantidad general de estudiantes que hacen uso de taxis: {uso_taxi[3]}")
print(f"Cantidad general de estudiantes que usan bicis: {uso_bici[3]}")
print(f"Cantidad general de estudiantes que caminan: {camina[3]}")
print("----------------------------------------------------------------------")
