# Caso 1: Control de venta de vigorón en feria universitaria UAM
# Desarrolle un programa que permita simular la venta de vigorón durante una feria gastronómica
# organizada en la Universidad Americana, UAM Managua. El sistema debe solicitar la cantidad
# de clientes atendidos y, por cada cliente, cuántas porciones de vigorón compró, junto con el
# precio unitario por porción. El programa debe calcular el total pagado por cada cliente y mostrar
# el total de ventas de toda la feria. Utilice estructuras cíclicas anidadas.

import os

os.system("cls || clear")
print("Bienvenido a la feria de venta de vigorones de la UAM")
cant_clientes = int(input(f"Introduzca la cantidad de clientes atendidos\n-> "))

porciones_totales = 0
total_ganado = 0
montos_ganados_por_clientes = []

for i in range(1,cant_clientes+1):
    os.system("cls || clear")
    total_pagado = 0
    print(f"Introduzca la cantidad de porciones que compro el cliente numero {i}")
    porcion_cliente = int(input("-> "))
    print(f"Introduzca el precio unitario de cada porcion del cliente {i}")
    for j in range(1,porcion_cliente+1):
        precio_porcion = float(input(f"{j}) "))
        total_pagado += precio_porcion
        total_ganado += precio_porcion 
    montos_ganados_por_clientes.append(total_pagado)
    porciones_totales += porcion_cliente

os.system("cls || clear")
print(f"Pociones totales de vigorones vendidos: {porciones_totales:,}")
print(f"Total ganado en la feria: {total_ganado:,}\n ")

x = ""
m = 1

for x in montos_ganados_por_clientes:
    if x in montos_ganados_por_clientes:
        print(f"Monto pagado por el cliente {m} = {x:,}")
    m += 1
print(" ")