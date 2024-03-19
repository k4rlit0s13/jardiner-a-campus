import json
import requests
from tabulate import tabulate
import re

import modules.getGamaProducto as getgama

 


# def agregarDatosGama():
#     gama = {
#     "gama": input("Ingrese la gama del producto: "),
#     "descripcion_texto": input("Ingrese una descripción del producto: "),
#     "descripcion_html": input("Ingrese una descipción html del producto: "),
    
# }


def FuncionDeConeccionGama():
    peticion=requests.get("http://10.0.2.15:5006/gama_productos") 
    Informacion=peticion.json()  
    return Informacion    



# opcion 2 borrar datos de la lista 
def deletearProduct(id):

    data=getgama.deleteProducto(id)

    if(len(data)):  
        peticion=requests.delete(f"http://10.0.2.15:5006/gama_productos/{id}")
        if(peticion.status_code==204):
            data.append({"message":"producto eliminado correctamente"})
            return {
              "body":data,
              "status":peticion.status_code,
         }
    else:
        return{
              "body":[{
                   "message":"producto no encontrado",
                   "id":id
              }],
              "status":400,
         }
    



def agregarDatosGama():
    gamasProducto={}
    while True:
        try:
           




            #expresion regular que escriba una palabra con la primera en mayuscula seguido de minusculas solo una palabra
           if not gamasProducto.get("gama"):
                idTransaccion=input("Ingresa la nueva gama de producto(ejemplo: Herramientas): ")
                if(re.match(r'^[A-Z][a-z]+$',idTransaccion)is not None):
                    Data=getgama.getGamaformGama(idTransaccion)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("El dato ya existe")
                        #break # el break se deja solo para el ultimo modulo sino se rompe toda la cadena
                    else:
                        gamasProducto["gama"]=idTransaccion
                        print("El dato cumple con el estandar, OK")
                else:
                    raise Exception("El dato no cumple con el estandar establecido")
    





                if not gamasProducto.get("descripcion_texto"):
                    descripcionGama =input("Ingresa un comentario sobre la nueva gama: ")
                    if(re.match(r'\w+',descripcionGama)is not None):
                        gamasProducto["descripcion_texto"]=descripcionGama
                        print("El comentario cumple con el estandar,OK")
                        break #solo para el ultimo modulo sino se rompe









        except Exception as error:
            print(error)


    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://10.0.2.15:5006",headers=headers, data=json.dumps(gamasProducto, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Dato Guardado"
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
        2. Eliminar un dato
                    
        0. Atras          
          
          
          
        

        """)
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
            opcion=int(opcion)
            if opcion>=0 and opcion<=2:      
                if(opcion==1):
                    print(tabulate(agregarDatosGama(), headers="keys",tablefmt="grid"))
                if(opcion==2):
                    idProducto=input("Ingrese el id del producto que desea eliminar: ")
                    print(tabulate(deletearProduct(idProducto)["body"],headers="keys",tablefmt="grid"))                    
                elif(opcion==0):
                    break        