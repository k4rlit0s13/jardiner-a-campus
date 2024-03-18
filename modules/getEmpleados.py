# import storage.empleado as em
from tabulate import tabulate

import requests
import json
import modules.postEmpleados as postEm
import re



def FuncionDeConeccionEmpleadoJson():
      peticion=requests.get("http://10.0.2.15:5003") 
      Informacion=peticion.json()  
      return Informacion        





#obtener un codigo de la lista directo(optimizado)
def deleteProducto(codigo):
       peticion=requests.get(f"http://10.0.2.15:5003/empleados/{codigo}")
       return(peticion.json()) if peticion.ok else []






#obtener codigo cliente a partir de codigo
def getEmpleadoFormempleados(codigo):
    clientecode=[]
    for val in FuncionDeConeccionEmpleadoJson():
        if (val.get("codigo_empleado")==codigo):
            return[val]



def getEmailFromEmail(email):
    empleadoemail=[]
    for val in FuncionDeConeccionEmpleadoJson():
        if (val.get("email")==email):
            return[val]
        

#filtro para obtener todos los nombres de los empleados
def getAllNames():
    NamesNames2EmailJefe=[]
    for val in FuncionDeConeccionEmpleadoJson():
        NamesNames2EmailJefe.append(
                {
                    "nombre": val.get ("nombre"),
                    "apellidos":(f'{val.get("apellido1")} {val.get("apellido2")}'), #hay que meter 2 datos en uno solo, usamo comentario con activador de funcion f
                    "email": val.get("email"),
                    "jefe": val.get("codigo_jefe")
                }
            )
    return NamesNames2EmailJefe



#algoritmo para devolver un listado con el nombre y email de los empleados cuyo jefe tiene un código de jefe igual a 7
def getAllNamesNames2EmailJefe7 (codigo):
    getAllNamesNames2EmailJefe=[]
    for val in FuncionDeConeccionEmpleadoJson():
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
    for val in FuncionDeConeccionEmpleadoJson():
            if val.get("codigo_empleado")==1:
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
def getAllNamesSurnamesJob():
    NamesSurnamesJob=[]
    for val in FuncionDeConeccionEmpleadoJson():
        if(val.get("puesto")!= "Representante Ventas"):
            NamesSurnamesJob.append(
            {"Nombre":val.get("nombre"),
             "Apellidos":(f'{val.get("apellido1")}{val.get("apellido2")}'),
             "Cargo":val.get("puesto")
             }
          )
    return NamesSurnamesJob


def menu():
    while True:
        print("""
              
███████╗███╗   ███╗██████╗ ██╗     ███████╗ █████╗ ██████╗  ██████╗ ███████╗
██╔════╝████╗ ████║██╔══██╗██║     ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔════╝
█████╗  ██╔████╔██║██████╔╝██║     █████╗  ███████║██║  ██║██║   ██║███████╗
██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  ██╔══██║██║  ██║██║   ██║╚════██║
███████╗██║ ╚═╝ ██║██║     ███████╗███████╗██║  ██║██████╔╝╚██████╔╝███████║
╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝
                                                                            
        1. Obtener todos los empleados
        2. Obtener listado con el nombre y email de los empleados cuyo jefe tiene un código de jefe igual a 7
        3. Obtener el nombre, apellidos y puesto de aquellos empleados que no sean respresentantes de ventas
        4. Obtener el nombre del puesto, nombre, apellidos e email del feje de la empresa

        EDITAR DATOS:      
        5. Modificar datos de empleado
        
              
        0. Salir al menu principal
""")
    
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=5:  

                    if(opcion==1):
                        print(tabulate(getAllNames(), headers="keys",tablefmt="grid"))

                    if(opcion==2):
                        codigo=int(input("Ingresa del numero del jefe: "))
                        print(tabulate(getAllNamesNames2EmailJefe7(codigo), headers="keys",tablefmt="grid"))
                    
                    if(opcion==3):
                        print(tabulate(getAllNamesSurnamesJob(), headers="keys",tablefmt="grid"))

                    if(opcion==4):
                        print(tabulate(getAllNameSurnamesJefeemail(), headers="keys",tablefmt="grid"))

                    if(opcion==5):
                        postEm.menu()

                    if(opcion==0):
                        break
                
