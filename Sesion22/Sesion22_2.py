#Programa 5
numP = int(input("Ingresa el numero de palabras: "))
lista = []
while numP > 0:
    lista.append(input("Ingresa una palabra: "))
    numP -= 1
print("[",end="")
for i in lista:
    print(i,end=" ")
print("]")

#programa 6
palabra = input("Ingresa la palabra a comparar: ")
print(lista.count(palabra),"ocurrencias encontradas")

