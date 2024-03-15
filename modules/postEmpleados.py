import json
import requests
from tabulate import tabulate




# def FuncionDeConeccionEmpleadoJson():
#       peticion=requests.get("http://10.0.2.15:5003") 
#       Informacion=peticion.json()  
#       return Informacion    

def agregarDatosEmpleado():
    empleado = {
    "codigo_empleado": int(input("Ingrese el código del empleado: ")),
    "nombre": input("Ingrese el nombre del empleado: "),
    "apellido1":input("Ingrese el primer apellido del empleado: "),
    "apellido2":input("Ingrese el segundo apellido del empleado: "),
    "extension":input("Ingrese la extensión del empleado: "),
    "email": input("Ingrese el email del empleado: "),
    "codigo_oficina": input("Ingrese la dirección 1: "),
    "codigo_jefe": int(input("Ingrese la dirección 2: ")),
    "puesto": input("Ingrese la ciudad: "),


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
            print(tabulate(agregarDatosEmpleado(), headers="keys",tablefmt="grid"))
        if(opcion==0):
            break
