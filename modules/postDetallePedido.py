import json
import requests
from tabulate import tabulate
import re




def FuncionDeConeccionDetallePedidosJson():
      peticion=requests.get("http://10.0.2.15:5005") 
      Informacion=peticion.json()  
      return Informacion        




def agregarDetalleProductos():
    detallrProductos={}
    while True:
        try:
           



        except Exception as error:
            print(error)


    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://10.0.2.15:5005",headers=headers, data=json.dumps(gamasProducto, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Dato Guardado"
    return [res]












def menu():
    while True:
        print("""
 █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗██╗███████╗████████╗██████╗  █████╗ ██████╗ 
██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗
███████║██║  ██║██╔████╔██║██║██╔██╗ ██║██║███████╗   ██║   ██████╔╝███████║██████╔╝
██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║██║╚════██║   ██║   ██╔══██╗██╔══██║██╔══██╗
██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║██║███████║   ██║   ██║  ██║██║  ██║██║  ██║
╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
                                                                                    
██████╗ ███████╗████████╗ █████╗ ██╗     ██╗     ███████╗    ██████╗ ███████╗       
██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔════╝    ██╔══██╗██╔════╝       
██║  ██║█████╗     ██║   ███████║██║     ██║     █████╗      ██║  ██║█████╗         
██║  ██║██╔══╝     ██║   ██╔══██║██║     ██║     ██╔══╝      ██║  ██║██╔══╝         
██████╔╝███████╗   ██║   ██║  ██║███████╗███████╗███████╗    ██████╔╝███████╗       
╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝    ╚═════╝ ╚══════╝       
                                                                                    
██████╗ ███████╗██████╗ ██╗██████╗  ██████╗ ███████╗                                
██╔══██╗██╔════╝██╔══██╗██║██╔══██╗██╔═══██╗██╔════╝                                
██████╔╝█████╗  ██║  ██║██║██║  ██║██║   ██║███████╗                                
██╔═══╝ ██╔══╝  ██║  ██║██║██║  ██║██║   ██║╚════██║                                
██║     ███████╗██████╔╝██║██████╔╝╚██████╔╝███████║                                
╚═╝     ╚══════╝╚═════╝ ╚═╝╚═════╝  ╚═════╝ ╚══════╝                                
                                                                                    
                                     

        1. Guardar nuevo dato de detalle de pedido
              
        0. Atras       


        """)
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=1:  
                             
                    if(opcion==1):
                        print(tabulate(agregarDetalleProductos(), headers="keys",tablefmt="grid"))
                    if(opcion==0):
                        break