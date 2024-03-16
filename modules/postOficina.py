import json
import requests
from tabulate import tabulate
import re

# def FuncionDeConeccionOficinaJson():
#       peticion=requests.get("http://10.0.2.15:5002") 
#       Informacion=peticion.json()  
#       return Informacion        






# agregar datos en oficina

# def agregarDatosOficina():
#     oficina = {
#     "codigo_oficina": input("Ingrese el codigo de la oficina: "),
#     "ciudad": input("Ingrese la ciudad de la oficina: "),
#     "pais": input("Ingrese el país de la oficina: "),
#     "region": input("Ingrese la región de la oficina: "),
#     "codigo_postal": input("Ingrese el código postal de la oficina: "),
#     "telefono": input("Ingrese el teléfono de la oficina: "),
#     "linea_direccion1": int(input("Ingrese la dirección 1 de la oficina: ")),
#     "linea_direccion2": int(input("Ingrese la dirección 2 de la oficina: "))
# }
#     headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
#     peticion = requests.post("http://10.0.2.15:5002",headers=headers, data=json.dumps(oficina, indent=4).encode("UTF-8"))
#     res = peticion.json()
#     res["Mensaje"] = "Producto Guardado"
#     return [res]


def agregarDatosoficina():
    pagos={}
    while True:
        try:
            # expresion regulat que tenga en cuenta escribir un numero solamente
            if not pagos.get("codigo_oficina"):
                codigoCliente=input("Ingresa el codigo del cliente: ")
                if (re.match(r'^\d+$',codigoCliente)is not None):
                        codigoCliente= int(codigoCliente)
                        pagos["codigo_cliente"]=codigoCliente
                        print("El codigo del cliente cumple con el estandar, OK")
                        break # el break se deja solo para el ultimo modulo sino se rompe toda la cadena
                else:
                    raise Exception("El código del cliente no cumple con el estandar establecido")  

        except Exception as error:
            print(error)
   

    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://10.0.2.15:5002",headers=headers, data=json.dumps(pedidos, indent=4).encode("UTF-8"))
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
                                                                                    
██████╗  █████╗ ████████╗ ██████╗ ███████╗    ██████╗ ███████╗    ██╗      █████╗   
██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝    ██╔══██╗██╔════╝    ██║     ██╔══██╗  
██║  ██║███████║   ██║   ██║   ██║███████╗    ██║  ██║█████╗      ██║     ███████║  
██║  ██║██╔══██║   ██║   ██║   ██║╚════██║    ██║  ██║██╔══╝      ██║     ██╔══██║  
██████╔╝██║  ██║   ██║   ╚██████╔╝███████║    ██████╔╝███████╗    ███████╗██║  ██║  
╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝    ╚═════╝ ╚══════╝    ╚══════╝╚═╝  ╚═╝  
                                                                                    
 ██████╗ ███████╗██╗ ██████╗██╗███╗   ██╗ █████╗                                    
██╔═══██╗██╔════╝██║██╔════╝██║████╗  ██║██╔══██╗                                   
██║   ██║█████╗  ██║██║     ██║██╔██╗ ██║███████║                                   
██║   ██║██╔══╝  ██║██║     ██║██║╚██╗██║██╔══██║                                   
╚██████╔╝██║     ██║╚██████╗██║██║ ╚████║██║  ██║                                   
 ╚═════╝ ╚═╝     ╚═╝ ╚═════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝                                   
                                                                                             

        1. Guardar nuevo dato de oficina
              
        0. Atras       




        """)
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=1:  
                             
                    if(opcion==1):
                        print(tabulate(agregarDatosOficina(), headers="keys",tablefmt="grid"))
                    if(opcion==0):
                        break