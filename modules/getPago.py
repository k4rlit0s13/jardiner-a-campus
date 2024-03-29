# import storage.pago as pa
# import storage.cliente as cli
# import storage.empleado as emp


from tabulate import tabulate

import json
import requests
import modules.postpago as postPa
import re



def FuncionDeConeccionPagoJson():
      peticion=requests.get("http://10.0.2.15:5008/pagos") 
      Informacion=peticion.json()  
      return Informacion        


def FuncionDeConeccionClienteJson():
      peticion=requests.get("http://10.0.2.15:5001/clientes") 
      Informacion=peticion.json()  
      return Informacion     


def FuncionDeConeccionEmpleadoJson():
      peticion=requests.get("http://10.0.2.15:5003/empleados") 
      Informacion=peticion.json()  
      return Informacion        






def getAllIdTransactions(code):
    transaction=[]
    for val in FuncionDeConeccionPagoJson():
         if val.get("id_transaccion")==id:
            return [val]






#obtener un codigo de la lista directo(optimizado)
def getAllcode(code):
       peticion=requests.get(f"http://10.0.2.15:5008/pagos/{id}")
       return[peticion.json()] if peticion.ok else []





#filtro para que devulve un listado en el codigo de cliente de aquellos clientes que realizaron algun pago en 2008, tenga en cuenta que debera eliminar  aquellos codigos de clientes que aparezcan repetidos. Resuelva la consulta

def getAll2008Clients():
    clientes_pagos_2008 = []  # Utilizamos un conjunto para asegurarnos de obtener códigos de cliente únicos
    for val in FuncionDeConeccionPagoJson():  # Suponemos que pago.pago es una lista que contiene todos los pagos
        fecha = val.get("fecha_pago")
        if fecha.startswith("2008"):  # Verificamos si la fecha de pago comienza con "2008"
            clientes_pagos_2008.append({
               "Código del cliente":val.get("codigo_cliente"),
               "fecha_pago":val.get("fecha_pago")
})
    return clientes_pagos_2008

    
#filtro que devuelva todos los pagos que se realizaron en el anio 2008 mediante paypal.ordene el resultado de mayor a menor

def getAllPaymentsPaypal2008():
    AllPaymentsPaypal2008=[]
    for pago in FuncionDeConeccionPagoJson():
        if pago.get("fecha_pago").startswith("2008") and pago.get("forma_pago")=="PayPal":
            AllPaymentsPaypal2008.append({
                    "fecha_pago":pago.get("fecha_pago"),
                    "forma_pago":pago.get("forma_pago"),
                    "total":pago.get("total")
                })
    AllPaymentsPaypal2008_ordenado = sorted(AllPaymentsPaypal2008, key=lambda x: x["total"], reverse=True)
    return AllPaymentsPaypal2008_ordenado


#filtro que devuelve un listado con todas las formas de pago que aparecen en la tabla pago. tenga en cuenta que no deben parecer formas de pago repetidas

def getAllFormToPay():
    allFormToPay=set()
    for pago in FuncionDeConeccionPagoJson():
        forma_pago=pago.get("forma_pago")
        allFormToPay.add(pago.get("forma_pago"))
    return allFormToPay


#Obtener todos los pagos realizados 
def getAllPays():
    Allpays=[]
    for val in FuncionDeConeccionPagoJson():
        Allpays.append({

           "Código del Cliente": val.get("codigo_cliente"),
            "Forma pago": val.get("forma_pago"),
            "ID transaccion": val.get("id_transaccion"),
            "Fecha pago": val.get("fecha_pago"),
            "Total": val.get("total"),
        })
    return Allpays


#Obtener el nombre de los clientes que hayan realizado pagos junto con el nombre de sus representantes
def getAllClientRepresentantsPayTrue():
    AllClientRepresentantsPayTrue=[]
    for pago in FuncionDeConeccionPagoJson():
        for Nombrecliente in FuncionDeConeccionClienteJson():
            for Representante in FuncionDeConeccionEmpleadoJson():
                    if (pago.get("codigo_cliente")==Nombrecliente.get("codigo_cliente")) and (Representante.get("codigo_empleado")==(Nombrecliente.get("codigo_empleado_rep_ventas"))):

                        AllClientRepresentantsPayTrue.append({
                        "Nombre del cliente": Nombrecliente.get("nombre_cliente"),
                        "Representante": f'{Representante.get("nombre")}{Representante.get("apellido1")}{Representante.get("apellido2")}',
                        "Fecha":pago.get("fecha_pago"),
                        "Precio pagado":pago.get("total")
                })
    return AllClientRepresentantsPayTrue


#muestra el nombre de los clientes que no hayan realizado pagos junto con el nombre de sus representantes de ventas

def getAllPaysFalse1():
    AllPaysFalse1 = []
    for val in FuncionDeConeccionClienteJson():
        pagos = False
    for val2 in FuncionDeConeccionPagoJson():
        if val.get("codigo_cliente") == val2.get("codigo_cliente"):
            pagos = True
            break
        if not pagos:
            for val3 in FuncionDeConeccionEmpleadoJson():
                if val.get('codigo_empleado_rep_ventas') == val3.get("codigo_empleado"):
                    if val2.get("puesto") == "Representante Ventas":
                        AllPaysFalse1.append({
                                "codigo": val.get("codigo_cliente"),
                                "Nombre Cliente": val.get("nombre_cliente"),
                                "puesto": val2.get("puesto"),
                                "Representante de ventas": val3.get("nombre")
                            })
    return AllPaysFalse1










def menu():
    while True:
        print("""
              
██████╗  █████╗  ██████╗  ██████╗ ███████╗
██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗██╔════╝
██████╔╝███████║██║  ███╗██║   ██║███████╗
██╔═══╝ ██╔══██║██║   ██║██║   ██║╚════██║
██║     ██║  ██║╚██████╔╝╚██████╔╝███████║
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝
        
        1. Obtener todos los pagos 
        2. Obtener todos los pagos que se realizaron en el anio 2008 mediante PayPal
        3. Obtener el codigo de cliente de aquellos clientes que realizaron algun pago en 2008
        4. Obtener todas las formas de pago 
        5. Obtener el nombre de los clientes que hayan realizado pagos junto con el nombre de sus representantes
        6. Obtener el nombre de los clientes que no hayan realizado pagos junto con el nombre de sus representantes de ventas
       
        EDITAR DATOS:      
        7. Modificar datos de pagos
                    
        0. Salir al menu principal

""")
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
            opcion= int(opcion)
            if opcion>=0 and opcion<=7:

                if(opcion==1):
                    print(tabulate(getAllPays(), headers="keys",tablefmt="grid"))
                if(opcion==2):
                    print(tabulate(getAllPaymentsPaypal2008(), headers="keys",tablefmt="grid"))
                if(opcion==3):
                    print(tabulate(getAll2008Clients(), headers="keys",tablefmt="grid"))
                if(opcion==4):
                    print(tabulate(getAllFormToPay(), headers="keys",tablefmt="grid"))
                if(opcion==5):
                    print(tabulate(getAllClientRepresentantsPayTrue(), headers="keys",tablefmt="grid"))
                if(opcion==6):
                    print(tabulate(getAllPaysFalse1(), headers="keys",tablefmt="grid"))
                if(opcion==7):
                    postPa.menu()
                elif(opcion==0):
                    break