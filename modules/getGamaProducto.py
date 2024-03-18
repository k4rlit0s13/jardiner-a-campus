# import storage.gama_producto as gama
from tabulate import tabulate

import requests
import json
import modules.postGamaProducto as postGama
import re








def FuncionDeConeccionGamaProductoJson():
      peticion=requests.get("http://10.0.2.15:5006/productos") 
      Informacion=peticion.json()  
      return Informacion        




#obtener un codigo de la lista directo(optimizado)
def deleteProducto(codigo):
       peticion=requests.get(f"http://10.0.2.15:5006/productos/{codigo}")
       return(peticion.json()) if peticion.ok else []






def getGamaformGama(gama):
     GamaformGama=[]
     for val in FuncionDeConeccionGamaProductoJson():
          if val.get("gama")==gama:
               return [val]




#Obtener toda la gama de productos
def getAllGamaProducts():
    AllStockPriceGama=[]
    for precio in FuncionDeConeccionGamaProductoJson():
        AllStockPriceGama.append({
            "Gama": precio.get("gama"),
            "Descripcion del produ": precio.get("descripcion_texto")
        })
    return AllStockPriceGama







def menu():
    while True:
        print(f"""
              
 ██████╗  █████╗ ███╗   ███╗ █████╗     ██████╗ ███████╗                    
██╔════╝ ██╔══██╗████╗ ████║██╔══██╗    ██╔══██╗██╔════╝                    
██║  ███╗███████║██╔████╔██║███████║    ██║  ██║█████╗                      
██║   ██║██╔══██║██║╚██╔╝██║██╔══██║    ██║  ██║██╔══╝                      
╚██████╔╝██║  ██║██║ ╚═╝ ██║██║  ██║    ██████╔╝███████╗                    
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝                    
                                                                            
██████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗ ██████╗████████╗ ██████╗ ███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔═══██╗██╔════╝
██████╔╝██████╔╝██║   ██║██║  ██║██║   ██║██║        ██║   ██║   ██║███████╗
██╔═══╝ ██╔══██╗██║   ██║██║  ██║██║   ██║██║        ██║   ██║   ██║╚════██║
██║     ██║  ██║╚██████╔╝██████╔╝╚██████╔╝╚██████╗   ██║   ╚██████╔╝███████║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝   ╚═╝    ╚═════╝ ╚══════╝
                                                                            

            1. Obtener toda la gama de productos
            
              
            EDITAR DATOS:      
            2. Modificar datos de productos
            
              
            0. Salir al menu principal

""")
        
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=2:    
                        
                    if(opcion==1):
                        print(tabulate(getAllGamaProducts(), headers="keys",tablefmt="grid"))
                    if(opcion==2):
                        postGama.menu()
                    if(opcion==0):
                        break