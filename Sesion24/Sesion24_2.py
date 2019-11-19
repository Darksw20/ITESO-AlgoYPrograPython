def convertirASegundos(horas,minu,seg):
    return str((horas*3600)+(minu*60)+seg)
def convertirAHoras(seg):
    segundos = seg % 60
    minutos = (seg %3660)
    hrs = seg // 3600
    return [hrs,minutos,segundos]

#hrs = int(input("Ingresa la hora: "))
#minu = int(input("Ingresa los minutos: "))
seg = int(input("Ingresa los segundos: "))
lista = convertirAHoras(seg)
print(f"horas: {lista[0]} minutos: {lista[1]} segundos: {lista[2]}")
#print(convertirAHoras(hrs,minu,seg),"Segundos")

