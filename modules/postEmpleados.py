import json
import requests
from tabulate import tabulate
import re




# def agregarDatosEmpleado():
#     empleado = {
#     "codigo_empleado": int(input("Ingrese el código del empleado: ")),
#     "nombre": input("Ingrese el nombre del empleado: "),
#     "apellido1":input("Ingrese el primer apellido del empleado: "),
#     "apellido2":input("Ingrese el segundo apellido del empleado: "),
#     "extension":input("Ingrese la extensión del empleado: "),
#     "email": input("Ingrese el email del empleado: "),
#     "codigo_oficina": input("Ingrese el codigo de la oficina del empleado: "),
#     "codigo_jefe": int(input("Ingrese el código del jefe del empleado: ")),
#     "puesto": input("Ingrese el puesto del empleado: "),


# }
#     headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
#     peticion = requests.post("http://10.0.2.15:5003",headers=headers, data=json.dumps(empleado, indent=4).encode("UTF-8"))
#     res = peticion.json()
#     res["Mensaje"] = "Producto Guardado"
#     return [res]



def FuncionDeConeccionEmpleadoJson():
      peticion=requests.get("http://10.0.2.15:5003") 
      Informacion=peticion.json()  
      return Informacion    


def agregarDatosEmpleados():
    empleados={}
    while True:
        try:
            # expresion regulat que tenga en cuenta escribir un numero solamente
            if not empleados.get("codigo_cliente"):
                codigoCliente=input("Ingresa el codigo del cliente: ")
                if (re.match(r'^\d+$',codigoCliente)is not None):
                        codigoCliente= int(codigoCliente)
                        empleados["codigo_cliente"]=codigoCliente
                        print("El codigo del cliente cumple con el estandar, OK")
                        break # el break se deja solo para el ultimo modulo sino se rompe toda la cadena
                else:
                    raise Exception("El código del cliente no cumple con el estandar establecido")  

        except Exception as error:
            print(error)
   

    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://10.0.2.15:5003",headers=headers, data=json.dumps(pedidos, indent=4).encode("UTF-8"))
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
                                                                                                                          
██████╗  █████╗ ████████╗ ██████╗ ███████╗    ███████╗███╗   ███╗██████╗ ██╗     ███████╗ █████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝    ██╔════╝████╗ ████║██╔══██╗██║     ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║  ██║███████║   ██║   ██║   ██║███████╗    █████╗  ██╔████╔██║██████╔╝██║     █████╗  ███████║██║  ██║██║   ██║███████╗
██║  ██║██╔══██║   ██║   ██║   ██║╚════██║    ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  ██╔══██║██║  ██║██║   ██║╚════██║
██████╔╝██║  ██║   ██║   ╚██████╔╝███████║    ███████╗██║ ╚═╝ ██║██║     ███████╗███████╗██║  ██║██████╔╝╚██████╔╝███████║
╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝    ╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝
                                                                                                                             
         
        1. Guardar un nuevo dato de empleado
              
        0. Atras          
          
          
        """)
        
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=1:      
                                 
                    if(opcion==1):
                        print(tabulate(agregarDatosEmpleado(), headers="keys",tablefmt="grid"))
                    if(opcion==0):
                        break
