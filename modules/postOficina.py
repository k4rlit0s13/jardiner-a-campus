import json
import requests
from tabulate import tabulate


# def FuncionDeConeccionOficinaJson():
#       peticion=requests.get("http://10.0.2.15:5002") 
#       Informacion=peticion.json()  
#       return Informacion        






# agregar datos en oficina

def agregarDatosOficina():
    oficina = {
    "codigo_oficina": input("Ingrese el codigo de la oficina: "),
    "ciudad": input("Ingrese el nombre del empleado: "),
    "pais": input("Ingrese el país: "),
    "region": input("Ingrese la región: "),
    "codigo_postal": input("Ingrese el código postal: "),
    "telefono": input("Ingrese el teléfono: "),
    "linea_direccion1": int(input("Ingrese la dirección 1: ")),
    "linea_direccion2": int(input("Ingrese la dirección 2: "))
}
    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://10.0.2.15:5002",headers=headers, data=json.dumps(oficina, indent=4).encode("UTF-8"))
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
        opcion=int(input("\nSeleccione una de las opciones: "))
        
        if(opcion==1):
            print(tabulate(agregarDatosOficina(), headers="keys",tablefmt="grid"))
        if(opcion==0):
            break