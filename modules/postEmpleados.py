import json
import requests
from tabulate import tabulate




# def FuncionDeConeccionEmpleadoJson():
#       peticion=requests.get("http://10.0.2.15:5003") 
#       Informacion=peticion.json()  
#       return Informacion    

def agregarDatosEmpleado():
    empleado = {
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
    peticion = requests.post("http://10.0.2.15:5003",headers=headers, data=json.dumps(empleado, indent=4).encode("UTF-8"))
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
        
        opcion=int(input("\nSeleccione una de las opciones: "))
        
        if(opcion==1):
            print(tabulate((), headers="keys",tablefmt="grid"))
        if(opcion==0):
            break
