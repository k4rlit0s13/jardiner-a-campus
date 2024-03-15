import json
import requests
from tabulate import tabulate
import re


# def FuncionDeConeccionClienteJson():
#       # json-server storage/producto.json -b 5006
#       peticion=requests.get("http://10.0.2.15:5006") #aqui tendremos que solocar una ip que es la que tendremos al iniciar el servidor, esto se hace con: json-server storage/producto.json -b (numero de puerto) OJO NUNCA DARLE KILL SOLO CERRAR, SERVIDOR ACTIVO FUNCIONARA EL CODIGO
#       Informacion=peticion.json()  # poner el servidor remoto, no el local, estamos usando simulacion de servidores
#       return Informacion        




# agregar datos en oficina

# def agregarDatosProducto():
#     producto = {
#     "codigo_producto": input("Ingrese el código del producto: "),
#     "nombre": input("Ingrese el nombre del producto: "),
#     "gama": input("Ingrese el tipo de gama(ejemplo: Ornamentales): "),
#     "dimensiones": input("Ingrese las dimensiones del producto: "),
#     "proveedor": input("Ingrese el proveedor: "),
#     "cantidad_en_stock": int(input("Ingrese la cantidad en stock: ")),
#     "precio_venta": int(input("Ingrese el precio de venta: ")),
#     "precio_proveedor": int(input("Ingrese el precio del proveedor: "))

# }
#     headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
#     peticion = requests.post("http://10.0.2.15:5006",headers=headers, data=json.dumps(producto, indent=4).encode("UTF-8"))
#     res = peticion.json()
#     res["Mensaje"] = "Producto Guardado"
#     return [res]
def agregarDatosProducto():
    producto={}
    while True:
        try:


            #
            # if not producto.get("codigo_producto"):




            # expresion regular que tenga en cuenta la escritura de un nombre con la primera letra en mayusc, que se pueda escribir en una sola palabra o mas de una y respete espacios entre si
            if not producto.get("nombre"):
                nombre =input("Ingrese el nombre del producto: ")
                if(re.match(r'^[A-Z][a-z]*(?: [A-Z][a-z]*)*$',nombre)is not None):
                    producto["nombre"]=nombre
                    print("El nombre cumple con el estandar,OK")
                    # break 
                else:
                    raise Exception("El nombre del producto no cumple con el estandar establecido")







        except ValueError as error:
            print("Error")
            print(error)






























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
                                                                                    
██████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗ ██████╗████████╗ ██████╗                 
██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔═══██╗                
██████╔╝██████╔╝██║   ██║██║  ██║██║   ██║██║        ██║   ██║   ██║                
██╔═══╝ ██╔══██╗██║   ██║██║  ██║██║   ██║██║        ██║   ██║   ██║                
██║     ██║  ██║╚██████╔╝██████╔╝╚██████╔╝╚██████╗   ██║   ╚██████╔╝                
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝   ╚═╝    ╚═════╝                 
                                                                                    
        1. Guardar un nuevo dato de Producto
              
        0. Atras


        

        """)
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=1:    
                    
                    if(opcion==1):
                        print(tabulate(agregarDatosProducto(), headers="keys",tablefmt="grid"))
                    if(opcion==0):
                        break