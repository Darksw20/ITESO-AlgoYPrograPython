#1
alumnos = {}
for i in range(3):
    clave = input(f"Ingresa el nombre del alumno {i+1}: ")
    calif = []
    for x in range(3):
        calif.append(input(f"Ingresa la calificacion {x+1}: "))
    alumnos[clave] = calif
print(alumnos)
#2
claveF = input("Ingrese el alumno a buscar: ")
if claveF in alumnos:
    print("simon, si existe")
#3
for nombre in alumnos:
    print("El alumno "+nombre+ " tiene las siguientes calificaciones: " + ', '.join(alumnos[nombre]))
