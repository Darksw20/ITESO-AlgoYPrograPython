num = int(input("Ingrese numero: "))
while num != 1:
    print(num) 
    if (num % 2) == 0:
        num /= 2
    elif(num % 2) == 1:
        num = (num * 3)+1
print(num)