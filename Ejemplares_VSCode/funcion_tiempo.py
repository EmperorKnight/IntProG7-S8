from datetime import datetime
# from datetime import timedelta
# from datetime import date
# import time

# # Obtener la fecha actual.
# # Date.today muestra la fecha actual 
# dia = date.today()

# # Datetime.now muestra la fecha actual, la hora, los minutos, los segundos y los microsegundos exactos
# hoy = datetime.now()

# print(dia)
# print(hoy)

# # Atributos
# # Date
# print("El dia actualmente es {}".format(dia.day))
# print("El mes actualmente es {}".format(dia.month))
# print("El año actualmente es {}".format(dia.year))

# # Datetime
# print("El dia actualmente es {}".format(hoy.day))
# print("El mes actualmente es {}".format(hoy.month))
# print("El año actualmente es {}".format(hoy.year))
# print("La hora actualmente es {}".format(hoy.hour))
# print("Los minutos actualmente son {}".format(hoy.minute))
# print("Los segundos actualmente son {}".format(hoy.second))
# print("Los microsegundos actualmente son {}".format(hoy.microsecond))

# # Operaciones
# hoy = datetime.now()
# fecha_futura = hoy + timedelta(days = 2)
# print(fecha_futura)

# # Formato de fechas
# hoy = datetime.now()
# ejemplo = hoy.strftime("Dia: %d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S")
# print(ejemplo)
# # %d Día
# # %m Mes
# # %Y Año
# # %H Hora
# # %M Minutos
# # %S segundos

# def ejemplo (date):
#     meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
#     dia = date.day
#     mes_actual= meses[date.month - 1]
#     año = date.year
#     hora = date.hour
#     minutos = date.minute
#     segundos = date.second
#     mensaje = f"{dia} de {mes_actual} del {año}. \nSon las {hora}:{minutos}:{segundos}"
#     return mensaje

# fecha = datetime.now()
# print(ejemplo(fecha))

# Reloj que se actualiza
# while True:
#     tiempo = time.strftime("%H:%M:%S")
#     print(f"\rHora actual: {tiempo}", end = "")

# nacimiento = input(f"Introduzca su fecha de nacimiento en formato dd/mm/aaaa \n-> ")
# nacimiento1 = datetime.strptime(nacimiento,"%d/%m/%Y")

# dias_vividos = (fecha - nacimiento1).days
# dias_vividos = dias_vividos//365

# print(dias_vividos)

