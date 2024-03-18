import json
import requests
from tabulate import tabulate
import re
import modules.getPedido as getPe

# EL MODULO DE LAS EXPRESIONES REGULARES PARA AGREGAR UN DATO:

# while True:
#     try:

#         if not NombreDeLDiccionarioDentroDeLaFuncion.get("LakeyDelJson"):
#             variableNombre =input("Ingresa el dato ---")
#             if(re.match(r'LA EXPRESION REGULAR',variableNombre)is not None):
#                     NombreDeLDiccionarioDentroDeLaFuncion["LakeyDelJson"]=variableNombre
#                     print("El código cumple con el estandar, OK")
#             else:
#                 raise Exception("El dato de -- no cumple con el estandar establecido")


#     except Exception as error:
#         print(error)

# EL MODULO DE LAS EXPRESIONES REGULARES PARA COMPROBAR QUE HAY DATOS IGUALES:

# while True:
#     try:

#         if not NombreDeLDiccionarioDentroDeLaFuncion.get("LakeyDelJson"):
#             variableNombre =input("Ingresa el dato ---")
#             if(re.match(r'LA EXPRESION REGULAR',variableNombre)is not None):
#                 Data= importDelGetRespectivo.laFuncionQueNeseciteComprobar(nombreDeLaVariableQueActuaDeparámetro(lo que esta en los get))
#                 if(Data):
#                     print(tabulate(Data, headers="keys",tablefmt="grid"))
#                     raise Exception("El dato de --- ya es existente")
#                     #break # el break se deja solo para el ultimo modulo sino se rompe toda la cadena
#                 else:
#                     NombreDeLDiccionarioDentroDeLaFuncion["LakeyDelJson"]=variableNombre
#                     print("El código cumple con el estandar, OK")
#             else:
#                 raise Exception("El dato de -- no cumple con el estandar establecido")


#     except Exception as error:
#         print(error)



#SERVER A CONECTAR LOS DATOS(JSON DE ESTE ARCHIVO.PY)

def FuncionDeConeccionPedidoJson():
      peticion=requests.get("http://10.0.2.15:5004") 
      Informacion=peticion.json()  
      return Informacion     


# ESTRUCTURA DE DATOS DE ESTE .PY

# def agregarDatosPedido():
#     pedido = {
#     "codigo_pedido": int(input("Ingrese el código del pedido: ")),
#     "fecha_pedido": input("Ingrese la fecha del pedido: "),
#     "fecha_esperada":input("Ingrese la fecha esperada del pedido: "),
#     "fecha_entrega":input("Ingrese la fecha de entrega del pedido: "),
#     "estado":input("Ingrese el estado del pedido: "),
#     "comentario": input("Ingrese un comentario: "),
#     "codigo_cliente": int(input("Ingrese el código del cliente: ")),
# }
#     headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
#     peticion = requests.post("http://10.0.2.15:5004",headers=headers, data=json.dumps(pedido, indent=4).encode("UTF-8"))
#     res = peticion.json()
#     res["Mensaje"] = "Producto Guardado"
#     return [res]


# opcion 2 borrar datos de la lista 
def deletearProduct(id):

    data=getPe.deleteProducto(id)

    if(len(data)):  
        peticion=requests.delete(f"http://10.0.2.15:5004/pedidos/{id}")
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



def agregarDatosPedido():
    pedidos={}
    while True:
        try:

            # expresion regulat que tenga en cuenta escribir un numero solamente

            if not pedidos.get("codigo_pedido"):
                codigoPedido=input("Ingresa el código del pedido: ")
                if(re.match(r'^\d+$',codigoPedido)is not None):
                    codigoPedido=int(codigoPedido)
                    Data=getPe.getCodeByCode(codigoPedido)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("El código ya existe")
                        #break # el break se deja solo para el ultimo modulo sino se rompe toda la cadena
                    else:
                        pedidos["codigo_pedido"]=codigoPedido
                        print("El código cumple con el estandar, OK")
                else:
                    raise Exception("El código no cumple con el estandar establecido")

 
            # expresion que tenga en cuenta la escritura de una fecha que va el año 4 numeros, quión,el mes 2 numeros,gión y el dia tambien 2 numeros
                
            if not pedidos.get("fecha_pedido"):
                fechaPedido =input("Ingresa la fecha del pedido(año-mes-día): ")
                if(re.match(r'^\d{4}-\d{2}-\d{2}$',fechaPedido)is not None):
                    pedidos["fecha_pedido"]=fechaPedido
                    print("la fecha del pedido cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("La fecha del pedido no cumple con el estandar establecido")



            if not pedidos.get("fecha_esperada"):
                fechaEsperada =input("Ingresa la fecha de espera(año-mes-día): ")
                if(re.match(r'^\d{4}-\d{2}-\d{2}$',fechaEsperada)is not None):
                    pedidos["fecha_esperada"]=fechaEsperada
                    print("la fecha de espera cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("La fecha de espera no cumple con el estandar establecido")



            if not pedidos.get("fecha_entrega"):
                fechaEntrega =input("Ingresa la fecha de entrega(año-mes-día): ")
                if(re.match(r'^\d{4}-\d{2}-\d{2}$',fechaEntrega)is not None):
                    pedidos["fecha_entrega"]=fechaEntrega
                    print("la fecha de entrega cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("La fecha de entrega no cumple con el estandar establecido")
                

                
            # expresion regular que tenga en cuenta la escritura de palabras primera letra en mayuscula seguidas de minusculas, una palabra única, nada más, sin numeros ni simbolos especiales

            if not pedidos.get("estado"):
                estado =input("Ingresa el estado del producto (ejemplos: Entregado, Pendiente, Rechazado): ")
                if(re.match(r'^[A-Z][a-z]+$',estado)is not None):
                    pedidos["estado"]=estado
                    print("El estado cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El estado no cumple con el estandar establecido")



            # expresion regular que tenga en cuenta la escritura de palabras para parrafos

            if not pedidos.get("comentario"):
                comentario =input("Ingresa un comentario sobre el pedido: ")
                if(re.match(r'\w+',comentario)is not None):
                    pedidos["comentario"]=comentario
                    print("El comentario cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                


            # expresion regulat que tenga en cuenta escribir un numero solamente
            if not pedidos.get("codigo_cliente"):
                codigoCliente=input("Ingresa el codigo del cliente: ")
                if (re.match(r'^\d+$',codigoCliente)is not None):
                        codigoCliente= int(codigoCliente)
                        pedidos["codigo_cliente"]=codigoCliente
                        print("El codigo del cliente cumple con el estandar, OK")
                        break # el break se deja solo para el ultimo modulo sino se rompe toda la cadena
                else:
                    raise Exception("El código del cliente no cumple con el estandar establecido")  



        except Exception as error:
            print(error)
   

    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://10.0.2.15:5004",headers=headers, data=json.dumps(pedidos, indent=4).encode("UTF-8"))
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
                                                                                    
██████╗  █████╗ ████████╗ ██████╗ ███████╗    ██████╗ ███████╗██╗                   
██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝    ██╔══██╗██╔════╝██║                   
██║  ██║███████║   ██║   ██║   ██║███████╗    ██║  ██║█████╗  ██║                   
██║  ██║██╔══██║   ██║   ██║   ██║╚════██║    ██║  ██║██╔══╝  ██║                   
██████╔╝██║  ██║   ██║   ╚██████╔╝███████║    ██████╔╝███████╗███████╗              
╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝    ╚═════╝ ╚══════╝╚══════╝              
                                                                                    
██████╗ ███████╗██████╗ ██╗██████╗  ██████╗                                         
██╔══██╗██╔════╝██╔══██╗██║██╔══██╗██╔═══██╗                                        
██████╔╝█████╗  ██║  ██║██║██║  ██║██║   ██║                                        
██╔═══╝ ██╔══╝  ██║  ██║██║██║  ██║██║   ██║                                        
██║     ███████╗██████╔╝██║██████╔╝╚██████╔╝                                        
╚═╝     ╚══════╝╚═════╝ ╚═╝╚═════╝  ╚═════╝                                         

        1. Guardar un nuevo dato de un pedido
        2. Eliminar un dato de pedido
                    
        0. Atras    

        

        """)
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=2:    
                        
        
                    if(opcion==1):
                        print(tabulate(agregarDatosPedido(), headers="keys",tablefmt="grid"))
                    if(opcion==2):
                        idProducto=input("Ingrese el id del producto que desea eliminar: ")
                        print(tabulate(deletearProduct(idProducto)["body"],headers="keys",tablefmt="grid"))                    
                    if(opcion==0):
                        break