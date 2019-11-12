def mostrarLista(lista):
    print("[",end="")
    for i in lista:
        print(i,end=" ")
    print("]")

#programa 10
numP = int(input("Ingresa el numero de palabras: "))
lista = []
while numP > 0:
    lista.append(input("Ingresa una palabra: "))
    numP -= 1
mostrarLista(lista)
lista2 = lista
lista2.reverse()
mostrarLista(lista2)