nombre = input("Ingrese el nombre:\n")
apellido = input("Ingrese el apellido:\n")
fullname = ""
nombre = nombre.capitalize()
apellido = apellido.capitalize()
print(nombre)
print(apellido)
for n in range(0,len(nombre)):
    if nombre[n].isspace():
        fullname += nombre[n+1].capitalize()
    elif nombre[n].isupper():
        fullname += nombre[n].lower()
    else:
        fullname += nombre[n]
fullname += " "
for a in range(0,len(apellido)):
    if apellido[a].isspace():
        fullname += apellido[a+1].capitalize()
    elif apellido[a].isupper():
        fullname += apellido[a].lower()
    else:
        fullname += apellido[a]

print(f"El nombre es: {fullname}")