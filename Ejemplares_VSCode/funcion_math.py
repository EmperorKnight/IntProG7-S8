import math

radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

area_base = math.pi * (radio ** 2)
volumen = area_base * altura

area_lateral = 2 * math.pi * radio * altura
area_superficial = area_lateral + 2 * area_base

print("\n--- RESULTADOS ---")
print(f"Radio del cilindro: {radio}")
print(f"Altura del cilindro: {altura}")
print(f"Volumen del cilindro: {volumen:.2f} unidades cúbicas")
print(f"Área superficial del cilindro: {area_superficial:.2f} unidades cuadradas")