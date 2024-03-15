import json
import requests
from tabulate import tabulate





# def FuncionDeConeccionGamaProductoJson():
#       peticion=requests.get("http://10.0.2.15:5005") 
#       Informacion=peticion.json()  
#       return Informacion    


def agregarDatosGama():
    gama = {
    "gama": input("Ingrese la gama del producto: "),
    "descripcion_texto": input("Ingrese una descripción del producto: "),
    "descripcion_html": input("Ingrese una descipción html del producto: "),
    
}
    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://10.0.2.15:5005",headers=headers, data=json.dumps(gama, indent=4).encode("UTF-8"))
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
                                                                                                              
██████╗  █████╗ ████████╗ ██████╗ ███████╗     ██████╗  █████╗ ███╗   ███╗ █████╗     ██████╗ ███████╗██╗     
██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝    ██╔════╝ ██╔══██╗████╗ ████║██╔══██╗    ██╔══██╗██╔════╝██║     
██║  ██║███████║   ██║   ██║   ██║███████╗    ██║  ███╗███████║██╔████╔██║███████║    ██║  ██║█████╗  ██║     
██║  ██║██╔══██║   ██║   ██║   ██║╚════██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══██║    ██║  ██║██╔══╝  ██║     
██████╔╝██║  ██║   ██║   ╚██████╔╝███████║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║██║  ██║    ██████╔╝███████╗███████╗
╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝╚══════╝
                                                                                                              
██████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗ ██████╗████████╗ ██████╗                                           
██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔═══██╗                                          
██████╔╝██████╔╝██║   ██║██║  ██║██║   ██║██║        ██║   ██║   ██║                                          
██╔═══╝ ██╔══██╗██║   ██║██║  ██║██║   ██║██║        ██║   ██║   ██║                                          
██║     ██║  ██║╚██████╔╝██████╔╝╚██████╔╝╚██████╗   ██║   ╚██████╔╝                                          
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝   ╚═╝    ╚═════╝                                           
                                                                                                                 
        1. Guardar un nuevo dato de gama de productos
              
        0. Atras          
          
          
          
        

        """)
        opcion=int(input("\nSeleccione una de las opciones: "))
        
        if(opcion==1):
            print(tabulate(agregarDatosGama(), headers="keys",tablefmt="grid"))
        if(opcion==0):
            break        