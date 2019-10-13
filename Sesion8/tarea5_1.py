option = int(input("Menu del programa:\n1.-Verificar que numeros son positivos\n2.-Mostrar la suma de numeros positivos\n3.-Descuento en colegiaturas\n4.-Determina si una persona es apta para el servicio militar\n"))

if option == 1:
    num1 = float("Ingresa numero 1: ")
    num2 = float("Ingresa numero 2: ")
    if num1 >= 0 and num2 >= 0:
        print("Ambos numeros son positivos")
    elif num1 >= 0 and num2 < 0:
        print("El primer numero es positivo y el segundo es negativo")
    elif num1 < 0 and num2 >= 0:
        print("El primer numero es negativo y el segundo es positivo") 
    else:
        print("Ambos numeros son negativos")
elif option == 2:
    contador = 0.0
    num1 = float("Ingresa numero 1: ")
    num2 = float("Ingresa numero 2: ")
    num3 = float("Ingresa numero 3: ")
    if num1 >= 0.0:
        contador + num1
    if num2 >= 0.0:
        contador + num2
    if num3 >= 0.0:
        contador + num3
    print("El total es de",contador)
elif option == 3:
    nombre = input("Ingrese nombre del alumno: ")
    colegiatura = float(input("Ingrese colegiatura: "))
    egresado = input("¿Es egresado? 1=Si 0=No")
    print("Nombre:",nombre)
    print("Colegiatura:",colegiatura)
    if egresado == 1:
        print("Total a Pagar:",colegiatura-(colegiatura*.15))
elif option == 4:
    edad = int(input("Ingrese la edad: "))
    genero = int(input("Ingrese el genero F=0  M=1 "))
    if genero == 1 and edad > 18 and edad < 25:
        print("Es apto para el servicio militar")
    else:
        print("No es apto para el servicio militar")
else:
    print("Opcion invalida")