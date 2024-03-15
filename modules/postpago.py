import json
import requests
from tabulate import tabulate







# def FuncionDeConeccionPagoJson():
#       peticion=requests.get("http://10.0.2.15:5007") 
#       Informacion=peticion.json()  
#       return Informacion    


def agregarDatosPagos():
    pago = {
    "codigo_cliente": int(input("Ingrese el código del cliente: ")),
    "forma_pago": input("Ingrese la forma de pago: "),
    "id_transaccion": input("Ingrese el id de la transacción: "),
    "fecha_pago": input("Ingrese la fecha de pago(año-mes-día): "),
    "total": int(input("Ingrese el total del pago: ")),
}
    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://10.0.2.15:5007",headers=headers, data=json.dumps(pago, indent=4).encode("UTF-8"))
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
                                                                                                            
██████╗  █████╗ ████████╗ ██████╗ ███████╗    ██████╗ ███████╗██╗         ██████╗  █████╗  ██████╗  ██████╗ 
██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝    ██╔══██╗██╔════╝██║         ██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗
██║  ██║███████║   ██║   ██║   ██║███████╗    ██║  ██║█████╗  ██║         ██████╔╝███████║██║  ███╗██║   ██║
██║  ██║██╔══██║   ██║   ██║   ██║╚════██║    ██║  ██║██╔══╝  ██║         ██╔═══╝ ██╔══██║██║   ██║██║   ██║
██████╔╝██║  ██║   ██║   ╚██████╔╝███████║    ██████╔╝███████╗███████╗    ██║     ██║  ██║╚██████╔╝╚██████╔╝
╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝    ╚═════╝ ╚══════╝╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ 


        1. Guardar un nuevo dato de un pago
              
        0. Atras                                                                                                           
          
          
          
        

        """)
        opcion=int(input("\nSeleccione una de las opciones: "))
        
        if(opcion==1):
            print(tabulate(agregarDatosPagos(), headers="keys",tablefmt="grid"))
        if(opcion==0):
            break