def mostrarLista(lista):
    print("[",end="")
    for i in lista:
        print(i,end=" ")
    print("]")
#Programa 14
'''

numP = int(input("Ingresa el numero de palabras: "))
lista = []
while numP > 0:
    lista.append(input("Ingresa una palabra: "))
    numP -= 1
lista = set(lista)
mostrarLista(lista)
'''
#Programa 15
numP = int(input("Ingresa el numero de palabras: "))
lista = []
noInc1 = []
noInc2 = []
inc = []
while numP > 0:
    lista.append(input("Ingresa una palabra: "))
    numP -= 1
lista = list(set(lista))
numP2 = int(input("Ingresa el numero de palabras: "))
lista2 = []
while numP2 > 0:
    lista2.append(input("Ingresa una palabra: "))
    numP2 -= 1
lista2 = list(set(lista2))
for i in range(0,len(lista)):
    if lista[i] not in lista2:
        noInc1.append(lista[i])
for i in range(0,len(lista2)):
    if lista2[i] not in lista:
        noInc2.append(lista2[i])
for i in range(0,len(lista)):
    if lista[i] in lista2:
        inc.append(lista[i])
mostrarLista(noInc1)
mostrarLista(noInc2)
mostrarLista(inc)