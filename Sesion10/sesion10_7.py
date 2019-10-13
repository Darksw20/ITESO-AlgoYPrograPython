num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))
num3 = int(input("Ingrese el numero 3: "))
num4 = int(input("Ingrese el numero 4: "))
num5 = int(input("Ingrese el numero 5: "))
numMax = num1
if num1 >= numMax:
    numMax = num1
elif num2 >= numMax:
    numMax = num2
elif num3 >= numMax:
    numMax = num3
elif num4 >= numMax:
    numMax = num4
elif num5 >= numMax:
    numMax = num5
print("El numero maximo es:",numMax)