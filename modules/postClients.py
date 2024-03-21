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










# DELETE DATO
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
    

# POST DATO
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



#UPDATE DATO
def actualizarCodigoDelCliente(id):

    while True:
        # SEGUNDO hacemos las OPERACIONES para cada una de las actualizaciones que queremos hacer:

         # actualizar el codigo del cliente sin que se repita con alguno ya existente
        codigo_cliente = (input("Ingresa el nuevo código del cliente: "))

        # Validar solo números
        if not re.match(r"^[0-9]+$", codigo_cliente):
            print("El código del cliente debe ser un número entero positivo.")
            continue
        # Validar si el código ya existe
        response = requests.get(f"http://10.0.2.15:5001/clientes/{codigo_cliente}")
        if response.status_code == 200:
            print("El código del cliente ya existe.")
            continue

        break

    cliente = {
            "codigo_cliente":int(codigo_cliente)}


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

def actualizarNombreDelCliente(id):
    # actualizar el nombre del cliente sin que se repita con alguno ya existente
    while True:
        # actualizar el nombre del cliente/empresa
        nombre_cliente = (input("Ingrese el nuevo nombre de la empresa: "))

        # Validar nombre
        if not re.match(r"^([A-ZÁÉÍÓÚÑÜa-záéíóúñü]+[ _-]?)+$", nombre_cliente):
            print("El nombre del cliente no es válido.")
            continue
         # Validar si el nombre ya existe
        response = requests.get(f"http://10.0.2.15:5001/clientes/{nombre_cliente}")
        if response.status_code == 200:
            print("El código del cliente ya existe.")
            continue

        break
   # PRIMERO ponemos todo el listado de información de nuestra lista
    cliente = {"nombre_cliente":(nombre_cliente),}


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

def actualizarNombreDelContacto(id):

    while True:
            # actualizar el nombre del contacto
            nombre_contacto=(input("Ingrese el nuevo nombre del representante de la empresa: "))

            # Validar nombre
            if not re.match(r"^([A-ZÁÉÍÓÚÑÜa-záéíóúñü]+[ _-]?)+$", nombre_contacto):
                print("El nombre del contacto no es válido.")
                continue
            #  # NO ES NECESARIO VALIDAR
            # response = requests.get(f"http://10.0.2.15:5001/clientes/{nombre_contacto}")
            # if response.status_code == 200:
            #     print("El código del cliente ya existe.")
            #     continue
            break



    # actualizar el apellido del contacto y se puede repetir
    while True:
        # actualizar el nombre del cliente/empresa
        apellido_contacto=(input("Ingrese el nuevo apellido del representante de la empresa: "))

        # Validar nombre
        if not re.match(r"^([A-ZÁÉÍÓÚÑÜa-záéíóúñü]+[ _-]?)+$", apellido_contacto):
            print("El nombre del contacto no es válido.")
            continue
        #  # NO ES NECESARIO VALIDAR
        # response = requests.get(f"http://10.0.2.15:5001/clientes/{apellido_contacto}")
        # if response.status_code == 200:
        #     print("El código del cliente ya existe.")
        #     continue
        break
       
   # PRIMERO ponemos todo el listado de información de nuestra lista
    cliente = { 
         "nombre_contacto":(nombre_contacto),
        "apellido_contacto":(apellido_contacto),}


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

def actualizarTelefonoDelContacto(id):


    while True:
         # actualizar el teléfono del cliente sin que se repita con alguno ya existente
        telefono = (input("Ingresa el nuevo teléfono del cliente (11 dijitos 00000000000): "))
        # Validar solo 11 números
        if not re.match(r"^[0-9]{11}$", telefono):
            print("El teléfono del cliente se construye de 11 dígitos 00000000000.")
            continue
        # Validar si el telefono ya existe
        response = requests.get(f"http://10.0.2.15:5001/clientes/{telefono}")
        if response.status_code == 200:
            print("El teléfono del cliente ya existe.")
            continue
        break

   # PRIMERO ponemos todo el listado de información de nuestra lista
    cliente = {"telefono":(telefono),}


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

def actualizarDirecciones1Y2DelContacto(id):

    while True:
            # actualizar la linea_direccion1 del cliente sin que se repita con alguno ya existente
            linea_direccion1 = (input("Ingresa la nueva dirección del cliente: "))
            # Validar números,letras espacios y carácteres especiales
            if not re.match(r"^[\x00-\xFF]+$",linea_direccion1):
                print("La dirección del cliente se construye por números,letras y carácteres especiales como el /.")
                continue
            # Validar si la direccion ya existe
            response = requests.get(f"http://10.0.2.15:5001/clientes/{linea_direccion1}")
            if response.status_code == 200:
                print("La dirección del cliente ya existe.")
                continue
            break


    while True:
            # actualizar la linea_direccion2 del cliente sin que se repita con alguno ya existente
            linea_direccion2 = (input("Ingresa una nueva indicacion a la direccion del cliente: "))
            # Validar números,letras espacios y carácteres especiales
            if not re.match(r"^[\x00-\xFF]+$",linea_direccion2):
                print("La dirección del cliente se construye por números,letras y carácteres especiales como el /.")
                continue
            # Validar si la direccion2 ya existe
            response = requests.get(f"http://10.0.2.15:5001/clientes/{linea_direccion2}")
            if response.status_code == 200:
                print("El dato de la dirección del cliente ya existe.")
                continue
            break

   # PRIMERO ponemos todo el listado de información de nuestra lista
    cliente = {
        "linea_direccion1":(linea_direccion1),
        "linea_direccion2":(linea_direccion2)}
    

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

def actualizarCiudadDelContacto(id):

    while True:
            # actualizar la ciudad del cliente sin que se repita con alguno ya existente
            ciudad = (input("Ingresa una nueva ciudad del cliente: "))
            # Validar números,letras espacios y carácteres especiales
            if not re.match(r"^([A-Za-záéíóúñü]{2,}(?:\s?[A-Za-záéíóúñü]{2,})*)$",ciudad):
                print("La ciudad se indica con primera en mayuscula .")
                continue
            # NO NESECITA VALIDAR
            # response = requests.get(f"http://10.0.2.15:5001/clientes/{ciudad}")
            # if response.status_code == 200:
            #     print("El dato de la ciudad del cliente ya existe.")
            #     continue
            break
    
   # PRIMERO ponemos todo el listado de información de nuestra lista
    cliente = {"ciudad":(ciudad)}

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

def actualizarRegionDelContacto(id):

    while True:
            # actualizar la region del cliente sin que se repita con alguno ya existente
            region = (input("Ingresa una nueva región del cliente: "))
            # Validar números,letras espacios y carácteres especiales
            if not re.match(r"^([A-Za-záéíóúñü]{2,}(?:\s?[A-Za-záéíóúñü]{2,})*)$",region):
                print("La región se indica con primera en mayuscula .")
                continue
            # NO NESECITA VALIDAR
            # response = requests.get(f"http://10.0.2.15:5001/clientes/{region}")
            # if response.status_code == 200:
            #     print("El dato de region del cliente ya existe.")
            #     continue
            break
    
   # PRIMERO ponemos todo el listado de información de nuestra lista
    cliente = {"region":(region)}

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

def actualizarPaisContacto(id):

    while True:
            # actualizar el pais del cliente sin que se repita con alguno ya existente
            pais = (input("Ingresa un nuevo país del cliente: "))
            # Validar números,letras espacios y carácteres especiales
            if not re.match(r"^([A-Za-záéíóúñü]{2,}(?:\s?[A-Za-záéíóúñü]{2,})*)$",pais):
                print("El país se indica con primera en mayuscula .")
                continue
            # NO NESECITA VALIDAR
            # response = requests.get(f"http://10.0.2.15:5001/clientes/{pais}")
            # if response.status_code == 200:
            #     print("El dato de pais del cliente ya existe.")
            #     continue
            break

    
   # PRIMERO ponemos todo el listado de información de nuestra lista
    cliente = {"pais":(pais)}

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

def actualizarCodigoPostalContacto(id):

    while True:
            # actualizar el codigo postal sin que se repita con alguno ya existente
            codigo_postal = (input("Ingresa un nuevo código postal del cliente (5 números 00000): "))
            # Validar números,letras espacios y carácteres especiales
            if not re.match(r"^[0-9]{5}$",codigo_postal):
                print("El código postal se indica con  .")
                continue
            # NO NESECITA VALIDAR
            # response = requests.get(f"http://10.0.2.15:5001/clientes/{region}")
            # if response.status_code == 200:
            #     print("El dato de pais del cliente ya existe.")
            #     continue
            break

    cliente = {"codigo_postal":(codigo_postal),}

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

def actualizarRepresentanteContacto(id):

    while True:
            # actualizar el codigo del empleado sin que se repita con alguno ya existente
            codigo_empleado_rep_ventas = (input("Ingresa un nuevo codigo del empleado del cliente: "))
            # Validar números,letras espacios y carácteres especiales
            if not re.match(r"^[0-9]+$",codigo_empleado_rep_ventas):
                print("El codigo del empleadol se indica con un número.")
                continue
            # NO NESECITA VALIDAR
            # response = requests.get(f"http://10.0.2.15:5001/clientes/{codigo_empleado_rep_ventas}")
            # if response.status_code == 200:
            #     print("El dato de codigo del empleado del cliente ya existe.")
            #     continue
            break

    cliente = { "codigo_empleado_rep_ventas":int(codigo_empleado_rep_ventas)}

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

def actualizarLimiteCreditoContacto(id):

    while True:
            # actualizar el limite_credito del empleado sin que se repita con alguno ya existente
            limite_credito = (input("Ingresa un nuevo limite de crédito del cliente: "))
            # Validar números float
            if not re.match(r"^[0-9]+$",limite_credito):
                print("El limite crédito se indica con un número.")
                continue
            # NO NESECITA VALIDAR
            # response = requests.get(f"http://10.0.2.15:5001/clientes/{limite_credito}")
            # if response.status_code == 200:
            #     print("El dato de codigo del empleado del cliente ya existe.")
            #     continue
            break

    cliente = { "limite_credito":float(limite_credito)}

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

def actualizaridContacto(id):

    while True:
         # actualizar el codigo del cliente sin que se repita con alguno ya existente
        idNueva = (input("Ingresa el nuevo id del cliente(1,2,...): "))

        # Validar solo números
        if not re.match(r"^[0-9]+$", idNueva):
            print("El id del cliente debe ser un número entero positivo.")
            continue
        # Validar si el código ya existe
        response = requests.get(f"http://10.0.2.15:5001/clientes/{idNueva}")
        if response.status_code == 200:
            print("El id del cliente ya existe.")
            continue

        break

    cliente = {"id":int(idNueva)}

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

def actualizarTodoUnDatoCliente(id):

    while True:
        # SEGUNDO hacemos las OPERACIONES para cada una de las actualizaciones que queremos hacer:

         # actualizar el codigo del cliente sin que se repita con alguno ya existente
        codigo_cliente = (input("Ingresa el nuevo código del cliente: "))

        # Validar solo números
        if not re.match(r"^[0-9]+$", codigo_cliente):
            print("El código del cliente debe ser un número entero positivo.")
            continue
        # Validar si el código ya existe
        response = requests.get(f"http://10.0.2.15:5001/clientes/{codigo_cliente}")
        if response.status_code == 200:
            print("El código del cliente ya existe.")
            continue

        break



    # actualizar el nombre del cliente sin que se repita con alguno ya existente
    while True:
        # actualizar el nombre del cliente/empresa
        nombre_cliente = (input("Ingrese el nuevo nombre de la empresa: "))

        # Validar nombre
        if not re.match(r"^([A-ZÁÉÍÓÚÑÜa-záéíóúñü]+[ _-]?)+$", nombre_cliente):
            print("El nombre del cliente no es válido.")
            continue
         # Validar si el nombre ya existe
        response = requests.get(f"http://10.0.2.15:5001/clientes/{nombre_cliente}")
        if response.status_code == 200:
            print("El código del cliente ya existe.")
            continue

        break





    # actualizar el nombre del contacto y se puede repetir
    while True:
        # actualizar el nombre del contacto
        nombre_contacto=(input("Ingrese el nuevo nombre del representante de la empresa: "))

        # Validar nombre
        if not re.match(r"^([A-ZÁÉÍÓÚÑÜa-záéíóúñü]+[ _-]?)+$", nombre_contacto):
            print("El nombre del contacto no es válido.")
            continue
        #  # NO ES NECESARIO VALIDAR
        # response = requests.get(f"http://10.0.2.15:5001/clientes/{nombre_contacto}")
        # if response.status_code == 200:
        #     print("El código del cliente ya existe.")
        #     continue
        break



    # actualizar el apellido del contacto y se puede repetir
    while True:
        # actualizar el nombre del cliente/empresa
        apellido_contacto=(input("Ingrese el nuevo apellido del representante de la empresa: "))

        # Validar nombre
        if not re.match(r"^([A-ZÁÉÍÓÚÑÜa-záéíóúñü]+[ _-]?)+$", apellido_contacto):
            print("El nombre del contacto no es válido.")
            continue
        #  # NO ES NECESARIO VALIDAR
        # response = requests.get(f"http://10.0.2.15:5001/clientes/{apellido_contacto}")
        # if response.status_code == 200:
        #     print("El código del cliente ya existe.")
        #     continue
        break




    while True:
         # actualizar el teléfono del cliente sin que se repita con alguno ya existente
        telefono = (input("Ingresa el nuevo teléfono del cliente (11 dijitos 00000000000): "))
        # Validar solo 11 números
        if not re.match(r"^[0-9]{11}$", telefono):
            print("El teléfono del cliente se construye de 11 dígitos 00000000000.")
            continue
        # Validar si el telefono ya existe
        response = requests.get(f"http://10.0.2.15:5001/clientes/{telefono}")
        if response.status_code == 200:
            print("El teléfono del cliente ya existe.")
            continue
        break




    while True:
         # actualizar el fax del cliente sin que se repita con alguno ya existente
        fax = (input("Ingresa el nuevo fax del cliente(10 dígitos 0000000000): "))
        # Validar solo 11 números
        if not re.match(r"^[0-9]{10}$",fax):
            print("El fax del cliente se construye de 10 dígitos 0000000000.")
            continue
        # Validar si el fax ya existe
        response = requests.get(f"http://10.0.2.15:5001/clientes/{fax}")
        if response.status_code == 200:
            print("El fax del cliente ya existe.")
            continue
        break



    while True:
            # actualizar la linea_direccion1 del cliente sin que se repita con alguno ya existente
            linea_direccion1 = (input("Ingresa la nueva dirección del cliente: "))
            # Validar números,letras espacios y carácteres especiales
            if not re.match(r"^[\x00-\xFF]+$",linea_direccion1):
                print("La dirección del cliente se construye por números,letras y carácteres especiales como el /.")
                continue
            # Validar si la direccion ya existe
            response = requests.get(f"http://10.0.2.15:5001/clientes/{linea_direccion1}")
            if response.status_code == 200:
                print("La dirección del cliente ya existe.")
                continue
            break




    while True:
            # actualizar la linea_direccion2 del cliente sin que se repita con alguno ya existente
            linea_direccion2 = (input("Ingresa una nueva indicacion a la direccion del cliente: "))
            # Validar números,letras espacios y carácteres especiales
            if not re.match(r"^[\x00-\xFF]+$",linea_direccion2):
                print("La dirección del cliente se construye por números,letras y carácteres especiales como el /.")
                continue
            # Validar si la direccion2 ya existe
            response = requests.get(f"http://10.0.2.15:5001/clientes/{linea_direccion2}")
            if response.status_code == 200:
                print("El dato de la dirección del cliente ya existe.")
                continue
            break


      
    while True:
            # actualizar la ciudad del cliente sin que se repita con alguno ya existente
            ciudad = (input("Ingresa una nueva ciudad del cliente: "))
            # Validar números,letras espacios y carácteres especiales
            if not re.match(r"^([A-Za-záéíóúñü]{2,}(?:\s?[A-Za-záéíóúñü]{2,})*)$",ciudad):
                print("La ciudad se indica con primera en mayuscula .")
                continue
            # NO NESECITA VALIDAR
            # response = requests.get(f"http://10.0.2.15:5001/clientes/{ciudad}")
            # if response.status_code == 200:
            #     print("El dato de la ciudad del cliente ya existe.")
            #     continue
            break
    

    while True:
            # actualizar la region del cliente sin que se repita con alguno ya existente
            region = (input("Ingresa una nueva región del cliente: "))
            # Validar números,letras espacios y carácteres especiales
            if not re.match(r"^([A-Za-záéíóúñü]{2,}(?:\s?[A-Za-záéíóúñü]{2,})*)$",region):
                print("La región se indica con primera en mayuscula .")
                continue
            # NO NESECITA VALIDAR
            # response = requests.get(f"http://10.0.2.15:5001/clientes/{region}")
            # if response.status_code == 200:
            #     print("El dato de region del cliente ya existe.")
            #     continue
            break
    



    while True:
            # actualizar el pais del cliente sin que se repita con alguno ya existente
            pais = (input("Ingresa un nuevo país del cliente: "))
            # Validar números,letras espacios y carácteres especiales
            if not re.match(r"^([A-Za-záéíóúñü]{2,}(?:\s?[A-Za-záéíóúñü]{2,})*)$",pais):
                print("El país se indica con primera en mayuscula .")
                continue
            # NO NESECITA VALIDAR
            # response = requests.get(f"http://10.0.2.15:5001/clientes/{pais}")
            # if response.status_code == 200:
            #     print("El dato de pais del cliente ya existe.")
            #     continue
            break




    while True:
            # actualizar el codigo postal sin que se repita con alguno ya existente
            codigo_postal = (input("Ingresa un nuevo código postal del cliente (5 números 00000): "))
            # Validar números,letras espacios y carácteres especiales
            if not re.match(r"^[0-9]{5}$",codigo_postal):
                print("El código postal se indica con  .")
                continue
            # NO NESECITA VALIDAR
            # response = requests.get(f"http://10.0.2.15:5001/clientes/{region}")
            # if response.status_code == 200:
            #     print("El dato de pais del cliente ya existe.")
            #     continue
            break
    


    while True:
            # actualizar el codigo del empleado sin que se repita con alguno ya existente
            codigo_empleado_rep_ventas = (input("Ingresa un nuevo codigo del empleado del cliente: "))
            # Validar números,letras espacios y carácteres especiales
            if not re.match(r"^[0-9]+$",codigo_empleado_rep_ventas):
                print("El codigo del empleadol se indica con un número.")
                continue
            # NO NESECITA VALIDAR
            # response = requests.get(f"http://10.0.2.15:5001/clientes/{codigo_empleado_rep_ventas}")
            # if response.status_code == 200:
            #     print("El dato de codigo del empleado del cliente ya existe.")
            #     continue
            break



    while True:
            # actualizar el limite_credito del empleado sin que se repita con alguno ya existente
            limite_credito = (input("Ingresa un nuevo limite de crédito del cliente: "))
            # Validar números float
            if not re.match(r"^[0-9]+$",limite_credito):
                print("El limite crédito se indica con un número.")
                continue
            # NO NESECITA VALIDAR
            # response = requests.get(f"http://10.0.2.15:5001/clientes/{limite_credito}")
            # if response.status_code == 200:
            #     print("El dato de codigo del empleado del cliente ya existe.")
            #     continue
            break





    while True:
         # actualizar el codigo del cliente sin que se repita con alguno ya existente
        idNueva = (input("Ingresa el nuevo id del cliente(1,2,...): "))

        # Validar solo números
        if not re.match(r"^[0-9]+$", id):
            print("El id del cliente debe ser un número entero positivo.")
            continue
        # Validar si el código ya existe
        response = requests.get(f"http://10.0.2.15:5001/clientes/{idNueva}")
        if response.status_code == 200:
            print("El id del cliente ya existe.")
            continue

        break




    # PRIMERO ponemos todo el listado de información de nuestra lista
    cliente = {
        "codigo_cliente":int(codigo_cliente),
        "nombre_cliente":(nombre_cliente),
        "nombre_contacto":(nombre_contacto),
        "apellido_contacto":(apellido_contacto),
        "telefono":(telefono),
        "fax":(fax),
        "linea_direccion1":(linea_direccion1),
        "linea_direccion2":(linea_direccion2),
        "ciudad":(ciudad),
        "region":(region),
        "pais":(pais),
        "codigo_postal":(codigo_postal),
        "codigo_empleado_rep_ventas":int(codigo_empleado_rep_ventas),
        "limite_credito":float(limite_credito),
        "id":int(idNueva)
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
            8.  Actualizar país
            9.  Actualizar código postal
            10. Actualizar codigo del representante de ventas
            11. Actualizar límite de crédito
            12. Actualizar id del cliente
                
            13. Actualizar todos los datos anteriores
                        
            0. Atras          
            
                
                """)
            
            opcion=input("\nEscribe el número de una de las opciones: ")
            if(re.match(r'[0-9]+$',opcion)is not None):
                    opcion= int(opcion)
                    if opcion>=0 and opcion<=13:    



                        if opcion == 1:
                            id=input("Ingrese la id del cliente que desea actualizar: ")
                            print(tabulate(actualizarCodigoDelCliente(id),headers="keys",tablefmt="grid"))

                        if opcion == 2:
                            id=input("Ingrese la id del cliente que desea actualizar: ")
                            print(tabulate(actualizarNombreDelCliente(id),headers="keys",tablefmt="grid"))

                        if opcion == 3:
                            id=input("Ingrese la id del cliente que desea actualizar: ")
                            print(tabulate(actualizarNombreDelContacto(id),headers="keys",tablefmt="grid"))

                        if opcion == 4:
                            id=input("Ingrese la id del cliente que desea actualizar: ")
                            print(tabulate(actualizarTelefonoDelContacto(id),headers="keys",tablefmt="grid"))

                        if opcion == 5:
                            id=input("Ingrese la id del cliente que desea actualizar: ")
                            print(tabulate(actualizarDirecciones1Y2DelContacto(id),headers="keys",tablefmt="grid"))

                        if opcion == 6:
                            id=input("Ingrese la id del cliente que desea actualizar: ")
                            print(tabulate(actualizarCiudadDelContacto(id),headers="keys",tablefmt="grid"))  
                            
                        if opcion == 7:
                            id=input("Ingrese la id del cliente que desea actualizar: ")
                            print(tabulate(actualizarRegionDelContacto(id),headers="keys",tablefmt="grid"))    

                        if opcion == 8:
                            id=input("Ingrese la id del cliente que desea actualizar: ")
                            print(tabulate(actualizarPaisContacto(id),headers="keys",tablefmt="grid"))    

                        if opcion == 9:
                            id=input("Ingrese la id del cliente que desea actualizar: ")
                            print(tabulate(actualizarCodigoPostalContacto(id),headers="keys",tablefmt="grid"))    

                        if opcion == 10:
                            id=input("Ingrese la id del cliente que desea actualizar: ")
                            print(tabulate(actualizarRepresentanteContacto(id),headers="keys",tablefmt="grid"))                                                                                                                                            

                        if opcion == 11:
                            id=input("Ingrese la id del cliente que desea actualizar: ")
                            print(tabulate(actualizarLimiteCreditoContacto(id),headers="keys",tablefmt="grid"))
                   
                        if opcion == 12:
                            id=input("Ingrese la id del cliente que desea actualizar: ")
                            print(tabulate(actualizaridContacto(id),headers="keys",tablefmt="grid"))

                        if opcion == 13:
                            id=input("Ingrese la id del cliente que desea actualizar: ")
                            print(tabulate(actualizarTodoUnDatoCliente(id),headers="keys",tablefmt="grid"))

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









        
    





























































































