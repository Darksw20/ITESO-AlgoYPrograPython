''' TAREA 3 - Area de un triangulo
altura = int(input("Por favor ingrese la altura del triangulo: "))
base = int(input("Por favor ingrese la base del triangulo: "))
print("El area del triangulo es de",(base*altura)/2)

TAREA 3 - Ultimos dos digitos de un numero del 100 al 1000
num = int(input("Por favor ingrese el numero a evaluar: "))
print("Los ultimos digitos del numero son", num % 100)

Practica 1
productName1 = input("Ingresar nombre del Producto 1: ")
productPrice1 = input("Ingresar precio del "+productName1)
productName2 = input("Ingresar nombre del Producto 2: ")
productPrice2 = input("Ingresar precio del "+productName2)

subTotal = float(productPrice1) + float(productPrice2)
print("Subtotal:",subTotal)
iva = float(subTotal*0.16)
print("IVA:",iva)
print("Total:",subTotal + iva)

Practica 2


gasActual = float(input("Cuantos litros de gasolina te quedan?: "))
gasNecesario = float(input("Cuantos litros necesitas para llegar?: "))
if gasNecesario > gasActual:
    gasAPoner = (gasActual-gasNecesario)*-1
    print("Litros que faltan poner", gasAPoner)
else:
    print("Si llegas carnal")

'''

num = float(input("Ingrese un numero real: "))
if num < 0.0 or num > 10.0:
    print("NO VALIDO")
else:
    if num < 5.9:
        print ("CINCO")
    elif num < 6.49:
        print("SEIS")
    elif num < 7.49:
        print("SIETE")
    elif num < 8.49:
        print("OCHO")
    elif num < 9.49:
        print("NUEVE")
    elif num <= 10.0:
        print("DIEZ")