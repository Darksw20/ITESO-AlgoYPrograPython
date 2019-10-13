num = int(input("Ingrese el numero: "))
i = 1
num1 = 1
aux = 1
nexnum = 0
while i <= num:
    if i == 1:
        print("1")
    elif i == 2:
        print("1")
    else:
        nexnum = num1 + aux
        num1 = aux
        aux = nexnum
        print(nexnum)
    i += 1
