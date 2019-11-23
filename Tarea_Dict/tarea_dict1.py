import random
futbolistas = {}
claves = []
valores = []
for i in range(3):
    nombre = input("Ingresa el nombre del futbolista: ")
    numC = int(input("Ingresa el numero de camisa: "))
    futbolistas[numC] = nombre

for x, y in futbolistas.items():
    print(f"Nombre {str(y)} y camisa {str(x)}")
    valores.append(y)
    claves.append(x)

print(f"El número de elementos del diccionario son: {len(futbolistas)}")
print(f"Claves {str(claves)}")
print(f"Valores {str(valores)}")

print(futbolistas[random.choice(claves)])
 
newVal = input("Nuevo nombre: ")
newClav = int(input("Nueva camisa: "))
if newClav in futbolistas:
    print("Ya existe, ni modo")
else:
    futbolistas[newClav] = newVal

newVal2 = input("Nuevo nombre: ")
newClav2 = int(input("Nueva camisa: ")) 
futbolistas[newClav2] = newVal2

delClav = int(input("Numero de jugador a eliminar: "))
futbolistas.pop(delClav)
futbolistas2 = futbolistas.copy()
print(futbolistas2)
futbolistas2.clear()
for i in range(len(claves)):
    futbolistas2[claves[i]] = valores[i]
print(futbolistas2)

revClave = int(input("Ingresa un numero de camisa a ver si existe: "))
if revClave in futbolistas2:
    print("Si existe!")
else:
    print("Nel, no existe")
for x, y in futbolistas2.items():
    print(f"({str(x)},{str(y)})")

suplentes = {22:"Lionel Messi",23:"El bofo",24:"Oswaldo Sanchez",25:"Ochoa",26:"El chicharito"}

equipo = {
    "regulares": futbolistas,
    "suplentes": suplentes
}
print(equipo)