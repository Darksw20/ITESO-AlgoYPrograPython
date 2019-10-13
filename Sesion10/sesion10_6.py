num1 = float(input("Ingrese el numero 1: "))
num2 = float(input("Ingrese el numero 2: "))

if num1 == num2:
    print("Ambos numeros n son iguales")
elif num1 > num2:
    numMayor = num1
else:
    numMayor = num2
print("El numero mayor es",numMayor)