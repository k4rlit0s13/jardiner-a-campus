import storage.oficina as of

#filtro que devuelva un listado con el código de oficina y la ciudad donde hay oficinas
def getAllCodeOfficeCity7():
    AllCodeOfficeCity7=[]
    for val in of.oficina:
        if (val.get("pais"))=="España":
            AllCodeOfficeCity7.append(
            {
                "codigo_oficina":val.get("codigo_oficina"),
                "ciudad":val.get("ciudad")
        })
    return AllCodeOfficeCity7