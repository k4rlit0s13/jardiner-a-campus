import json
import requests
from tabulate import tabulate





# def FuncionDeConeccionPedidoJson():
#       peticion=requests.get("http://10.0.2.15:5004") 
#       Informacion=peticion.json()  
#       return Informacion     


def agregarDatosPedido():
    pedido = {
    "codigo_pedido": int(input("Ingrese el código del cliente/empresa: ")),
    "fecha_pedido": input("Ingrese el nombre del cliente/empresa: "),
    "apellido1":input("Ingrese el nombre del contacto de la empresa: "),
    "apellido2":input("Ingrese el apellido del contacto de la empresa: "),
    "extension":input("Ingrese el telefono: "),
    "email": input("Ingrese el fax: "),
    "codigo_oficina": input("Ingrese la dirección 1: "),
    "codigo_jefe": int(input("Ingrese la dirección 2: ")),
    "puesto": input("Ingrese la ciudad: "),


"codigo_pedido": 1,
"fecha_pedido": "2006-01-17",
"fecha_esperada": "2006-01-19",
"fecha_entrega": "2006-01-19",
"estado": "Entregado",
"comentario": "Pagado a plazos",
"codigo_cliente": 5

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