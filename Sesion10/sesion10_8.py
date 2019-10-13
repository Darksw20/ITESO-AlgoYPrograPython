exa = float(input("Ingrese la calificacion del examen: "))

if exa < 10.5:
    print("Te pasas")
elif exa < 15.0:
    print("Aprobado")
elif exa < 17.0:
    print("Notable")
elif exa < 20.0:
    print("Sobresaliente")
elif exa >= 20.0:
    print("Matricula de Honor")