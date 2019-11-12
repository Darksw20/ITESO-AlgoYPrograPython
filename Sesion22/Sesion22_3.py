def mostrarLista(lista):
    print("[",end="")
    for i in lista:
        print(i,end=" ")
    print("]")

#programa 8
numP = int(input("Ingresa el numero de palabras: "))
lista = []
while numP > 0:
    lista.append(input("Ingresa una palabra: "))
    numP -= 1
mostrarLista(lista)
palabra = input("Ingresa la palabra a eliminar: ")
lista.pop(lista.index(palabra))
mostrarLista(lista)

