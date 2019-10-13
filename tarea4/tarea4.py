calif = float(input("¿Cual es tu calificacio final [0-10]?"))

if calif > 10 and calif < 0:
    print("Calificacion no valida. Se pondra 5.")
    calif = 5.0
if calif >= 6:
    print("Aprobaste el curso.")
else:
    print("Reprobaste el curso.")