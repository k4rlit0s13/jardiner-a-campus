# import storage.pedido as pe
from tabulate import tabulate



import requests
import json
import modules.postPedido as postPe
import re

def FuncionDeConeccionPedidoJson():
      peticion=requests.get("http://10.0.2.15:5004") 
      Informacion=peticion.json()  
      return Informacion        

























#filtro para devolver un listado con los distintos estados por los que puede pasar un pedido

def obtener_estados_pedidos():
    estados = set()  # Utilizamos un conjunto para asegurarnos de obtener estados únicos
    for val in FuncionDeConeccionPedidoJson():  
        estado = val.get("estado")
        if val.get not in estados:
            estados.add(estado)
    return estados

#filtro que devuelva un listado con el codigo de pedido, codigo de cliente, fecha esperada y fecha de entrega de los pedidos que no han sido entregados a tiempo
#importar fechas
# def obtener_pedidos_entrega_tardia():
#     pedidos_entrega_tardia = []
#     for pedido in pe.pedido:
#         estado = pedido.get("estado")
#         if estado == "Entregado":
#             fecha_entrega = pedido.get("fecha_entrega")
#             fecha_esperada = pedido.get("fecha_esperada")
#             if fecha_entrega is not None and fecha_esperada is not None:
#                 fecha_entrega_split = fecha_entrega.split("-")
#                 fecha_esperada_split = fecha_esperada.split("-")
#                 if len(fecha_entrega_split) == 3 and len(fecha_esperada_split) == 3:
#                     fecha_entrega = "/".join(fecha_entrega_split[::-1])
#                     fecha_esperada = "/".join(fecha_esperada_split[::-1])
#                     if fecha_entrega > fecha_esperada:
#                         codigo_pedido = pedido.get("codigo_pedido")
#                         codigo_cliente = pedido.get("codigo_cliente")
#                         pedidos_entrega_tardia.append({
#                             "Código_de_pedido": codigo_pedido,
#                             "Código_de_cliente": codigo_cliente,
#                             "Fecha_esperada": fecha_esperada,
#                             "Fecha_de_entrega": fecha_entrega
#                         })
#     return pedidos_entrega_tardia

from datetime import datetime

def obtener_pedidos_entrega_tardia():
   pedidos_entrega_tardia=[{
        "Código_de_pedido": FuncionDeConeccionPedidoJson.get("codigo_pedido"),
        "Código_de_cliente": FuncionDeConeccionPedidoJson.get("codigo_cliente"),
        "Fecha_esperada": "/".join(pedido.get("fecha_esperada").split("-")[::-1]),
        "Fecha_de_entrega": "/".join(pedido.get("fecha_entrega").split("-")[::-1])
        } 
            for pedido in FuncionDeConeccionPedidoJson() if pedido.get("estado") == "Entregado"
            and pedido.get("fecha_entrega") and pedido.get("fecha_esperada")
            and pedido.get("fecha_entrega") > pedido.get("fecha_esperada")]
   return pedidos_entrega_tardia 

#filtro que devuelva el codigo del pedido, código de cliente, fecha esperada y fecha de entrega de los pedidos cuya fecha de entrega ha sido al menos 2 dias antes de la fecha esperada, usando la función adddate,datediff, sera posible es consulta utilizando el operador de suma o resta, comandos equivalentes para python
def getAllOrderClientDates2DaysAgo():
    pedidos_entrega_anticipada=[]
    for pedido in FuncionDeConeccionPedidoJson():

        fecha_entrega_base=(pedido.get("fecha_entrega"))
        fecha_esperada_base=(pedido.get("fecha_esperada"))

        if fecha_entrega_base is not None and fecha_esperada_base is not None:
            fecha_entrega = datetime.strptime(fecha_entrega_base, "%Y-%m-%d")
            fecha_esperada = datetime.strptime(fecha_esperada_base, "%Y-%m-%d")
            
            diferencia_dias=(fecha_esperada-fecha_entrega).days

            if diferencia_dias>=2:
                pedidos_entrega_anticipada.append(
                {
                    "código_pedido":pedido.get("codigo_pedido"),
                    "código_cliente":pedido.get("código_cliente"),
                    "fecha_esperada":pedido.get("fecha_esperada"),
                    "fecha_entrega":pedido.get("fecha_entrega")                
                }
                )
    return pedidos_entrega_anticipada 



#filtro que devuelva los pedidos rechazados en 2009
def getAllOrdersRefused2009():
    AllOrdersRefused2009=[]
    for pedido in FuncionDeConeccionPedidoJson():
        pedidos_2009=(pedido.get("fecha_pedido"))

        if pedidos_2009.startswith("2009") and pedido.get("estado")=="Rechazado":
            AllOrdersRefused2009.append(
                {
                    "codigo_pedido":pedido.get("codigo_pedido"),
                    "estado":pedido.get("estado"),
                    "fecha_pedido":pedido.get("fecha_pedido"),
                })
    return AllOrdersRefused2009



#filtro que devuelva todos los pedidos que han sido entregados en el mes de enero de cualquier año\
def getAllOrder01():
    AllOrder01=[]
    for pedido in FuncionDeConeccionPedidoJson():
        entrega=pedido.get("fecha_entrega")
        if entrega:
            year,month,_=entrega.split("-")
            if month=="01":  # Enero en las fechas dadas
                AllOrder01.append({
                "codigo_pedido":pedido.get("codigo_pedido"),
                "fecha_entrega":pedido.get("fecha_entrega"),
                "codigo_cliente":pedido.get("codigo_cliente")
            })
    return AllOrder01


import keyboard


def menu():
    while True:
        print("""
              
██████╗ ███████╗██████╗ ██╗██████╗  ██████╗ ███████╗
██╔══██╗██╔════╝██╔══██╗██║██╔══██╗██╔═══██╗██╔════╝
██████╔╝█████╗  ██║  ██║██║██║  ██║██║   ██║███████╗
██╔═══╝ ██╔══╝  ██║  ██║██║██║  ██║██║   ██║╚════██║
██║     ███████╗██████╔╝██║██████╔╝╚██████╔╝███████║
╚═╝     ╚══════╝╚═════╝ ╚═╝╚═════╝  ╚═════╝ ╚══════╝
                                                       
        1. Obtener todos los pedidos
        2. Obtener todos los pedidos que han sido entregados en el mes de enero de cualquier año
        3. Obtener los pedidos rechazados en 2009
        4. Obtener los distintos estados por los que puede pasar un pedido
        
        EDITAR DATOS:      
        5. Modificar datos de pedidos        
        
        0. Salir al menu principal
""")
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=5:      
                                 
                    if(opcion==1):
                        print(tabulate(getAllOrder01(), headers="keys",tablefmt="grid"))

                    if(opcion==2):
                        print(tabulate(getAllOrder01(), headers="keys",tablefmt="grid"))

                    if(opcion==3):
                        print(tabulate(getAllOrdersRefused2009(), headers="keys",tablefmt="grid"))

                    if(opcion==4):
                        print(tabulate(obtener_estados_pedidos(), headers="keys",tablefmt="grid"))
                    
                    if(opcion==5):
                        postPe.menu()

                    if(opcion==0):
                        break


