import storage.empleado as em

def getAllNamesNames2EmailJefe (codigo):
    getAllNamesNames2EmailJefe=[]
    for val in em.empleados:
        if(val.get("codigo_jefe")==codigo):
            getAllNamesNames2EmailJefe.append(
                {
                    "nombre": val.get ("nombre"),
                    "apellidos": val.get(f'{val.get("apellido1")} {val.get("apellido2")}'), #hay que meter 2 datos en uno solo, usamo comentario con activador de funcion f
                    "email": val.get("email"),
                    "jefe": val.get("codigo_jefe")
                }
            )
    return getAllNamesNames2EmailJefe