palindromo = input("Inserte el palindromo: ")
comp = ""
for x in range(len(palindromo),0,-1):
    comp += palindromo[x-1]
if palindromo == comp:
    print("Si es un palindromo")
else:
    print("No es un palindromo")