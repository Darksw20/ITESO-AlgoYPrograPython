nombre = input("Favor de ingresar su nombre\n")
apP = input("Favor de ingresar su Apellido Paterno\n")
apM = input("Favor de ingresar su Apellido Materno\n")
fechaN = input("Favor de ingresar su Fecha de Nacimiento usando el formato dd/mm/aaaa\n")
ano = fechaN[0:2]
mes = fechaN[3:5]
dia = fechaN[8:]
print(f"RFC del ITESO: {apP[:2].upper()}{apM[:1].upper()}{nombre[:1].upper()}{ano}{mes}{dia} ")