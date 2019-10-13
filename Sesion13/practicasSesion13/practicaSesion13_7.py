'''
num = int(input("Ingrese una cantidad de numeros\n"))
contador = int(input("Ingrese un numero\n"))
compnum = contador
while num > 0:
    if contador >= compnum:
        print("Es el mayor")
        compnum = contador
    contador = int(input("Ingrese un numero\n"))
    num -= 1
    '''

num = int(input("Ingrese factorial"))
acumulador = 1
while num > 0:
    acumulador = num * acumulador
    num -= 1
print("Factorial=",acumulador)
