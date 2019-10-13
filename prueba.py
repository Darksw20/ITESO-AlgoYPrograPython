'''
opcion = 0 
while opcion != 5:
    opcion = int(input("******MENU******\n1.Leer\n2.Escribir\n3.Escuchar\n4.Hablar\n5.Salir\n"))
    if opcion == 1:
        print("Leer")
    elif opcion == 2:
        print("Escribir")
    elif opcion == 3:
        print("Escuchar")
    elif opcion == 4:
        print("Hablar")
print("Vamos a salir del programa")
'''
passw = "algoritmos123"
passu = input("Ingrese la contraseña")
while passw != passu:
    passu = input("Contraseña incorrecta, ingresala nuevamente:")    
print("Bienvenido al sistema")
