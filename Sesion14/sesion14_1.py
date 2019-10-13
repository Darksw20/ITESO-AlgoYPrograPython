'''
numCalif = int(input("Ingrese la cantidad de calificaciones"))
i=numCalif
acumulador = 0
while i > 0:
    acumulador += float(input("Calificacion :"))
    i -= 1
print("Promedio = ",acumulador/numCalif)
'''
a = int(input("Ingrese el primer numero del rango:"))
b = int(input("Ingrese el segunto numero del rango"))
acum = 0
while a != b+1:
    acum += a
    a+=1
print("La sumatoria es de:",acum)

numEstaturas = int(input("Ingrese la cantidad de estaturas"))
i=numEstaturas
acumulador = 0
while i > 0:
    acumulador += float(input("Estaturas :"))
    i -= 1
print("Promedio = ",acumulador/numEstaturas)
