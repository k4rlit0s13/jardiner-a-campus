import json
import requests
from tabulate import tabulate
import re

import modules.getClients as getcli

def FuncionDeConeccionClienteJson():
      peticion=requests.get("http://10.0.2.15:5001/clientes") 
      Informacion=peticion.json()  
      return Informacion        


# def agregarDatosCliente():
#     cliente = {
#     "codigo_cliente": input("Ingrese el código del cliente/empresa: "),
#     "nombre_cliente": input("Ingrese el nombre del cliente/empresa: "),
#     "nombre_contacto": input("Ingrese el nombre del contacto de la empresa: "),
#     "apellido_contacto": input("Ingrese el apellido del contacto de la empresa: "),
#     "telefono": int(input("Ingrese el telefono: ")),
#     "fax": int(input("Ingrese el fax: ")),
#     "linea_direccion1": (input("Ingrese la dirección 1: ")),
#     "linea_direccion2": (input("Ingrese la dirección 2: ")),
#     "ciudad": input("Ingrese la ciudad: "),
#     "region": input("Ingrese la región: "),
#     "pais": input("Ingrese el país: "),
#     "codigo_postal": input("Ingrese el código postal: "),
#     "codigo_empleado_rep_ventas": input("Ingrese el código del representante de ventas: "), 
#     "limite_credito": float(input("Ingrese el limite del crédito del cliente: ")),
# }
#     headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
#     peticion = requests.post("http://10.0.2.15:5001",headers=headers, data=json.dumps(cliente, indent=4).encode("UTF-8"))
#     res = peticion.json()
#     res["Mensaje"] = "Producto Guardado"
#     return [res]



# opcion 2 borrar datos de la lista 
def deletearProduct(id):

    data=getcli.deleteProducto(id)

    if(len(data)):  
        peticion=requests.delete(f"http://10.0.2.15:5001/clientes/{id}")
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
    



def agregarDatosClientes():
    Clientes={}
    while True:
        try:


            # expresion regulat que tenga en cuenta escribir un numero solamente
            if not Clientes.get("codigo_cliente"):
                codigoCliente=input("Ingresa el codigo del cliente: ")
                if (re.match(r'^\d+$',codigoCliente)is not None):
                    codigoCliente= int(codigoCliente)
                    Data=getcli.getclientFormClient(codigoCliente)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("El código ya existe")
                        #break # el break se deja solo para el ultimo modulo sino se rompe toda la cadena
                else:
                    Clientes["codigo_cliente"]=codigoCliente
                    print("El codigo del cliente cumple con el estandar, OK")



            # expresion regular que tenga en cuenta la escritura de palabras para parrafos

            if not Clientes.get("nombre_cliente"):
                nombreCliente =input("Ingresa un nombre a la empresa: ")
                if(re.match(r'\w+',nombreCliente)is not None):
                    Clientes["nombre_cliente"]=nombreCliente
                    print("El dato cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                


            # expresion regular que tenga en cuenta la escritura de una palabra con la primera en mayuscula y el resto en minuscula

            if not Clientes.get("nombre_contacto"):
                nombreCliente =input("Ingresa un nombre de representante de la empresa(ejemplo: Juan): ")
                if(re.match(r'^[A-Z][a-z]*$',nombreCliente)is not None):
                    Clientes["nombre_contacto"]=nombreCliente
                    print("El dato cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                

            if not Clientes.get("apellido_contacto"):
                nombreCliente =input("Ingresa el apellido de representante de la empresa(ejemplo: Alberto): ")
                if(re.match(r'^[A-Z][a-z]*$',nombreCliente)is not None):
                    Clientes["apellido_contacto"]=nombreCliente
                    print("El dato cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                


            # expresion regular que tenga en cuenta la escritura de un numero de 9 digitos
            if not Clientes.get("telefono"):
                telefono=input("Ingresa el teléfono del cliente(000000000): ")
                if(re.match(r'^\d{9}$',telefono)is not None):
                    Data=getcli.getTelFromTelclient(telefono)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("El telefono del cliente ya existe")
                        #break #solo para el ultimo modulo sino se rompe
                    else:
                        Clientes["telefono"]=telefono
                        print("El dato cumple con el estandar,OK")

                else:
                    raise Exception("El dato no cumple con el estandar establecido")
       
            

            # expresion regular que tenga en cuenta la escritura de un numero de 9 digitos

            if not Clientes.get("fax"):
                fax=input("Ingresa el fax del cliente(000000000): ")
                if(re.match(r'^\d{9}$',fax)is not None):
                    Data=getcli.getfaxfromfax(fax)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("El fax del cliente ya existe")
                        #break #solo para el ultimo modulo sino se rompe
                    else:
                        Clientes["fax"]=fax
                        print("El dato cumple con el estandar,OK")

                else:
                    raise Exception("El dato no cumple con el estandar establecido")




            # expresion que tenga en cuenta la escritura de una direccion 
            if not Clientes.get("linea_direccion1"):
                direccion1=input("Ingresa la primera direccion del cliente: ")
                if(re.match(r'\w+',direccion1)is not None):
                    Data=getcli.getDireccion1FromDireccion(direccion1)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("la dirección ya existe")
                        #break #solo para el ultimo modulo sino se rompe
                    else:
                        Clientes["linea_direccion1"]=direccion1
                        print("El dato cumple con el estandar,OK")

                else:
                    raise Exception("El dato no cumple con el estandar establecido")
                


            if not Clientes.get("linea_direccion2"):
                direccion2=input("Ingresa la segunda direccion del cliente: ")
                if(re.match(r'\w+',direccion2)is not None):
                    Data=getcli.getDireccion2FromDireccion(direccion2)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("La dirección ya existe")
                        #break #solo para el ultimo modulo sino se rompe
                    else:
                        Clientes["linea_direccion2"]=direccion2
                        print("El dato cumple con el estandar,OK")

                else:
                    raise Exception("El dato no cumple con el estandar establecido")


            # expresion regular que tenga en cuenta una palabra con mayuscula al principio,o  que pueda ser toda mayuscula, o que pueda tener un guion, que puedan ser varias palabras, que pueda tener numeros ni caracteres especiales
            if not Clientes.get("ciudad"):
                ciudad =input("Ingresa la ciudad del cliente: ")
                if(re.match(r'^([A-ZÁÉÍÓÚÜ][a-záéíóúü]*-?)+[A-ZÁÉÍÓÚÜ]?[a-záéíóúü]*$',ciudad)is not None):
                    Clientes["ciudad"]=ciudad
                    print("El dato cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")



            if not Clientes.get("pais"):
                pais =input("Ingresa el país del cliente: ")
                if(re.match(r'^([A-ZÁÉÍÓÚÜ][a-záéíóúü]*-?)+[A-ZÁÉÍÓÚÜ]?[a-záéíóúü]*$',pais)is not None):
                    Clientes["pais"]=pais
                    print("El dato cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")



            if not Clientes.get("region"):
                region =input("Ingresa la región del cliente: ")
                if(re.match(r'^([A-ZÁÉÍÓÚÜ][a-záéíóúü]*-?)+[A-ZÁÉÍÓÚÜ]?[a-záéíóúü]*$',region)is not None):
                    Clientes["region"]=region
                    print("El dato cumple con el estandar,OK")
                    # break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")



            #expresion regular que tenga en cuenta la escritura de numeros solamente, o que escriba unas letras(obligatorio en mayuscula) junto con numeros separados por un espacio, o que pueda ser un numero seguido de un guión y luego más numeros todo pegado
            if not Clientes.get("codigo_postal"):
                codigoPostal =input("Ingresa el código postal del cliente(00000): ")
                if(re.match(r'^\d{5}$',codigoPostal)is not None):
                    Clientes["codigo_postal"]=codigoPostal
                    print("El dato cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")


            # expresion regular que tenga en cuenta la escritura de un numero 
            if not Clientes.get("codigo_empleado_rep_ventas"):
                codigoEmpleado =input("Ingresa el código del representante de ventas del cliente: ")
                if(re.match(r'^\d+$',codigoEmpleado)is not None):
                    codigoEmpleado=int(codigoEmpleado)
                    Clientes["codigo_empleado_rep_ventas"]=codigoEmpleado
                    print("El dato cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")


            # expresion regular que tenga en cuenta la escritura de un numero 
            if not Clientes.get("limite_credito"):
                limiteCredito =input("Ingresa el límite de crédito del cliente: ")
                if(re.match(r'^\d+$',limiteCredito)is not None):
                    limiteCredito=float(limiteCredito)
                    Clientes["limite_credito"]=limiteCredito
                    print("El dato cumple con el estandar,OK")
                    break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")



        except Exception as error:
            print(error)
   

    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://10.0.2.15:5001",headers=headers, data=json.dumps(Clientes, indent=4).encode("UTF-8"))
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
                                                                                                            
██████╗  █████╗ ████████╗ ██████╗ ███████╗     ██████╗██╗     ██╗███████╗███╗   ██╗████████╗███████╗███████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝    ██╔════╝██║     ██║██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔════╝
██║  ██║███████║   ██║   ██║   ██║███████╗    ██║     ██║     ██║█████╗  ██╔██╗ ██║   ██║   █████╗  ███████╗
██║  ██║██╔══██║   ██║   ██║   ██║╚════██║    ██║     ██║     ██║██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ╚════██║
██████╔╝██║  ██║   ██║   ╚██████╔╝███████║    ╚██████╗███████╗██║███████╗██║ ╚████║   ██║   ███████╗███████║
╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝     ╚═════╝╚══════╝╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝
                                                                                                                     
        1. Guardar un nuevo dato de un cliente
        2. Eliminar un dato
                    
        0. Atras          
          
          
          
        

        """)
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=2:      
                         
                    if(opcion==1):
                        print(tabulate(agregarDatosClientes(), headers="keys",tablefmt="grid"))
                    if(opcion==2):
                        idProducto=input("Ingrese el id del producto que desea eliminar: ")
                        print(tabulate(deletearProduct(idProducto)["body"],headers="keys",tablefmt="grid"))                        
                    if(opcion==0):
                        break       