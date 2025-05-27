#len("lista"): devuelve la cantidad de elementos de una lista
n=[1,2,2]
print(len(n)) 

#"lista".index() devuelve la posicion en la lista del elemento que seleccionamos (se le puede sumar)
o = [1,2,2]
print(o.index(1)+1) 

#"LISTA".append(): coloca el elemento introducido al final de la lista
m = []
m.append(1)
m.append(2)
m.append(3)
print(m)

#"LISTA".extend(): permite colocar multiples elementos a una lista
l = []
l.extend([1,2,3,"Azucar"])
print(l)

#modificar elementos
k = [1,2,3]
k[1] = 4
print(k)

#"LISTA".remove(): elemina un elemento especifico de la lista
p = [1,2,3]
p.remove(2)
print(p)

#se le denomina "element" a un indice en una lista 
list = [-4,-3,-2,-1,0,1,2,3,4]
pares = []
impares = []
for x in list:
    if x % 2 == 0:
        pares += [x]
    else:
        impares += [x]
print(pares)
print(impares)





# El método .join() en Python se utiliza principalmente con iterables de cadenas para unirlos en una sola cadena, 
# usando una cadena separadora. Aquí tienes una lista de todos los usos comunes y posibles escenarios donde .join() 
# puede ser útil:

# 1. Unir listas de cadenas
nombres = ["Ana", "Luis", "Carlos"]
resultado = ", ".join(nombres)  # "Ana, Luis, Carlos"

# 2. Unir tuplas de cadenas
tupla = ("Hola", "mundo")
resultado = " ".join(tupla)  # "Hola mundo"

# 3. Unir caracteres individuales
letras = ['P', 'y', 't', 'h', 'o', 'n']
resultado = "".join(letras)  # "Python"

# 4. Unir elementos con saltos de línea
lineas = ["Línea 1", "Línea 2", "Línea 3"]
resultado = "\n".join(lineas)
# Resultado:
# Línea 1
# Línea 2
# Línea 3

# 5. Unir elementos numéricos convertidos a string
numeros = [1, 2, 3]
resultado = " - ".join(str(num) for num in numeros)  # "1 - 2 - 3"

# 6. Unir claves de un diccionario
diccionario = {"a": 1, "b": 2}
resultado = ", ".join(diccionario)  # "a, b"

# 7. Unir valores de un diccionario
resultado = ", ".join(str(valor) for valor in diccionario.values())  # "1, 2"

# 8. Unir con diferentes separadores
"".join(["123", "456"])         # "123456"
"-".join(["2025", "05", "10"])  # "2025-05-10"
"***".join(["A", "B", "C"])     # "A***B***C"

# 9. Unir nombres o palabras para formar rutas, URLs, o frases
rutas = ["home", "usuario", "documentos"]
ruta_completa = "/".join(rutas)  # "home/usuario/documentos"

# 10. Unir resultados de una función o filtro
palabras = ["esto", "es", "", "una", "", "prueba"]
resultado = " ".join(p for p in palabras if p)  # "esto es una prueba"

# Casos donde NO puedes usar .join() directamente
# No puedes usar .join() directamente en listas de enteros o flotantes sin convertirlos primero a cadenas.
# Esto da error:
", ".join([1, 2, 3])  # TypeError

# Debe ser:
", ".join(str(num) for num in [1, 2, 3])  # "1, 2, 3"

# 1. Usando [::-1] (rebanado inverso)
mi_lista = [1, 2, 3, 4, 5]
print(mi_lista[::-1])

# 2. Usando el método reverse() (modifica la lista original)
mi_lista = [1, 2, 3, 4, 5]
mi_lista.reverse()
print(mi_lista)

# 3. Usando la función reversed() (no modifica la lista original)
mi_lista = [1, 2, 3, 4, 5]
print(list(reversed(mi_lista)))

