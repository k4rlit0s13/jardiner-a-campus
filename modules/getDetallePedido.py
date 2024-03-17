import requests
import json
import re
from tabulate import tabulate
import modules.postDetallePedido as postDe



def FuncionDeConeccionDetallePedidosJson():
      peticion=requests.get("http://10.0.2.15:5005") 
      Informacion=peticion.json()  
      return Informacion        




#obtener todos los detalles de los pedidos
def getAlldetallepedidos():
    detallespedidos= []
    for val in FuncionDeConeccionDetallePedidosJson():
            detallespedidos.append({
                "Código del pedido": val.get("codigo_pedido"),
                "Código del producto": val.get("codigo_producto"),
                "Cantidad": val.get("cantidad"),
                "Precio Unidad": val.get("precio_unidad"),
                "Número de Línea": val.get("numero_linea"),
            })
    return detallespedidos


def menu():
    while True:
        print("""
              
██████╗ ███████╗████████╗ █████╗ ██╗     ██╗     ███████╗███████╗       
██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔════╝██╔════╝       
██║  ██║█████╗     ██║   ███████║██║     ██║     █████╗  ███████╗       
██║  ██║██╔══╝     ██║   ██╔══██║██║     ██║     ██╔══╝  ╚════██║       
██████╔╝███████╗   ██║   ██║  ██║███████╗███████╗███████╗███████║       
╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝       
                                                                        
██████╗ ███████╗    ██████╗ ███████╗██████╗ ██╗██████╗  ██████╗ ███████╗
██╔══██╗██╔════╝    ██╔══██╗██╔════╝██╔══██╗██║██╔══██╗██╔═══██╗██╔════╝
██║  ██║█████╗      ██████╔╝█████╗  ██║  ██║██║██║  ██║██║   ██║███████╗
██║  ██║██╔══╝      ██╔═══╝ ██╔══╝  ██║  ██║██║██║  ██║██║   ██║╚════██║
██████╔╝███████╗    ██║     ███████╗██████╔╝██║██████╔╝╚██████╔╝███████║
╚═════╝ ╚══════╝    ╚═╝     ╚══════╝╚═════╝ ╚═╝╚═════╝  ╚═════╝ ╚══════╝
                                                                        
        
        1. Obtener todos los detalles de los pedidos
      
        EDITAR DATOS:      
        2. Guardar un detalle de pedido
                    
        0. Salir al menu principal

""")
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
            opcion= int(opcion)
            if opcion>=0 and opcion<=2:

                if(opcion==1):
                    print(tabulate(getAlldetallepedidos(), headers="keys",tablefmt="grid"))

                if(opcion==2):
                    postDe.menu()






