# import storage.cliente as cli
# import storage.empleado as emple
from tabulate import tabulate

import re
import requests
import json
import modules.postClients as postcli








#json-server storage/cliente.json -b 5001
def FuncionDeConeccionClienteJson():
      peticion=requests.get("http://10.0.2.15:5001") 
      Informacion=peticion.json()  
      return Informacion        

def FuncionDeConeccionEmpleadoJson():
      peticion=requests.get("http://10.0.2.15:5003") 
      Informacion=peticion.json()  
      return Informacion        









def search():
    clienteNames=[]
    for val in FuncionDeConeccionClienteJson():
        codigoName=({
        "codigo_cliente": val.get("codigo_cliente"),
        "nombre_cliente": val.get ("nombre_cliente")
     })
        clienteNames.append(val)
        return clienteNames
    




#filtro para obtener lista del codigo y nombre de cliente
def getAllCodesClients():
    clienteNames= []
    for cliente in FuncionDeConeccionClienteJson():
            clienteNames.append({
                "codigo del cliente": cliente.get("codigo_cliente"),
                "nombre del cliente": cliente.get("nombre_cliente")
            })
    return clienteNames





#filtro para obtener lista del codigo y nombre de cliente a partir de un numero de codigo escrito
def getOneClienteCodigo(codigo):
    clienteNames= list()
    for codigoN in FuncionDeConeccionClienteJson():
        if (codigoN.get("codigo_cliente")==codigo):
            clienteNames.append({
                "codigo del cliente": codigoN.get("codigo_cliente"),
                "nombre del cliente": codigoN.get("nombre_cliente")
            })
    return clienteNames






#fuiltro para devolver todos los datos segun un limite de credito y la ciudad

def  getAllClientCreditCiudad(limiteCredit,ciudad):
    clienteCredit=list()
    for val in FuncionDeConeccionClienteJson():
        if(val.get("limite_credito")>=limiteCredit and val.get("ciudad")==ciudad):
            clienteCredit.append(val)
    return clienteCredit






#filtro que devuelva la info de los clientes del limite y la ciudad
def  getAllClientCreditCiudad2(limiteCredit,ciudad):
    clienteCredit=[]
    for datos in FuncionDeConeccionClienteJson():
        if(datos.get("limite_credito")>=limiteCredit and datos.get("ciudad")==ciudad):
            clienteCredit.append({

                "Código": datos.get("codigo_cliente"),
                "Cliente": datos.get("nombre_cliente"),
                "Director": f"{datos.get('nombre_contacto')} {datos.get('apellido_contacto')}", #OJO CUIDADO, cuando aparece un  f"" lo que esté adentro si es una toma de info es mejor que dentro vaya en '' así: f"dato.get('')"
                "Telefono": datos.get("telefono"),
                "Fax": datos.get("fax"),
                "Direcciones": f"{datos.get('linea_direccion1')} {datos.get('linea_direccion2')}",
                "Origen":f"{datos.get('ciudad')} {datos.get('region')} {datos.get('pais')}",
                "Código del asesor": datos.get("codigo_empleado_rep_ventas"),
                "Crédito": datos.get("limite_credito")
            })
    return clienteCredit






# obtener pais region y ciudad de los clientes 
def getAllPaisRegionCiudad(pais,region=None,ciudad=None):
    clientZone = list()
    for val in FuncionDeConeccionClienteJson():
        if(
            val.get('pais')==pais and
            (val.get('region')==region or val.get('region')==None) or
            (val.get('ciudad')==ciudad or val.get('ciudad')==None)    
        ):
            clientZone.append(val)
    return clientZone         





#filtro para obtener nombre con la direccion numero 2 de los clientes
def obtener_informacion_clientes():
    clientes_info = []
    for cliente in FuncionDeConeccionClienteJson():
        info = {
            "nombre_cliente": cliente.get("nombre_cliente"),
            "linea_direccion2": cliente.get("linea_direccion2")
        }
        clientes_info.append(info)
    return clientes_info


#filtro para obtener los nombres de los clientes que contengan un código con número par
def GetAllCodePar ():
    clientes_info = []
    for cliente in FuncionDeConeccionClienteJson():
        codigo_cliente = cliente.get("codigo_cliente")
        if codigo_cliente % 2 == 0:  # Verifica si el código del cliente es par
            info = {
                "nombre_cliente": cliente.get("nombre_cliente"),
                "codigo_cliente": codigo_cliente
            }
            clientes_info.append(info)
    return clientes_info


#filtro que permita buscar clientes cuyos nombres coincidan parcialmente con un término de búsqueda proporcionado
def GetAllsimilarNames(nombre_busqueda):
    clientes_info = []
    for cliente in FuncionDeConeccionClienteJson():
        nombre_cliente = cliente.get("nombre_contacto")
        codigo_cliente = cliente.get("codigo_cliente")
        if nombre_busqueda.lower() in nombre_cliente.lower():  # Verificar si el término de búsqueda está contenido en el nombre del cliente
            info = {
                "nombre_contacto": nombre_cliente,
                "codigo_cliente": codigo_cliente
            }
            clientes_info.append(info)
    return clientes_info


#filtro que muestre clientes por país según el seleccionado
def GetAllClientCountry(pais):
    clientes_info = []
    for cliente in FuncionDeConeccionClienteJson():
        if cliente.get("pais") == pais:
            info = {
            "nombre_cliente": cliente.get("nombre_cliente"),
            "pais":cliente.get("pais")
        }
            clientes_info.append(info)
    return clientes_info


#filtro que muestre los clientes con el primer digito de telefono igual
def GetAllClientTel(numero_telefono):
    clientes_info = []
    for cliente in FuncionDeConeccionClienteJson():
        telefono_cliente = cliente.get("telefono", "")
        if str(telefono_cliente).startswith(str(numero_telefono)): #str para para convertir un objeto en su representación de cadena
            info = {
                "nombre_cliente": cliente.get("nombre_cliente"),
                "telefono": telefono_cliente
            }
            clientes_info.append(info)
    return clientes_info


#filtro que devuelve un listado con el nombre de todos los clientes españoles 
def GetAllNamesSpain():
    clientesEspañoles=[]
    for cliente in FuncionDeConeccionClienteJson():
        if (cliente.get("pais")=='Spain'):
            clientesEspañoles.append(
            {
             "Nombre":cliente.get("nombre_cliente")
            })
    return  clientesEspañoles


#Obtener los clientes que sean de una ciudad y su representante
def getAllCityRepresentants(ciudad,representante):
    AllCityRepresentants=[]
    for val in FuncionDeConeccionClienteJson():
        if val.get("ciudad")==ciudad and val.get("codigo_empleado_rep_ventas")==representante:
            AllCityRepresentants.append({
                "Código del cliente":val.get("codigo_cliente"),
                "Nombre del cliente":val.get("nombre_cliente"),
                "Teléfono":val.get("telefono"),
                "Ciudad":val.get("ciudad"),
                "Empleado":val.get("codigo_empleado_rep_ventas")
            })
    return AllCityRepresentants


# Obtener los nombres de los clientes y el nombre de sus representantes de ventas
def getAllClientAndRepresentant():
    AllClientAndRepresentant=[]
    for Nombrecliente in FuncionDeConeccionClienteJson():
        for NombreRepresentante in FuncionDeConeccionEmpleadoJson():
            if Nombrecliente.get("codigo_empleado_rep_ventas")==NombreRepresentante.get("codigo_empleado"):
                AllClientAndRepresentant.append({
                    "Nombre del cliente":Nombrecliente.get("nombre_cliente"),
                    "Nombre del representante":f'{NombreRepresentante.get("nombre")}{NombreRepresentante.get("apellido1")}{NombreRepresentante.get("apellido2")}',
                })
    return AllClientAndRepresentant



















# https://manytools.org/hacker-tools/ascii-banner/

def menu():
    while True:
        print("""
          
██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗███████╗                        
██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝                        
██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   █████╗                          
██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══╝                          
██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   ███████╗                        
╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝                        
                                                                                  
██████╗ ███████╗     ██████╗██╗     ██╗███████╗███╗   ██╗████████╗███████╗███████╗
██╔══██╗██╔════╝    ██╔════╝██║     ██║██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔════╝
██║  ██║█████╗      ██║     ██║     ██║█████╗  ██╔██╗ ██║   ██║   █████╗  ███████╗
██║  ██║██╔══╝      ██║     ██║     ██║██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ╚════██║
██████╔╝███████╗    ╚██████╗███████╗██║███████╗██║ ╚████║   ██║   ███████╗███████║
╚═════╝ ╚══════╝     ╚═════╝╚══════╝╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝
                                                                                  

    1. Obtener todos los clientes (código y nombre)         
    2. Obtener un cliente por el codigo (código y nombre)
    3. Obtener toda la información de un cliente segun su limite de credito y ciudad ( ejemplo:1500.0, San Francisco )
    4. Obtener todos los nombres de clientes según el país
    5. Obtener lista con los nombres de los clientes que contengan un código de número par
    6. Obtener los clientes que sean de una ciudad y su representante(ejemplo: Madrid, 11 o 30)
    7. Obtener los nombres de los clientes y el nombre de sus representantes de ventas
              
    EDITAR DATOS:      
    8. Modificar datos de clientes
              
    0. Salir al menu principal

""")
    

        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=8:

                    if(opcion==1):
                        print(tabulate(getAllCodesClients(), headers="keys",tablefmt="grid"))

                    if(opcion==2):
                        codigoCliente=int(input("Ingrese el codigo del cliente: "))
                        print(tabulate(getOneClienteCodigo(codigoCliente), headers="keys",tablefmt="github"))

                    if(opcion==3):
                        limite=float(input("Ingrese el límite de crédito de los clientes que deseas visualizar: "))
                        ciudad=input("Ingrese el nombre de la ciudad que deseas filtrar los clientes: ")
                        print(tabulate(getAllClientCreditCiudad2(limite,ciudad), headers="keys",tablefmt="github"))

                    if(opcion==4):
                        pais=input("Ingrese el pais de crédito de los clientes que deseas visualizar: ")
                        print(tabulate(GetAllClientCountry(pais), headers="keys",tablefmt="github"))
                    
                    if(opcion==5):
                        print(tabulate(GetAllCodePar(), headers="keys",tablefmt="github"))

                    if(opcion==6):
                        ciudad=input("\nIngresa la ciudad que deseas mostrar: ")
                        representante=int(input("Registra el código del representante: "))
                        print(tabulate(getAllCityRepresentants(ciudad, representante), headers="keys",tablefmt="github"))

                    if(opcion==7):
                        print(tabulate(getAllClientAndRepresentant(), headers="keys",tablefmt="github"))

                    if(opcion==8):
                        postcli.menu()

                    if(opcion==0):
                        break
                
   
