option = int(input("Menu del programa:\n1.-Tipo de cambio MXN -> USD y USD -> MXN\n2.-Calcular el valor de Descuento en el supermercado\n3.-Convertir peso\n4.-Calcular calificación final\n"))

if option == 1:
    opcion = int(input("1.-MXN -> USD\n2.-USD -> MXN\n"))
    if opcion == 1:
        mxn = float(input("Ingrese cantidad de pesos a convertir: "))
        print("Son",mxn*0.051,"USD")
    elif opcion == 2:
        usd = float(input("Ingrese cantidad de dolares a convertir: "))
        print("Son",usd*19.44,"MXN")
    else:
        print("Opcion invalida")
elif option == 2:
    total = float(input("Ingresa el total del gasto en el supermercado: "))
    print("El total de de ahorro es de",total*0.15,"MXN")
elif option == 3:
    peso = float(input("Ingresa el peso en Kg: "))
    print("El peso en gramos es de",peso*1000)
    print("El peso en kilos es de",peso,"Kg")
    print("El peso en toneladas es de",peso*0.001,"T")    
elif option == 4:
    print("Ingrese las calificaciones del parcial")
    ex1 = float(input("Examen parcial 1: "))
    ex2 = float(input("Examen parcial 2: "))
    ex3 = float(input("Examen parcial 3: "))
    ex = float(input("Examen final: "))
    tf = float(input("Trabajo final: "))
    print("La calificacion fin es de", ((ex1*.15)+(ex2*.15)+(ex3*.15)+(ex*.30)+(tf*.25)))
else:
    print("Opcion invalida")