#Programa 1

lista=["Hola"]
for i in range(5):
    print(lista[0])

#Programa 2
numero=int(input("Ingrese un número: "))
if numero>0:
    print("El número es positivo.")
elif numero==0:
    print("El número es cero.")
else: 
    print("El número es negativo.")

#Programa 3
numeros=[]
for i in range(5):
    numeros.append(int(input("Ingrese el número: ")))
print(sum(numeros))


#Programa 4
import math
numero= int(input("Ingrese un número: "))
while numero<0:
    numero= int(input("Ingrese un número positivo: "))
print(f"La raíz cuadrada es: {math.sqrt(numero)} ")

#Programa 5
simbolo=input("Ingrese un símbolo: ")
tamaño=int(input("Ingrese el tamaño: "))
linea=[]
for i in range(tamaño):
    linea.append(simbolo)
for i in range(tamaño):
    for i in range(tamaño):
        print(linea[i], end=" ")
    print("\n")

