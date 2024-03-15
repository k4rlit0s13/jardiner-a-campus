# import storage.oficina as of
from tabulate import tabulate

import requests
import json
import modules.postOficina as postOfi




def FuncionDeConeccionOficinaJson():
      peticion=requests.get("http://10.0.2.15:5002") 
      Informacion=peticion.json()  
      return Informacion        

































#filtro que obtenga todas las oficinas
def getAllOffice():
    Office=[]
    for val in FuncionDeConeccionOficinaJson():
            Office.append(
            {
                "codigo_oficina":val.get("codigo_oficina"),
                "ciudad":val.get("ciudad")
        })
    return Office



#filtro que devuelva un listado con el código de oficina y la ciudad donde hay oficinas
def getAllCodeOfficeCity7():
    AllCodeOfficeCity7=[]
    for val in FuncionDeConeccionOficinaJson():
        AllCodeOfficeCity7.append(
            {
                "codigo_oficina":val.get("codigo_oficina"),
                "ciudad":val.get("ciudad")
        })
    return AllCodeOfficeCity7

#filtro que devuelva un listado con la ciudad y el telefono de las oficinas de españa
def getAllCityPhoneSpain():
    AllCityPhone=[]
    for val in FuncionDeConeccionOficinaJson():
        if (val.get("pais"))=="España":
            AllCityPhone.append(
            {
                "ciudad":val.get("ciudad"),
                "telefono":val.get("telefono")
        })
    return AllCityPhone

# obtener los telefonos de las oficinas
def getAllCityPhones():
    AllCityPhone=[]
    for val in FuncionDeConeccionOficinaJson():
        AllCityPhone.append(
             {
        "codigo_oficina":val.get("codigo_oficina"),
        "ciudad":val.get("ciudad"),
        "telefono":val.get("telefono")
        })
    return AllCityPhone







def menu():
        while True:
            print("""

 ██████╗ ███████╗██╗ ██████╗██╗███╗   ██╗ █████╗ ███████╗
██╔═══██╗██╔════╝██║██╔════╝██║████╗  ██║██╔══██╗██╔════╝
██║   ██║█████╗  ██║██║     ██║██╔██╗ ██║███████║███████╗
██║   ██║██╔══╝  ██║██║     ██║██║╚██╗██║██╔══██║╚════██║
╚██████╔╝██║     ██║╚██████╗██║██║ ╚████║██║  ██║███████║
 ╚═════╝ ╚═╝     ╚═╝ ╚═════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
 
       1. Obtener todas las oficinas 
       2. Obtener la ciudad y el telefono de las oficinas de españa
       3. Obtener el código de oficina y la ciudad donde hay oficinas
       4. Obtener los telefonos de las oficinas

       EDITAR DATOS:      
       5. Modificar datos de oficinas

       0. Salir al menu principal
""")
            opcion=int(input("\nSeleccione una de las opciones: "))

            if(opcion==1):
                print(tabulate(getAllOffice(), headers="keys",tablefmt="grid"))

            if(opcion==2):
                print(tabulate(getAllCityPhoneSpain(), headers="keys",tablefmt="grid"))

            if(opcion==3):
                print(tabulate(getAllCodeOfficeCity7(), headers="keys",tablefmt="grid"))

            if(opcion==4):
                print(tabulate(getAllCityPhones(), headers="keys",tablefmt="grid"))
            
            if(opcion==5):
                postOfi.menu()

            if(opcion==0):
                break