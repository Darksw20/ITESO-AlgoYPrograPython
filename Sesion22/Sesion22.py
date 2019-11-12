#programa 1
lista = [1,2,3,4,5,6,7,8,9,10]

#programa 2
lista2 = []
inp = 1
while inp != 0:
    inp = int(input("Ingresa un numero: "))
    if inp != 0:
        lista2.append(inp)
lista2.sort()
print("[",end="")
for i in lista2:
    print(i,end=",")
print("]")

#Programa 3
lista2.sort(reverse=True)
print("[",end="")
for i in lista2:
    print(i,end=",")
print("]")

#programa 4
num = []
num.append(int(input("Ingresa el numero 1:")))
num.append(int(input("Ingresa el numero 2:")))
num.append(int(input("Ingresa el numero 3:")))
num.sort(reverse=True)
print(f"Numero maximo: {num[0]}")
num.sort()
print(f"Numero minimo: {num[0]}")
print("Promedio:",float((num[0]+num[1]+num[2])/3))