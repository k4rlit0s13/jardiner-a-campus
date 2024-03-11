import storage.pago as pa
from tabulate import tabulate

#filtro para que devulve un listado en el codigo de cliente de aquellos clientes que realizaron algun pago en 2008, tenga en cuenta que debera eliminar  aquellos codigos de clientes que aparezcan repetidos. Resuelva la consulta

def getAll2008Clients():
    clientes_pagos_2008 = set()  # Utilizamos un conjunto para asegurarnos de obtener códigos de cliente únicos
    for val in pa.pago:  # Suponemos que pago.pago es una lista que contiene todos los pagos
        fecha_pago = val.get("fecha_pago")
        if fecha_pago.startswith("2008"):  # Verificamos si la fecha de pago comienza con "2008"
            clientes_pagos_2008.add(val.get("codigo_cliente"))

    return clientes_pagos_2008

    
#filtro que devuelva todos los pagos que se realizaron en el anio 2008 mediante paypal.ordene el resultado de mayor a menor

def getAllPaymentsPaypal2008():
    AllPaymentsPaypal2008=[]
    for pago in pa.pago:
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
    for pago in pa.pago:
        forma_pago=pago.get("forma_pago")
        allFormToPay.add(pago.get("forma_pago"))
    return allFormToPay


#Obtener todos los pagos realizados 
def getAllPays():
    Allpays=[]
    for pays in pa.pago:
        Allpays.append({

           "Código del Cliente": pays.get("codigo_cliente"),
            "Forma pago": pays.get("forma_pago"),
            "ID transaccion": pays.get("id_transaccion"),
            "Fecha pago": pays.get("fecha_pago"),
            "Total": pays.get("total"),
        })


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
        3. 
        4. todas las formas de pago 
              
        0. Salir al menu principal

""")
        opcion=int(input("\nSeleccione una de las opciones: "))

        if(opcion==1):
            print(tabulate(getAllPays(), headers="keys",tablefmt="grid"))
        if(opcion==2):
            print(tabulate(getAllPaymentsPaypal2008(), headers="keys",tablefmt="grid"))
            
        if(opcion==4):
            print(tabulate(getAllPaymentsPaypal2008(), headers="keys",tablefmt="grid"))
        elif(opcion==0):
                break