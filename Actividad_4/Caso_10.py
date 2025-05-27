# Caso 10: Control de préstamos en la biblioteca de la UAM
# Desarrolle un programa que permita registrar los préstamos de libros en la biblioteca de la UAM.
# Se trabajará con cuatro categorías de libros (ingeniería, salud, derecho y literatura), cada una
# con tres subcategorías. Por cada subcategoría se registrarán los préstamos de cinco días. El
# sistema debe mostrar el total de préstamos por subcategoría, categoría y el total general
# semanal.

import os

categorias = ["Ingenieria","Salud","Derecho","Literatura"]
sub_categorias = 3
dias = 5
por_sub_categoria = []
por_categoria = []

os.system("cls || clear")
for i in categorias:
    total_categoria = 0
    for j in range(1,sub_categorias+1):
        total_dia = 0
        total_sub_categoria = 0
        print(f"En la categoria de {i}, en la subcategoria {j}")
        for k in range(1,dias+1):
            cant_prestamos = 0
            print(f"En el dia {k}")
            cant_prestamos = int(input("-> "))
            total_dia += cant_prestamos
        
        total_sub_categoria += total_dia
        por_sub_categoria.append(str(total_sub_categoria))
        os.system("cls || clear")

        total_categoria += total_sub_categoria

    por_categoria.append(str(total_categoria))
    os.system("cls || clear")

os.system("cls || clear")

posicion = 0
m = 1
posicion1 = 0

print(por_sub_categoria)

for x in por_sub_categoria:
    if m == 4:
        m = 1

    
        
    print(f"En la subcategoria {m}")
    print(f"Se prestaron {por_sub_categoria[posicion]} libros")
    print(" ")

    posicion += 1
    m += 1

print(" ")