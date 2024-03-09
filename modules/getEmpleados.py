import storage.empleado as em

#algoritmo para devolver un listado con el nombre y email de los empleados cuyo jefe tiene un código de jefe igual a 7
def getAllNamesNames2EmailJefe (codigo):
    getAllNamesNames2EmailJefe=[]
    for val in em.empleados:
        if(val.get("codigo_jefe")==codigo):
            getAllNamesNames2EmailJefe.append(
                {
                    "nombre": val.get ("nombre"),
                    "apellidos":(f'{val.get("apellido1")} {val.get("apellido2")}'), #hay que meter 2 datos en uno solo, usamo comentario con activador de funcion f
                    "email": val.get("email"),
                    "jefe": val.get("codigo_jefe")
                }
            )
    return getAllNamesNames2EmailJefe

#filtro para devolver el nombre del puesto, nombre, apellidos e email del feje de la empresa
def getAllNameSurnamesJefeemail():
    NameSurnamesJefeemail=[]
    for val in em.empleados:
            NameSurnamesJefeemail.append(
                {
                    "Nombre": val.get ("nombre"),
                    "Apellidos":(f"{val.get('apellido1')} {val.get('apellido2')}"), #hay que meter 2 datos en uno solo, usamo comentario con activador de funcion f
                    "codigo del Jefe": val.get("codigo_jefe"),
                    "Email jefe":val.get("email")
                }
            )
    return NameSurnamesJefeemail

#filtro para devolver un listado con el nombre, apellidos y puesto de aquellos empleados que no sean respresentantes de ventas
def getAllNamesSurnamesJob(puesto):
    NamesSurnamesJob=[]
    for val in em.empleados:
        if(val.get("puesto")!= puesto):
            NamesSurnamesJob.append(
            {"Nombre":val.get("nombre"),
             "Apellidos":(f'{val.get("apellido1")}{val.get("apellido2")}'),
             "Cargo":val.get("puesto")
             }
          )
    return NamesSurnamesJob


def menu():
    print("""
███████╗███╗   ███╗██████╗ ██╗     ███████╗ █████╗ ██████╗  ██████╗ ███████╗
██╔════╝████╗ ████║██╔══██╗██║     ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔════╝
█████╗  ██╔████╔██║██████╔╝██║     █████╗  ███████║██║  ██║██║   ██║███████╗
██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  ██╔══██║██║  ██║██║   ██║╚════██║
███████╗██║ ╚═╝ ██║██║     ███████╗███████╗██║  ██║██████╔╝╚██████╔╝███████║
╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝
                                                                            
        1.
        2.
        3.
        4.

""")