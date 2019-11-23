with open('Tarea_Archivos/algoritmos.iteso.txt', 'w+') as a:
    a.write(">secuencia 1\nACTG\n")

with open('Tarea_Archivos/algoritmos.iteso.txt', 'a+') as a:
    a.write(">secuencia 2\nGATA\n")

with open('Tarea_Archivos/serie.num.txt', 'w+') as a:
    for i in range(1,101):
        a.write(str(i)+"\n")    

with open('Tarea_Archivos/serie.num.txt', 'r') as a:
    cont = a.read()
    with open('Tarea_Archivos/archivoCopiado.txt', 'w+') as b:
        b.write(cont)

with open('Tarea_Archivos/SesionArchivos_ejemplo.txt', 'r',encoding="UTF-8") as a:
    lines = []
    data = []
    for i in range(1,5):
        line = a.readlines(i)
        data = line[0].split(";")
        lines.append(data)
    print("ID\tNOMBRE\tAPELLIDO\tFECHA DE NACIMIENTO")
    for i in range(0,4):
        print(f"{str(lines[i][0])}\t{str(lines[i][1])}\t{str(lines[i][2])}\t\t{str(lines[i][3])}")