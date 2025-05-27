# Caso 7: Control de ventas en kioscos estudiantiles de la UAM
# Implemente un programa que simule el control de ventas de alimentos en tres kioscos dentro
# del campus UAM. Cada kiosco ofrece cinco productos diferentes y se registrarán las ventas
# durante cuatro días. El programa debe calcular y mostrar el total vendido por producto en cada
# kiosco, así como el total general por día.

import os

kioscos = 3
productos = 5
dias = 4
ventas_producto = []
total_ventas_dia = []

for i in range(1,kioscos+1):
    os.system("cls || clear")
    print(f"En el kiosco {i}")
    for j in range(1,dias+1):
        total_productos = 0
        total_dia = 0
        print(f"En el dia {j}")
        print(f"Introduzca la cantidad de veces que se vendio cada producto")
        for k in range(1,productos+1):
            cant_producto = 0
            cant_producto = int(input(f"Producto {k}: "))
            ventas_producto.append(cant_producto)
            total_productos += cant_producto
        print(" ")

        total_dia = total_productos
        total_ventas_dia.append(total_dia)

os.system("cls || clear")
posicion = 0
p = 0
for l in range(1,kioscos+1):
    print("---------------------------------------------------------------------")
    print(f"En el kiosco {l}")
    for h in range(1,dias+1):
        print(f"En el dia {h}")
        for u in range(1,productos+1):
            print(f"El producto {u} se vendio {ventas_producto[posicion]} veces")
            posicion += 1
        print(f"El total general del dia es de {total_ventas_dia[p]}\n ")
        p += 1

