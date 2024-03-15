import json
import requests
from tabulate import tabulate





# def FuncionDeConeccionPedidoJson():
#       peticion=requests.get("http://10.0.2.15:5004") 
#       Informacion=peticion.json()  
#       return Informacion     


def agregarDatosPedido():
    pedido = {
    "codigo_pedido": int(input("Ingrese el código del pedido: ")),
    "fecha_pedido": input("Ingrese la fecha del pedido: "),
    "fecha_esperada":input("Ingrese la fecha esperada del pedido: "),
    "fecha_entrega":input("Ingrese la fecha de entrega del pedido: "),
    "estado":input("Ingrese el estado del pedido: "),
    "comentario": input("Ingrese un comentario: "),
    "codigo_cliente": int(input("Ingrese el código del cliente: ")),
}
    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://10.0.2.15:5004",headers=headers, data=json.dumps(pedido, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
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
                                                                                    
██████╗  █████╗ ████████╗ ██████╗ ███████╗    ██████╗ ███████╗██╗                   
██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝    ██╔══██╗██╔════╝██║                   
██║  ██║███████║   ██║   ██║   ██║███████╗    ██║  ██║█████╗  ██║                   
██║  ██║██╔══██║   ██║   ██║   ██║╚════██║    ██║  ██║██╔══╝  ██║                   
██████╔╝██║  ██║   ██║   ╚██████╔╝███████║    ██████╔╝███████╗███████╗              
╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝    ╚═════╝ ╚══════╝╚══════╝              
                                                                                    
██████╗ ███████╗██████╗ ██╗██████╗  ██████╗                                         
██╔══██╗██╔════╝██╔══██╗██║██╔══██╗██╔═══██╗                                        
██████╔╝█████╗  ██║  ██║██║██║  ██║██║   ██║                                        
██╔═══╝ ██╔══╝  ██║  ██║██║██║  ██║██║   ██║                                        
██║     ███████╗██████╔╝██║██████╔╝╚██████╔╝                                        
╚═╝     ╚══════╝╚═════╝ ╚═╝╚═════╝  ╚═════╝                                         

        1. Guardar un nuevo dato de un pedido
              
        0. Atras    

        

        """)
        opcion=int(input("\nSeleccione una de las opciones: "))
        
        if(opcion==1):
            print(tabulate(agregarDatosPedido(), headers="keys",tablefmt="grid"))
        if(opcion==0):
            break