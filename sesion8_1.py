'''
menu = input("Que desea \n1.-Triangulo\n2.-Circulo\n")
if menu == "1":
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))
    print("El area del triangulo es:",float((base*altura)/2))
elif menu == "2":
    radio = float(input("Ingrese el radio: "))
    print("El area del circuilo es:", int((3.1416*(radio**2))))
else:
    print("Opcion invalida")

sueldo = float(input("Ingrese su sueldo: "))
if sueldo <= 0:
    print("Sueldo invalido")
else:
    if sueldo < 496.07:
        isr = 0.0 + (sueldo - 0.01)*(1.92)/100
    elif sueldo < 4210.41:
        isr = 9.52 + (sueldo - 496.08)*(6.40)/100
    elif sueldo < 7399.42:
        isr = 247.23 + (sueldo - 4210.42)*(10.88)/100
    elif sueldo < 8601.50:
        isr = 594.24 + (sueldo - 7399.43)*(16.00)/100
    elif sueldo < 10298.35:
        isr = 786.55 + (sueldo - 8601.51)*(17.92)/100
    elif sueldo < 20770.29:
        isr = 1090.62 + (sueldo - 10298.36)*(21.36)/100
    elif sueldo < 32736.85:
        isr = 3327.42 + (sueldo - 20770.30)*(23.52)/100
    else:
        isr = 6141.95 + (sueldo - 32736.84)*(30.0)/100
    print("El ISR es de",isr)


opcion = int(input("¿Que operacion desea realizar?\n[1] Suma\n[2] Resta\n[3] Multiplicacion\n[4] Division\n"))
if opcion > 4 or opcion < 1
    num1 = float(input("Escriba el primer numero: "))
    num2 = float(input("Escriba el segundo numero: "))

if opcion == 1:
    print("Bienvenido al programa para sumar")
    resultado = num1 + num2
elif opcion == 2:
    print("Bienvenido al programa para restar")
    resultado = num1 - num2
elif opcion == 3:
    print("Bienvenido al programa para multiplicar")
    resultado = num1 * num2
elif opcion == 4:
    print("Bienvenido al programa para dividir")
    resultado = num1 / num2
else:
    resultado = 0
print("Resultado: ",resultado)
'''

