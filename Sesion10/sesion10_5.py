cantidadC = float(input("Ingrese el capital: "))
interes = float(input("Ingrese el porcentaje de interes: "))
years = int(input("Ingrese el numero de años: "))

if interes >= 0.0:
    capFinal = cantidadC*(interes/100)*years
    print("El capital final es de",capFinal)
else:
    print("El interes es negativo")