#Programa 10
lista = [12,"JAJAJA","NO",131,"WUENO","Vamos a bailar","el maligno ritual","Asando un Salmon",36.15, "EL JAJAS"]
search = input("Cosa a buscar: ")
try:
    serPar = float(search)
    try:
        res=lista.index(serPar)
    except:
        res= "No esta en la lista"
except:
    try:
        res=lista.index(search)
    except:
        res= "No esta en la lista"
print(res)

#Programa 11
lista = [12,"JAJAJA","NO",131,"WUENO","Vamos a bailar","el maligno ritual","Asando un Salmon",36.15, "EL JAJAS"]
search = input("Cosa a buscar: ")
try:
    serPar = float(search)
    try:
        res="El resultado se repite: "+str(lista.count(serPar))+ " veces"
    except:
        res= "No esta en la lista."
except:
    try:
        res="El resultado se repite: "+str(lista.count(search))+ " veces"
    except:
        res= "No esta en la lista"
print(res)

#Programa 12 y 13
nombres=[]
cedula=[]
for i in range(3):
    nombres.append(input("Ingrese el nombre del estudiante: "))
    cedula.append(input("Ingrese la cedula del estudiante: "))

cedula_Search=input("Ingrese la cedula que desea buscar: ")
if cedula_Search in cedula:
    posicion=cedula.index(cedula_Search)
    print(f"Esa cedula corresponde a {nombres[posicion]}")
else: 
    print("No existe esa cedula.")