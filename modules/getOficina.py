# import storage.oficina as of
from tabulate import tabulate

import requests
import json
import modules.postOficina as postOfi
import re



def FuncionDeConeccionOficinaJson():
      peticion=requests.get("http://10.0.2.15:5002/oficinas") 
      Informacion=peticion.json()  
      return Informacion        





#obtener un codigo de la lista directo(optimizado)
def getAllcode(codigo):
       peticion=requests.get(f"http://10.0.2.15:5002/oficinas/{codigo}")
       return[peticion.json()] if peticion.ok else []






# Obtener oficinca segun se escriba
def getTelFromTel(telefono):
     Officecode=[]
     for val in FuncionDeConeccionOficinaJson():
        if val.get("telefono")==telefono:
            return[val]




#obtener oficinca segun la que se meta por consola
def getCodeOfficeCode(codigo):
     Officecode=[]
     for val in FuncionDeConeccionOficinaJson():
        if val.get("codigo_oficina")==codigo:
            return[val]

#obtener direcciones a partir de direcciones
def getDireccion1FromDireccion(direccion):
     linea1=[]
     for val in FuncionDeConeccionOficinaJson():
        if val.get("linea_direccion1")==direccion:
            return[val]
        
def getDireccion2FromDireccion(direccion):
     line2=[]
     for val in FuncionDeConeccionOficinaJson():
        if val.get("linea_direccion2")==direccion:
            return[val]


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
            
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=5:
                        
                    if(opcion==1):
                        print(tabulate(getAllOffice(), headers="keys",tablefmt="grid"))

                    elif(opcion==2):
                        print(tabulate(getAllCityPhoneSpain(), headers="keys",tablefmt="grid"))

                    elif(opcion==3):
                        print(tabulate(getAllCodeOfficeCity7(), headers="keys",tablefmt="grid"))

                    elif(opcion==4):
                        print(tabulate(getAllCityPhones(), headers="keys",tablefmt="grid"))
                    
                    elif(opcion==5):
                        postOfi.menu()

                    elif(opcion==0):
                        break