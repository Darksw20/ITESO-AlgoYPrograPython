num1 = int(input("Escriba numero 1: "))
num2 = int(input("Escriba numero 2: "))
num3 = int(input("Escriba numero 3: "))

if num1 > num2:
    if num1 > num3:
        print("El numero mas grande es",num1)
    else:
        print("El numero mas grande es",num3)
else:
    if num2 > num3:
        print("El numero mas grande es",num2)
    else:
        print("El numero mas grande es",num3)