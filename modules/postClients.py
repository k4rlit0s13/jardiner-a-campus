import json
import requests
from tabulate import tabulate
import re


# def FuncionDeConeccionClienteJson():
#       peticion=requests.get("http://10.0.2.15:5001") 
#       Informacion=peticion.json()  
#       return Informacion        


def agregarDatosCliente():
    cliente = {
    "codigo_cliente": input("Ingrese el código del cliente/empresa: "),
    "nombre_cliente": input("Ingrese el nombre del cliente/empresa: "),
    "nombre_contacto": input("Ingrese el nombre del contacto de la empresa: "),
    "apellido_contacto": input("Ingrese el apellido del contacto de la empresa: "),
    "telefono": int(input("Ingrese el telefono: ")),
    "fax": int(input("Ingrese el fax: ")),
    "linea_direccion1": (input("Ingrese la dirección 1: ")),
    "linea_direccion2": (input("Ingrese la dirección 2: ")),
    "ciudad": input("Ingrese la ciudad: "),
    "region": input("Ingrese la región: "),
    "pais": input("Ingrese el país: "),
    "codigo_postal": input("Ingrese el código postal: "),
    "codigo_empleado_rep_ventas": input("Ingrese el código del representante de ventas: "), 
    "limite_credito": float(input("Ingrese el limite del crédito del cliente: ")),
}
    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://10.0.2.15:5001",headers=headers, data=json.dumps(cliente, indent=4).encode("UTF-8"))
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
                                                                                                            
██████╗  █████╗ ████████╗ ██████╗ ███████╗     ██████╗██╗     ██╗███████╗███╗   ██╗████████╗███████╗███████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝    ██╔════╝██║     ██║██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔════╝
██║  ██║███████║   ██║   ██║   ██║███████╗    ██║     ██║     ██║█████╗  ██╔██╗ ██║   ██║   █████╗  ███████╗
██║  ██║██╔══██║   ██║   ██║   ██║╚════██║    ██║     ██║     ██║██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ╚════██║
██████╔╝██║  ██║   ██║   ╚██████╔╝███████║    ╚██████╗███████╗██║███████╗██║ ╚████║   ██║   ███████╗███████║
╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝     ╚═════╝╚══════╝╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝
                                                                                                                     
        1. Guardar un nuevo dato de un cliente
              
        0. Atras          
          
          
          
        

        """)
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=1:      
                         
                    if(opcion==1):
                        print(tabulate((), headers="keys",tablefmt="grid"))
                    if(opcion==0):
                        break       