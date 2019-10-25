import random
i = int(input("¿Desea tirar el dado? 1=Si 0=No\n"))
while i == 1:
    print(f"El valor del dado es: {random.randint(1,6)}")
    i = int(input("¿Desea tirar el dado otra vez? 1=Si 0=No\n"))
print("Gracias por usar el programa")