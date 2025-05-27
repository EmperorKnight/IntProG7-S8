nombre = input(f"Introduzca su nombre completo \n-> ")

# "variable".split(" "): .split() sirve para omitir un simbolo de una cadena o de un entero introducido por el usuario
p_nombre, s_nombre, p_apellido, s_apellido = nombre.split(" ")

p_nombre2 = str(p_nombre)
s_nombre2 = str(s_nombre)
p_apellido2 = str(p_apellido)
s_apellido2 = str(s_apellido)

print(p_nombre2)
print(s_nombre2)
print(p_apellido2)
print(s_apellido2)

# # Covertir todo un texto en mayuscula se usa .upper():
# hola1 = nombre.upper()
# print(hola1)

# # Convertir todo un texto en minuscula se una .lower():
# hola2 = nombre.lower()
# print(hola2)

# # Convertir solo la primer letra de un texto en mayuscula se usa .capitalize():
# hola3 = nombre.capitalize()
# print(hola3)

# # Cambiar mayúsculas por minúsculas y viceversa se usa .swapcase(): 
# hola4 = nombre.swapcase()
# print(hola4)

# # Convertir un texto a formato título se usa .title():
# hola5 = nombre.title()
# print(hola5)

# # Comprobar si un texto está todo en mayúsculas se usa .isupper():
# hola6 = nombre.isupper()
# print(hola6)

# # Comprobar si un texto está todo en minuscula .islower():
# hola7 = nombre.islower()
# print(hola7)

# # Contar todos los caracteres se usa len("variable"):
# hola8 = len(nombre)
# print(hola8)

# # Contar ocurrencias de un carácter específico se usa .count():
# hola9 = nombre.count(" ")
# print(hola9)

# # Contar vocales:
# vocales = ["a","e","i","o","u"]
# vocal = 0
# h=hola2
# for x in h:
#     if x in vocales:
#         vocal += 1
# print(vocal)
