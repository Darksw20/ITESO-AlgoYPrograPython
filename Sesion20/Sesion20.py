lista_numeros = []
for i in range(4):
    numero = int(input("Numero: "))
    lista_numeros.append(numero)
prom = float(sum(lista_numeros)/len(lista_numeros)) 
print("Promedio",prom)
for i in lista_numeros:
    if i <= prom:
        print(i," ",end="")
        