'''
letra = input("Ingrese solamente vocales\n")
while letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    letra = input("Ingrese solamente vocales\n")


opc = int(input("******MENU******\n1.Leer\n2.Escribir\n3.Escuchar\n4.Hablar\n5.Salir\n"))
while opc != 5:
    if opc == 1:
        print("Leer\n")
    elif opc == 2:
        print("Escribir\n")
    elif opc == 3:
        print("Escuchar\n")
    elif opc == 4:
        print("Hablar\n")
    else:
        print("Numero invalido")
    opc = int(input("******MENU******\n1.Leer\n2.Escribir\n3.Escuchar\n4.Hablar\n5.Salir\n"))
print("Salio\n")

contador = 0
passw  = input("Ingresa tu contraseña\n")
while passw != "algoritmos123" and contador < 2:
    passw = input("Contraseña incorrecta, intento, ingresala nuevamente:\n")
    contador += 1
if contador == 2:
    print("Se agotaron los intentos")
else:
    print("Bienvenido al sistema\n")
'''
