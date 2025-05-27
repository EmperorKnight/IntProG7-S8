# Caso 9: Evaluación del acceso a internet en hogares de estudiantes
# Implemente un programa que simule una encuesta realizada a estudiantes de la UAM para
# conocer su acceso a internet en casa. Se trabajará con tres carreras, cada una con tres grupos,
# y se entrevistará a cinco estudiantes por grupo. Se debe registrar si el estudiante tiene acceso
# estable, intermitente o no tiene internet. Al final, mostrar un conteo de cada tipo de acceso por
# carrera y el total general.

import os

carreras = 3
grupos = 3
estudiantes = 5
internet_estable = []
internet_intermitente = []
sin_internet = []

for i in range(1,carreras+1):
    total_estable = 0
    total_intermitente = 0
    total_sin = 0

    for j in range(1,grupos+1):
        os.system("cls || clear")
        estable = 0
        intermitente = 0
        sin = 0
        print(f"En la carrera {i}, en el grupo {j}")
        
        for n in range(1,estudiantes+1):
            print(f"¿Posee acceso a internet?")
            print("Internet estable = ie || Internet intermitente = ii || Sin internet = si")
            aclaracion = input(f"Estudiante {n}: ").strip().lower()
            print(" ")
            if aclaracion == "ie":
                estable += 1
            elif aclaracion == "ii":
                intermitente += 1
            elif aclaracion == "si":
                sin += 1
                
        total_sin += sin
        total_estable += estable
        total_intermitente += intermitente


    internet_estable.append(total_estable)
    internet_intermitente.append(total_intermitente)
    sin_internet.append(total_sin)

os.system("cls || clear")
posicion = 0
for i in range(1,carreras+1):
    print("---------------------------------------------------------------------")
    print(f"La carrera {i} posee: ")
    print(f"{internet_estable[posicion]} estudiantes con internet estable en su casa")
    print(f"{internet_intermitente[posicion]} estudiantes con internet intermitente en su casa")
    print(f"{sin_internet[posicion]} estudiantes sin internet")  

total_general_estable = 0
for i in internet_estable:
    total_general_estable += i

total_general_intermitente = 0
for j in internet_intermitente:
    total_general_intermitente += j

total_general_sin = 0
for k in sin_internet:
    total_general_sin += k

print("---------------------------------------------------------------------")
print(f"Total de estudiantes con acceso a internet en su casa:")
print(f"{total_general_estable:,} estudiantes con internet estable")
print(f"{total_general_intermitente:,} estudiantes con internet intermitente")
print(f"{total_general_sin:,} estudiantes sin acceso a internet")
print("---------------------------------------------------------------------")     
            