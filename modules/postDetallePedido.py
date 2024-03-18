import json
import requests
from tabulate import tabulate
import re
import modules.getDetallePedido as getDe



def FuncionDeConeccionDetallePedidosJson():
      peticion=requests.get("http://10.0.2.15:5005") 
      Informacion=peticion.json()  
      return Informacion        







# opcion 2 borrar datos de la lista 
def deletearProduct(id):

    data=getDe.deleteProducto(id)

    if(len(data)):  
        peticion=requests.delete(f"http://10.0.2.15:5005/detalle_pedidos/{id}")
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
    



def agregarDetalleProductos():
    detalleProductos={}
    while True:
        try:
           

           # expresion que tenga en cuenta la escritura de 
            if not detalleProductos.get("codigo_pedido"):
                codigo=input("Ingresa el código del pedido: ")
                if(re.match(r'^\d+$',codigo)is not None):
                    codigo=int(codigo)
                    Data=getDe.getCodeByCode(codigo)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("El código del pedido ya es existente")
                        #break #solo para el ultimo modulo sino se rompe
                    else:
                        detalleProductos["codigo_pedido"]=codigo
                        print("El dato cumple con el estandar, OK")

            else:
                raise Exception("El dato no cumple con el estandar establecido, DENEGADO")


            # expresion que pueda escribir o solo letras en mayuscula, o letras en mayuscula, un guion y letras en mayuscula, no hay espacios y pueden haber numeros solo despues del guion, las mayusculas son obligatorias
            if not detalleProductos.get("codigo_producto"):
                productoCodigo=input("Ingresa el código del producto (ejemplo:OR-123): ")
                if(re.match(r'^[A-Z]+(-[A-Z]+)?$',productoCodigo)is not None):
                        detalleProductos["codigo_producto"]=productoCodigo
                        print("El código cumple con el estandar, OK")
            else:
                raise Exception("El código del producto no cumple con el estandar establecido, DENEGADO")




            if not detalleProductos.get("cantidad"):
                cantidad=input("Ingresa la cantidad: ")
                if (re.match(r'^\d+$',cantidad)is not None):
                        cantidad= int(cantidad)
                        detalleProductos["cantidad"]=cantidad
                        print("El dato cumple con el estandar, OK")
                        # break # el break se deja solo para el ultimo modulo sino se rompe toda la cadena
                else:
                    raise Exception("El dato no cumple con el estandar establecido")  



            # expresion regular que tenga en cuenta la escritura de un numero 

            if not detalleProductos.get("precio_unidad"):
                precioUnidad =input("Ingresa el precio de la unidad: ")
                if(re.match(r'^\d+$',precioUnidad)is not None):
                    precioUnidad=float(precioUnidad)
                    detalleProductos["precio_unidad"]=precioUnidad
                    print("El dato cumple con el estandar,OK")
                    # break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")



            if not detalleProductos.get("numero_linea"):
                numerolinea=input("Ingresa el numero de la línea: ")
                if (re.match(r'^\d+$',numerolinea)is not None):
                    numerolinea= int(numerolinea)
                    detalleProductos["numero_linea"]=numerolinea
                    print("El dato cumple con el estandar, OK")
                    break # el break se deja solo para el ultimo modulo sino se rompe toda la cadena
                else:
                    raise Exception("El dato no cumple con el estandar establecido")  




        except Exception as error:
            print(error)


    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://10.0.2.15:5005",headers=headers, data=json.dumps(detalleProductos, indent=4).encode("UTF-8"))
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
                                                                                    
██████╗ ███████╗████████╗ █████╗ ██╗     ██╗     ███████╗    ██████╗ ███████╗       
██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔════╝    ██╔══██╗██╔════╝       
██║  ██║█████╗     ██║   ███████║██║     ██║     █████╗      ██║  ██║█████╗         
██║  ██║██╔══╝     ██║   ██╔══██║██║     ██║     ██╔══╝      ██║  ██║██╔══╝         
██████╔╝███████╗   ██║   ██║  ██║███████╗███████╗███████╗    ██████╔╝███████╗       
╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝    ╚═════╝ ╚══════╝       
                                                                                    
██████╗ ███████╗██████╗ ██╗██████╗  ██████╗ ███████╗                                
██╔══██╗██╔════╝██╔══██╗██║██╔══██╗██╔═══██╗██╔════╝                                
██████╔╝█████╗  ██║  ██║██║██║  ██║██║   ██║███████╗                                
██╔═══╝ ██╔══╝  ██║  ██║██║██║  ██║██║   ██║╚════██║                                
██║     ███████╗██████╔╝██║██████╔╝╚██████╔╝███████║                                
╚═╝     ╚══════╝╚═════╝ ╚═╝╚═════╝  ╚═════╝ ╚══════╝                                
                                                                                    
                                     

        1. Guardar nuevo dato de detalle de pedido
              
        0. Atras       


        """)
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=1:  
                             
                    if(opcion==1):
                        print(tabulate(agregarDetalleProductos(), headers="keys",tablefmt="grid"))
                    if(opcion==0):
                        break