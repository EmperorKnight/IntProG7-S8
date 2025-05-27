# Caso 6: Registro de ventas de nacatamales en eventos de domingo en la UAM
# Cree un programa que simule la venta de nacatamales durante cuatro domingos consecutivos
# en actividades realizadas en la UAM (como torneos, convivencias o ferias). Por cada domingo,
# se deberá registrar la cantidad de clientes y cuántos nacatamales compró cada uno. El
# programa debe calcular el total vendido por domingo y el acumulado mensual. Utilice bucles
# anidados para domingos y clientes.

import os

domingos = 4
domingos_clientes = []
domingos_ventas = []
actividad_UAM = []
total_mensual = 0
total_mensual_clientes = 0

for i in range(1,domingos+1):
    os.system("cls || clear")
    total_vendido = 0
    cant_clientes = 0
    print(f"Domingo {i}")
    cant_clientes = int(input(f"Introduzca la cantidad de clientes del domingo {i} \n-> "))
    domingos_clientes.append(cant_clientes)
    total_mensual_clientes += cant_clientes
    print(f" \nIntroduzca la cantidad de nacatamales que compro cada cliente")
    for j in range(1,cant_clientes+1):
        cant_nacatamales = 0
        cant_nacatamales = int(input(f"Cliente {j}: "))
        total_vendido += cant_nacatamales

    total_mensual += total_vendido 
    domingos_ventas.append(total_vendido)

os.system("cls || clear")

posicion = 0
for k in range(1,domingos+1):
    print("---------------------------------------------------------------------")
    print(f"En el domingo {k}")
    print(f"Se le vendio a {domingos_clientes[posicion]} clientes y se vendio un total de {domingos_ventas[posicion]} nacatamales")
    posicion += 1

print("---------------------------------------------------------------------")
print(f"En este mes se le vendio a un total de {total_mensual_clientes:,} clientes y se vendio un total de {total_mensual:,} nacatamales")
print("---------------------------------------------------------------------")
