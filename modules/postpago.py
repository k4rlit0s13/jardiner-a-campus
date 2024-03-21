import json
import requests
from tabulate import tabulate
import re
import modules.getPago as getpa







# def agregarDatosPagos():
#     pago = {
#     "codigo_cliente": int(input("Ingrese el código del cliente: ")),
#     "forma_pago": input("Ingrese la forma de pago: "),
#     "id_transaccion": input("Ingrese el id de la transacción: "),
#     "fecha_pago": input("Ingrese la fecha de pago(año-mes-día): "),
#     "total": int(input("Ingrese el total del pago: ")),
# }
#     headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
#     peticion = requests.post("http://10.0.2.15:5007",headers=headers, data=json.dumps(pago, indent=4).encode("UTF-8"))
#     res = peticion.json()
#     res["Mensaje"] = "Producto Guardado"
#     return [res]


def FuncionDeConeccionPagoJson():
      peticion=requests.get("http://10.0.2.15:5008/pagos") 
      Informacion=peticion.json()  
      return Informacion    




# opcion 2 borrar datos de la lista 
def deletearProduct(code):

    data=getpa.getAllcode(code)

    if(len(data)):  
        peticion=requests.delete(f"http://10.0.2.15:5008/pagos/{id}")
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
    




def agregarDatosPagos():
    pagos={}
    while True:
        try:

            # expresion regulat que tenga en cuenta escribir un numero solamente
            if not pagos.get("codigo_cliente"):
                codigoCliente=input("Ingresa el codigo del cliente: ")
                if (re.match(r'^\d+$',codigoCliente)is not None):
                        codigoCliente= int(codigoCliente)
                        pagos["codigo_cliente"]=codigoCliente
                        print("El codigo del cliente cumple con el estandar, OK")
                        # break # el break se deja solo para el ultimo modulo sino se rompe toda la cadena
                else:
                    raise Exception("El código del cliente no cumple con el estandar establecido")  


            # expresion regular que tenga en cuenta la escritura de palabras con primera en mayuscula seguida de minusculas, que puedan tener mayusculas entre medias y se pueda escribir una o mas palabras separadas por espacios, que se pueda poner numeros y nada de caracteres especiales
            if not pagos.get("forma_pago"):
                formaPago =input("Ingresa el metodo de pago (ejemplo: PayPal): ")
                if(re.match(r'[A-Z][a-z]*(?:\s[A-Z][a-z]*)*(?:\s\d*)*',formaPago)is not None):
                    pagos["forma_pago"]=formaPago
                    print("La forma de pago cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("La forma de pago no cumple con el estandar establecido")


            # expresion que tenga en cuenta la escritura de ak-std-000000
            if not pagos.get("id_transaccion"):
                idTransaccion=input("Ingresa id de la transacción(ak-std-000000): ")
                if(re.match(r'ak-std-\d{6}',idTransaccion)is not None):
                    Data=getpa.getAllIdTransactions(idTransaccion)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("El id ya existe")
                        #break # el break se deja solo para el ultimo modulo sino se rompe toda la cadena
                    else:
                        pagos["id_transaccion"]=idTransaccion
                        print("El id cumple con el estandar, OK")
                else:
                    raise Exception("El id no cumple con el estandar establecido")


            # expresion que tenga en cuenta la escritura de una fecha año-mes-día
            if not pagos.get("fecha_pago"):
                fechaPago =input("Ingresa la fecha del pago(año-mes-día): ")
                if(re.match(r'^\d{4}-\d{2}-\d{2}$',fechaPago)is not None):
                    pagos["fecha_pago"]=fechaPago
                    print("la fecha del pago cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("La fecha del pago no cumple con el estandar establecido")



            # expresion que tenga en cuenta la escritura de un numero
            if not pagos.get("total"):
                pagototal=input("Ingresa el valor del total(entero): ")
                if (re.match(r'^\d+$',pagototal)is not None):
                        pagototal= int(pagototal)
                        pagos["total"]=pagototal
                        print("El dato cumple con el estandar, OK")
                        break # el break se deja solo para el ultimo modulo sino se rompe toda la cadena
                else:
                    raise Exception("El dato no cumple con el estandar establecido")  



        except Exception as error:
            print(error)
   

    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://10.0.2.15:5008/pagos",headers=headers, data=json.dumps(pagos, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]







def actualizarPagoTotal(code):
    nuevoValorPago = float(input("Ingrese el nuevo valor del pago: "))
    pagos = getpa.getAllcode(code)  # Obtener todos los pagos
    for pago in pagos:  # Buscar el pago con el ID proporcionado
        if pago.get("id") == id: # Actualizar el valor total del pago
            pago["total"] = nuevoValorPago
            try:
                peticion = requests.put(f"http://154.38.171.54:5006/pagos/{id}", json=pago)  # Realizar una solicitud PUT para actualizar el pago en el servidor
                res = peticion.json()
                return [res]  # Devolver la respuesta del servidor
            except requests.exceptions.RequestException as e:
                print("Error al realizar la solicitud PUT:", e)
                return None
    
    # Si no se encontró un pago con el ID proporcionado
    print(f"No se encontró un pago con ID {id}")
    return None








def actualizarPagos():
    while True:
        print("""
 █████╗  ██████╗████████╗██╗   ██╗ █████╗ ██╗     ██╗███████╗ █████╗ ██████╗            
██╔══██╗██╔════╝╚══██╔══╝██║   ██║██╔══██╗██║     ██║╚══███╔╝██╔══██╗██╔══██╗           
███████║██║        ██║   ██║   ██║███████║██║     ██║  ███╔╝ ███████║██████╔╝           
██╔══██║██║        ██║   ██║   ██║██╔══██║██║     ██║ ███╔╝  ██╔══██║██╔══██╗           
██║  ██║╚██████╗   ██║   ╚██████╔╝██║  ██║███████╗██║███████╗██║  ██║██║  ██║           
╚═╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝           
                                                                                        
██████╗  █████╗ ████████╗ ██████╗ ███████╗    ██████╗  █████╗  ██████╗  ██████╗ ███████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝    ██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗██╔════╝
██║  ██║███████║   ██║   ██║   ██║███████╗    ██████╔╝███████║██║  ███╗██║   ██║███████╗
██║  ██║██╔══██║   ██║   ██║   ██║╚════██║    ██╔═══╝ ██╔══██║██║   ██║██║   ██║╚════██║
██████╔╝██║  ██║   ██║   ╚██████╔╝███████║    ██║     ██║  ██║╚██████╔╝╚██████╔╝███████║
╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝
                                                                                        

        1. Actualizar codigo cliente      
        2. Actualizar forma de pago     
        3. Actualizar id transaccion    
        4. Actualizar fecha de pago
        5. Actualizar total
        6. Actualizar id
                                   
        0. Atras                                                                                                           
          
          
          
        

        """)
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=6:   
                           
                   
                  
                    if(opcion==0):
                        break













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
        2. Eliminar un dato     
        3. Actualizar datos
                     
        0. Atras                                                                                                           
          
          
          
        

        """)
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=3:   
                           
                    if(opcion==1):
                        print(tabulate(agregarDatosPagos(), headers="keys",tablefmt="grid"))
                    if(opcion==2):
                        idProducto=input("Ingrese el id del producto que desea eliminar: ")
                        print(tabulate(deletearProduct(idProducto)["body"],headers="keys",tablefmt="grid"))
                    if(opcion==3):
                        actualizarPagos()             
                    if(opcion==0):
                        break