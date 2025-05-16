lista = []

for i in range(1,6):
    lista.append(str(i**3))
    p = " ".join(lista)
    print(f"{p}\n", end = "")
