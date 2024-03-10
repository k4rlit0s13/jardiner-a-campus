import storage.oficina as of
from tabulate import tabulate




#filtro que obtenga todas las oficinas
def getAllOffice():
    Office=[]
    for val in of.oficina:
            Office.append(
            {
                "codigo_oficina":val.get("codigo_oficina"),
                "ciudad":val.get("ciudad")
        })
    return Office



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

#filtro que devuelva un listado con la ciudad y el telefono de las oficinas de españa
def getAllCityPhone():
    AllCityPhone=[]
    for val in of.oficina:
        if (val.get("pais"))=="España":
            AllCityPhone.append(
            {
                "ciudad":val.get("ciudad"),
                "telefono":val.get("telefono")
        })
    return AllCityPhone


def menu():
        print("""

 ██████╗ ███████╗██╗ ██████╗██╗███╗   ██╗ █████╗ ███████╗
██╔═══██╗██╔════╝██║██╔════╝██║████╗  ██║██╔══██╗██╔════╝
██║   ██║█████╗  ██║██║     ██║██╔██╗ ██║███████║███████╗
██║   ██║██╔══╝  ██║██║     ██║██║╚██╗██║██╔══██║╚════██║
╚██████╔╝██║     ██║╚██████╗██║██║ ╚████║██║  ██║███████║
 ╚═════╝ ╚═╝     ╚═╝ ╚═════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
 
       1.Obtener todas las oficinas 
       2.
       3.
       4.
""")
        opcion=int(input("\nSeleccione una de las opciones: "))
        if(opcion==1):
            print(tabulate(getAllOffice(), headers="keys",tablefmt="grid"))