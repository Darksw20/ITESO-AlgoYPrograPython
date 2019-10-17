passw = input("Ingrese la contraseña de usuario a validar: ")
bandera = 0
may = 0
minus = 0
space = 0
if len(passw) < 8:
    print("La contraseña de usuario debe contener al menos 8 caracteres")
    bandera += 1
if passw.isalpha():
    print("Necesita un caracter no alfanumerico")
    bandera += 1
for x in passw:
    if x.isupper():
        may += 1
    if x.islower():
        minus += 1
    if x.isspace():
        space += 1
if may == 0:
    print("Le hacen falta mayusculas")
    bandera += 1
if minus == 0:
    print("Le hacen falta minusculas")
    bandera += 1
if space > 0:
    print("La contraseña no debe tener espacios")
    bandera += 1
if bandera == 0:
    print("La contraseña es SEGURA")
else:
    print("La contraseña elegida no es segura")