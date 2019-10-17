username = input("Ingrese el nombre de usuario a validar: ")
bandera = 0
if len(username) < 6:
    print("El nombre de usuario debe contener al menos 6 caracteres")
    bandera += 1
if len(username) > 12:
    print("El nombre de usuario no puede contener mas de 12 caracteres")
    bandera += 1
if not username.isalpha():
    print("El nombre de usuario puede contener solo letras y numeros")
    bandera += 1
if bandera == 0:
    print("El usuario cumple con los criterios de aceptacion")