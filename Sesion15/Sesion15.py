'''
for i in range(100):
    print(f"{i+1} Hola Mundo")

 
for i in range(0,51,5):
    print(i)


a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
acm = 0
for i in range(a,b+1):
    print(f"iterador: {i} acumulador: {acm}")
    acm = i+acm
print("resultado: ",acm)


for x in range(1,6):
    for y in range(1,11):
        print(f"{x}x{y}={x*y}")
'''
print("         Tabla de Multiplicar")
print("   ",end="|")
for i in range(1,11):
    print(f" {i}",end=" ")
print("")
print("-----------------------------------")
for x in range(1,11):
    print(f" {x} | ",end="")
    for y in range(1,11):
        print(f"{x*y} ",end=" ")
    print("")
