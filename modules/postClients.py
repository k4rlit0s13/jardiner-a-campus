import json
import requests
from tabulate import tabulate
import re

import modules.getClients as getcli


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











def FuncionDeConeccionClienteJson():
      peticion=requests.get("http://10.0.2.15:5001/clientes") 
      Informacion=peticion.json()  
      return Informacion        






def FuncionDeConeccionAUnaId(id):
      peticion=requests.get(f"http://10.0.2.15:5001/clientes/{id}") 
      return [peticion.json()] if peticion.ok else[]










# opcion 2 borrar datos de la lista 
def deletearProduct(id):

    data=getcli.getAllcode(id)

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
                else:
                    raise Exception("El dato no cumple con el estandar establecido")
                


            if not Clientes.get("apellido_contacto"):
                nombreCliente =input("Ingresa el apellido de representante de la empresa(ejemplo: Alberto): ")
                if(re.match(r'^[A-Z][a-z]*$',nombreCliente)is not None):
                    Clientes["apellido_contacto"]=nombreCliente
                    print("El dato cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")
                


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
    peticion = requests.post("http://10.0.2.15:5001/clientes",headers=headers, data=json.dumps(Clientes, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]





def actualizarCodigoDelCliente(id):

    # while True:
        # SEGUNDO hacemos las OPERACIONES para cada una de las actualizaciones que queremos hacer:

        #  # actualizar el codigo del cliente sin que se repita con alguno ya existente
        # codigo_cliente = (input("Ingresa el nuevo código del cliente: "))

        # # Validar solo números
        # if not re.match(r"^[0-9]+$", codigo_cliente):
        #     print("El código del cliente debe ser un número entero positivo.")
        #     continue
        # # Validar si el código ya existe
        # response = requests.get(f"http://10.0.2.15:5001/clientes/{codigo_cliente}")
        # if response.status_code == 200:
        #     print("El código del cliente ya existe.")
        #     continue

        # break



    # # actualizar el nombre del cliente sin que se repita con alguno ya existente
    # while True:
    #     # actualizar el nombre del cliente/empresa
    #     nombre_cliente = (input("Ingrese el nuevo nombre de la empresa: "))

    #     # Validar nombre
    #     if not re.match(r"^([A-ZÁÉÍÓÚÑÜa-záéíóúñü]+[ _-]?)+$", nombre_cliente):
    #         print("El nombre del cliente no es válido.")
    #         continue
    #      # Validar si el nombre ya existe
    #     response = requests.get(f"http://10.0.2.15:5001/clientes/{nombre_cliente}")
    #     if response.status_code == 200:
    #         print("El código del cliente ya existe.")
    #         continue

    #     break





    # # actualizar el nombre del contacto y se puede repetir
    # while True:
    #     # actualizar el nombre del contacto
    #     nombre_contacto=(input("Ingrese el nuevo nombre del representante de la empresa: "))

    #     # Validar nombre
    #     if not re.match(r"^([A-ZÁÉÍÓÚÑÜa-záéíóúñü]+[ _-]?)+$", nombre_contacto):
    #         print("El nombre del contacto no es válido.")
    #         continue
    #     #  # NO ES NECESARIO VALIDAR
    #     # response = requests.get(f"http://10.0.2.15:5001/clientes/{nombre_contacto}")
    #     # if response.status_code == 200:
    #     #     print("El código del cliente ya existe.")
    #     #     continue
    #     break



    # # actualizar el apellido del contacto y se puede repetir
    # while True:
    #     # actualizar el nombre del cliente/empresa
    #     apellido_contacto=(input("Ingrese el nuevo apellido del representante de la empresa: "))

    #     # Validar nombre
    #     if not re.match(r"^([A-ZÁÉÍÓÚÑÜa-záéíóúñü]+[ _-]?)+$", apellido_contacto):
    #         print("El nombre del contacto no es válido.")
    #         continue
    #     #  # NO ES NECESARIO VALIDAR
    #     # response = requests.get(f"http://10.0.2.15:5001/clientes/{apellido_contacto}")
    #     # if response.status_code == 200:
    #     #     print("El código del cliente ya existe.")
    #     #     continue
    #     break




    # while True:
    #      # actualizar el teléfono del cliente sin que se repita con alguno ya existente
    #     telefono = (input("Ingresa el nuevo teléfono del cliente: "))
    #     # Validar solo 11 números
    #     if not re.match(r"^[0-9]{11}$", telefono):
    #         print("El teléfono del cliente se construye de 11 números 00000000000.")
    #         continue
    #     # Validar si el telefono ya existe
    #     response = requests.get(f"http://10.0.2.15:5001/clientes/{telefono}")
    #     if response.status_code == 200:
    #         print("El teléfono del cliente ya existe.")
    #         continue
    #     break




    # while True:
    #      # actualizar el fax del cliente sin que se repita con alguno ya existente
    #     fax = (input("Ingresa el nuevo fax del cliente: "))
    #     # Validar solo 11 números
    #     if not re.match(r"^[0-9]{10}$",fax):
    #         print("El fax del cliente se construye de 10 números 0000000000.")
    #         continue
    #     # Validar si el fax ya existe
    #     response = requests.get(f"http://10.0.2.15:5001/clientes/{fax}")
    #     if response.status_code == 200:
    #         print("El fax del cliente ya existe.")
    #         continue
    #     break



    # while True:
    #         # actualizar la linea_direccion1 del cliente sin que se repita con alguno ya existente
    #         linea_direccion1 = (input("Ingresa la nueva dirección del cliente: "))
    #         # Validar números,letras espacios y carácteres especiales
    #         if not re.match(r"^[\x00-\xFF]+$",linea_direccion1):
    #             print("La dirección del cliente se construye por números,letras y carácteres especiales como el /.")
    #             continue
    #         # Validar si la direccion ya existe
    #         response = requests.get(f"http://10.0.2.15:5001/clientes/{linea_direccion1}")
    #         if response.status_code == 200:
    #             print("La dirección del cliente ya existe.")
    #             continue
    #         break




    # while True:
    #         # actualizar la linea_direccion2 del cliente sin que se repita con alguno ya existente
    #         linea_direccion2 = (input("Ingresa una nueva indicacion a la direccion del cliente: "))
    #         # Validar números,letras espacios y carácteres especiales
    #         if not re.match(r"^[\x00-\xFF]+$",linea_direccion2):
    #             print("La dirección del cliente se construye por números,letras y carácteres especiales como el /.")
    #             continue
    #         # Validar si la direccion2 ya existe
    #         response = requests.get(f"http://10.0.2.15:5001/clientes/{linea_direccion2}")
    #         if response.status_code == 200:
    #             print("El dato de la dirección del cliente ya existe.")
    #             continue
    #         break

      
    while True:
            # actualizar la ciudad del cliente sin que se repita con alguno ya existente
            ciudad = (input("Ingresa una nueva ciudad del cliente: "))
            # Validar números,letras espacios y carácteres especiales
            if not re.match(r"^([A-Za-záéíóúñü]{2,}(?:\s?[A-Za-záéíóúñü]{2,})*)$",ciudad):
                print("La ciudad se indica con primera en mayuscula .")
                continue
            # NO NESECITA VALIDAR
            response = requests.get(f"http://10.0.2.15:5001/clientes/{ciudad}")
            if response.status_code == 200:
                print("El dato de la dirección del cliente ya existe.")
                continue
            break
    


    # PRIMERO ponemos todo el listado de información de nuestra lista
    cliente = {
        # "codigo_cliente": int(codigo_cliente),
        # "nombre_cliente": (nombre_cliente),
        # "nombre_contacto":(nombre_contacto),
        # "apellido_contacto":(apellido_contacto),
        # "telefono":(telefono),
        # "fax":(fax),
        # "linea_direccion1":(linea_direccion1),
        # "linea_direccion2":(linea_direccion2),
        "ciudad":(ciudad),
        # "region":(region),
        # "pais":(pais),
        # "codigo_postal":(codigo_postal),
        # "codigo_empleado_rep_ventas":(codigo_empleado_rep_ventas),
        # "limite_credito":(limite_credito),
        # "id":(id)
        }





    clienteExistente=FuncionDeConeccionAUnaId(id)
    if not clienteExistente:
        return{"message":"Cliente no encontrado"}
    
    clienteActualizado= {**clienteExistente[0],**cliente}
    peticion=requests.put(f"http://10.0.2.15:5001/clientes/{id}",data=json.dumps(clienteActualizado))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]
















































def actualizarDatosClientes():
    while True:
            print("""
                
     █████╗  ██████╗████████╗██╗   ██╗ █████╗ ██╗     ██╗███████╗ █████╗ ██████╗                        
    ██╔══██╗██╔════╝╚══██╔══╝██║   ██║██╔══██╗██║     ██║╚══███╔╝██╔══██╗██╔══██╗                       
    ███████║██║        ██║   ██║   ██║███████║██║     ██║  ███╔╝ ███████║██████╔╝                       
    ██╔══██║██║        ██║   ██║   ██║██╔══██║██║     ██║ ███╔╝  ██╔══██║██╔══██╗                       
    ██║  ██║╚██████╗   ██║   ╚██████╔╝██║  ██║███████╗██║███████╗██║  ██║██║  ██║                       
    ╚═╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝                       
                                                                                                        
    ██████╗  █████╗ ████████╗ ██████╗ ███████╗     ██████╗██╗     ██╗███████╗███╗   ██╗████████╗███████╗
    ██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝    ██╔════╝██║     ██║██╔════╝████╗  ██║╚══██╔══╝██╔════╝
    ██║  ██║███████║   ██║   ██║   ██║███████╗    ██║     ██║     ██║█████╗  ██╔██╗ ██║   ██║   █████╗  
    ██║  ██║██╔══██║   ██║   ██║   ██║╚════██║    ██║     ██║     ██║██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  
    ██████╔╝██║  ██║   ██║   ╚██████╔╝███████║    ╚██████╗███████╗██║███████╗██║ ╚████║   ██║   ███████╗
    ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝     ╚═════╝╚══════╝╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝
                                                                                                        
                                            
            1.  Actualizar codigo del cliente (ingresa el entero desde 00,01...)                                                                                                        
            2.  Actualizar el nombre de la empresa
            3.  Actualizar el nombre del contacto
            4.  Actualizar telefono
            5.  Actualizar direcciones
            6.  Actualizar ciudad
            7.  Actualizar región
            8.  Actualizar código postal
            9.  Actualizar codigo del representante de ventas
            10. Actualizar límite de crédito
                
            11. Actualizar todos los datos anteriores
                        
            0. Atras          
            
                
                """)
            
            opcion=input("\nEscribe el número de una de las opciones: ")
            if(re.match(r'[0-9]+$',opcion)is not None):
                    opcion= int(opcion)
                    if opcion>=0 and opcion<=11:    


                        if opcion == 1:
                            id=input("Ingrese la id del cliente que desea actualizar: ")
                            print(tabulate(actualizarCodigoDelCliente(id),headers="keys",tablefmt="grid"))
                   



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
                                                                                                            
██████╗  █████╗ ████████╗ ██████╗ ███████╗     ██████╗██╗     ██╗███████╗███╗   ██╗████████╗███████╗███████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝    ██╔════╝██║     ██║██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔════╝
██║  ██║███████║   ██║   ██║   ██║███████╗    ██║     ██║     ██║█████╗  ██╔██╗ ██║   ██║   █████╗  ███████╗
██║  ██║██╔══██║   ██║   ██║   ██║╚════██║    ██║     ██║     ██║██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ╚════██║
██████╔╝██║  ██║   ██║   ╚██████╔╝███████║    ╚██████╗███████╗██║███████╗██║ ╚████║   ██║   ███████╗███████║
╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝     ╚═════╝╚══════╝╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝
                                                                                                                     
        1. Guardar un nuevo dato de un cliente
        2. Eliminar un dato
        3. Actualizar un dato de clientes
                    
        0. Atras          
          
          
          
        

        """)
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=3:      
                         
                    if(opcion==1):
                        print(tabulate(agregarDatosClientes(), headers="keys",tablefmt="grid"))
                    if(opcion==2):
                        idProducto=input("Ingrese el id del cliente que desea eliminar: ")
                        print(tabulate(deletearProduct(idProducto)["body"],headers="keys",tablefmt="grid"))
                    if(opcion==3):
                        actualizarDatosClientes()                         
                    if(opcion==0):
                        break       









        
    





























































































