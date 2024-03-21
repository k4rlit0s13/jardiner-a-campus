import json
import requests
from tabulate import tabulate
import re
import modules.getEmpleados as getEm



# def agregarDatosempleados():
#     empleados = {
#     "codigo_empleados": int(input("Ingrese el código del empleados: ")),
#     "nombre": input("Ingrese el nombre del empleados: "),
#     "apellido1":input("Ingrese el primer apellido del empleados: "),
#     "apellido2":input("Ingrese el segundo apellido del empleados: "),
#     "extension":input("Ingrese la extensión del empleados: "),
#     "email": input("Ingrese el email del empleados: "),
#     "codigo_oficina": input("Ingrese el codigo de la oficina del empleados: "),
#     "codigo_jefe": int(input("Ingrese el código del jefe del empleados: ")),
#     "puesto": input("Ingrese el puesto del empleados: "),


# }
#     headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
#     peticion = requests.post("http://10.0.2.15:5003",headers=headers, data=json.dumps(empleados, indent=4).encode("UTF-8"))
#     res = peticion.json()
#     res["Mensaje"] = "Producto Guardado"
#     return [res]



def FuncionDeConeccionempleadosJson():
      peticion=requests.get("http://10.0.2.15:5003/empleados") 
      Informacion=peticion.json()  
      return Informacion    



# DELETE DATOS
def deletearProduct(id):

    data=getEm.getAllcode(id)

    if(len(data)):  
        peticion=requests.delete(f"http://10.0.2.15:5003/empleados/{id}")
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
    
# POST DATOS
def agregarDatosempleados():
    empleados={}
    while True:
        try:


            # # expresion regulat que tenga en cuenta escribir un numero solamente

            if not empleados.get("codigo_cliente"):
                codigo=input("Ingresa el codigo del empleados: ")
                if (re.match(r'^\d+$',codigo)is not None):
                    codigo= int(codigo)
                    Data=getEm.getempleadosFormempleados(codigo)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("El código ya existe")
                    # break # el break se deja solo para el ultimo modulo sino se rompe toda la cadena
                else:
                    empleados["codigo_cliente"]=codigo
                    print("El dato cumple con el estandar, OK")






            # # expresion regular que tenga en cuenta la escritura de palabras para parrafos

            if not empleados.get("nombre"):
                nombre=input("Ingresa un nombre del empleados: ")
                if(re.match(r'\w+',nombre)is not None):
                    empleados["nombre"]=nombre
                    print("El dato cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                


            # expresion regular que tenga en cuenta la escritura de una palabra con la primera en mayuscula y el resto en minuscula

            if not empleados.get("apellido1"):
                apellido1 =input("Ingresa el primer apellido del empleados(ejemplo: Alberto): ")
                if(re.match(r'^[A-ZÁÉÍÓÚÜÑ][a-záéíóúüñ]*$',apellido1)is not None):
                    empleados["apellido1"]=apellido1
                    print("El dato cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
            else:
                raise Exception("El dato no cumple con el estandar establecido")      





            if not empleados.get("apellido2"):
                apellido2 =input("Ingresa el segundo apellido del empleados(ejemplo: Suarez): ")
                if(re.match(r'^[A-ZÁÉÍÓÚÜÑ][a-záéíóúüñ]*$',apellido2)is not None):
                    empleados["apellido2"]=apellido2
                    print("El dato cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
            else:
                raise Exception("El dato no cumple con el estandar establecido")      





            # # expresion regular que tenga en cuenta la escritura de un numero 
            if not empleados.get("extension"):
                extension =input("Ingresa la extension del empleado(0000): ")
                if(re.match(r'^\d{4}$',extension)is not None):
                    empleados["extension"]=extension
                    print("El dato cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")


            # expresion regular que tenga en cuenta la escritura 3 mayusculas un guion y 3 mayusculas
                
            if not empleados.get("email"):
                email=input("Ingresa el email del empleado: ")
                if(re.match(r'^[\s\S]*$',email)is not None):
                    Data=getEm.getEmailFromEmail(email)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("El email de la oficina ya existe")
                        #break #solo para el ultimo modulo sino se rompe
                    else:
                        empleados["email"]=email
                        print("El dato cumple con el estandar,OK")

                else:
                    raise Exception("El dato no cumple con el estandar establecido")



            # expresion regulat que tenga en cuenta escribir un numero solamente
            if not empleados.get("codigo_oficina"):
                oficina =input("Ingresa el código de la oficina(AAA-AAA): ")
                if(re.match(r'^[A-Z]+-[A-Z]+$',oficina)is not None):
                    empleados["codigo_oficina"]=oficina
                    print("El dato cumple con el estandar,OK")
                    # break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")



            # expresion regular que tenga en cuenta la escritura de un numero 
            if not empleados.get("codigo_jefe"):
                jefe =input("Ingresa el código del jefe del empleado: ")
                if(re.match(r'^\d+$',jefe)is not None):
                    empleados["codigo_jefe"]=jefe
                    print("El dato cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")



            if not empleados.get("puesto"):
                puesto=input("Ingresa el puesto del empleado(ejemplo: Representante Ventas): ")
                if(re.match(r'^[A-Z][a-z]*( [A-Z][a-z]*)*$',puesto)is not None):
                    print(tabulate(Data, headers="keys",tablefmt="grid"))
                    empleados["puesto"]=puesto
                    print("El dato cumple con el estandar,OK")
                break #solo para el ultimo modulo sino se rompe
            else:
                raise Exception("El dato no cumple con el estandar establecido")



        except Exception as error:
            print(error)


    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://10.0.2.15:5003/empleados",headers=headers, data=json.dumps(empleados, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]


# UPDATE DATOS

def actualizarTodoUnDatoempleados(id):

    while True:
        # SEGUNDO hacemos las OPERACIONES para cada una de las actualizaciones que queremos hacer:

         # actualizar el codigo del cliente sin que se repita con alguno ya existente
        codigo_empleado = (input("Ingresa el nuevo código del empleado: "))

        # Validar solo números
        if not re.match(r"^[0-9]+$", codigo_empleado):
            print("El código del empleado debe ser un número entero positivo.")
            continue
        # Validar si el código ya existe
        response = requests.get(f"http://10.0.2.15:5003/empleados/{codigo_empleado}")
        if response.status_code == 200:
            print("El código del cliente ya existe.")
            continue

        break



    # actualizar el nombre del cliente sin que se repita con alguno ya existente
    while True:
        # actualizar el nombre del cliente/empresa
        nombre = (input("Ingrese el nuevo nombre de la empresa: "))

        # Validar nombre
        if not re.match(r"^([A-ZÁÉÍÓÚÑÜa-záéíóúñü]+[ _-]?)+$", nombre):
            print("El nombre del cliente no es válido.")
            continue
        #  # NO SE ASIMILA
        # response = requests.get(f"http://10.0.2.15:5003/empleados/{nombre}")
        # if response.status_code == 200:
        #     print("El código del cliente ya existe.")
        #     continue

        break


    # actualizar el nombre del contacto y se puede repetir
    while True:
        # actualizar el apellido1
        apellido1=(input("Ingrese el nuevo primer apellido del empleado: "))

        # Validar apellido1
        if not re.match(r"^([A-ZÁÉÍÓÚÑÜa-záéíóúñü]+[ _-]?)+$", apellido1):
            print("El nombre del contacto no es válido.")
            continue
        #  # NO ES NECESARIO VALIDAR
        # response = requests.get(f"http://10.0.2.15:5003/empleados/{nombre_contacto}")
        # if response.status_code == 200:
        #     print("El código del cliente ya existe.")
        #     continue
        break



    # actualizar el apellido del contacto y se puede repetir
    while True:
        # actualizar el apellido2
        apellido2=(input("Ingrese el nuevo segundo apellido del empleado: "))

        # Validar apellido2
        if not re.match(r"^([A-ZÁÉÍÓÚÑÜa-záéíóúñü]+[ _-]?)+$", apellido2):
            print("El nombre del contacto no es válido.")
            continue
        #  # NO ES NECESARIO VALIDAR
        # response = requests.get(f"http://10.0.2.15:5003/empleados/{apellido_contacto}")
        # if response.status_code == 200:
        #     print("El código del cliente ya existe.")
        #     continue
        break




    while True:
         # actualizar el extension sin que se repita con alguno ya existente
        extension = (input("Ingresa la extension(0000) "))
        # Validar extension
        if not re.match(r"^[0-9]{4}$", extension):
            print("La extension son 4 dígitos 0000.")
            continue
        # Validar si el extension ya existe
        response = requests.get(f"http://10.0.2.15:5003/empleados/{extension}")
        if response.status_code == 200:
            print("La extension ya existe.")
            continue
        break




    while True:
         # actualizar el fax del cliente sin que se repita con alguno ya existente
        email = (input("Ingresa el nuevo email: "))
        # Validar solo 11 números
        if not re.match(r".+",email):
            print("El email es incorrecto.")
            continue
        # Validar si el fax ya existe
        response = requests.get(f"http://10.0.2.15:5003/empleados/{email}")
        if response.status_code == 200:
            print("El fax del cliente ya existe.")
            continue
        break



    while True:
            # actualizar la linea_direccion1 del cliente sin que se repita con alguno ya existente
            codigo_oficina = (input("Ingresa la nueva dirección del cliente: "))
            # Validar números,letras espacios y carácteres especiales
            if not re.match(r"^[A-Z]{3}-[A-Z]{3}$",codigo_oficina):
                print("La dirección del cliente se construye por números,letras y carácteres especiales como el /.")
                continue
            # Validar si la direccion ya existe
            response = requests.get(f"http://10.0.2.15:5003/empleados/{codigo_oficina}")
            if response.status_code == 200:
                print("La dirección del cliente ya existe.")
                continue
            break




    while True:
            # actualizar la linea_direccion2 del cliente sin que se repita con alguno ya existente
            codigo_jefe = (input("Ingresa una nueva indicacion a la direccion del cliente: "))
            # Validar números,letras espacios y carácteres especiales
            if not re.match(r"^[0-9]+$",codigo_jefe):
                print("El código se construye por un número.")
                continue
            # Validar si la direccion2 ya existe
            response = requests.get(f"http://10.0.2.15:5003/empleados/{codigo_jefe}")
            if response.status_code == 200:
                print("El dato de código ya existe.")
                continue
            break


      
    while True:
            # actualizar la ciudad del cliente sin que se repita con alguno ya existente
            puesto = (input("Ingresa una nueva puesto del empleado: "))
            # Validar números,letras espacios y carácteres especiales
            if not re.match(r"^[A-Z][a-zA-Z]*$",puesto):
                print("El puesto que indica no cumple.")
                continue
            # NO NESECITA VALIDAR
            # response = requests.get(f"http://10.0.2.15:5003/empleados/{ciudad}")
            # if response.status_code == 200:
            #     print("El dato de la ciudad del cliente ya existe.")
            #     continue
            break
    


    while True:
         # actualizar el codigo del cliente sin que se repita con alguno ya existente
        idNueva = (input("Ingresa el nuevo id del cliente(1,2,...): "))

        # Validar solo números
        if not re.match(r"^[0-9]+$", idNueva):
            print("El id del cliente debe ser un número entero positivo.")
            continue
        # Validar si el código ya existe
        response = requests.get(f"http://10.0.2.15:5003/empleados/{idNueva}")
        if response.status_code == 200:
            print("El id del cliente ya existe.")
            continue

        break




    # PRIMERO ponemos todo el listado de información de nuestra lista
    cliente = {
        "codigo_empleado":int(codigo_empleado),
        "nombre":(nombre),
        "apellido1":(apellido1),
        "apellido2":(apellido2),
        "extension":(extension),
        "email":(email),
        "codigo_oficina":(codigo_oficina),
        "codigo_jefe":int(codigo_jefe),
        "puesto":(puesto),
        "id":int(idNueva)
        }


    clienteExistente=FuncionDeConeccionempleadosJson(id)
    if not clienteExistente:
        return{"message":"Cliente no encontrado"}
    
    clienteActualizado= {**clienteExistente[0],**cliente}
    peticion=requests.put(f"http://10.0.2.15:5003/empleados/{id}",data=json.dumps(clienteActualizado))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]









def actualizarPostEpleador(id):
    while True:
        # SEGUNDO hacemos las OPERACIONES para cada una de las actualizaciones que queremos hacer:

        # actualizar el codigo del cliente sin que se repita con alguno ya existente
        codigo_empleado = (input("Ingresa el nuevo código del empleado: "))

        # Validar solo números
        if not re.match(r"^[0-9]+$", codigo_empleado):
            print("El código del empleado debe ser un número entero positivo.")
            continue
        # Validar si el código ya existe
        response = requests.get(f"http://10.0.2.15:5003/empleados/{codigo_empleado}")
        if response.status_code == 200:
            print("El código del cliente ya existe.")
            continue

        break



    cliente = {
            "codigo_empleado":int(codigo_empleado),
            }

    clienteExistente=FuncionDeConeccionempleadosJson(id)
    if not clienteExistente:
            return{"message":"Cliente no encontrado"}
        
    clienteActualizado= {**clienteExistente[0],**cliente}
    peticion=requests.put(f"http://10.0.2.15:5003/empleados/{id}",data=json.dumps(clienteActualizado))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]

def actualizaridNueva(id):

    while True:
         # actualizar el codigo del cliente sin que se repita con alguno ya existente
        idNueva = (input("Ingresa el nuevo id del cliente(1,2,...): "))

        # Validar solo números
        if not re.match(r"^[0-9]+$", idNueva):
            print("El id del cliente debe ser un número entero positivo.")
            continue
        # Validar si el código ya existe
        response = requests.get(f"http://10.0.2.15:5003/empleados/{idNueva}")
        if response.status_code == 200:
            print("El id del cliente ya existe.")
            continue

        break
    cliente = {
            "idNueva":int(idNueva),
            }

    clienteExistente=FuncionDeConeccionempleadosJson(id)
    if not clienteExistente:
            return{"message":"Cliente no encontrado"}
        
    clienteActualizado= {**clienteExistente[0],**cliente}
    peticion=requests.put(f"http://10.0.2.15:5003/empleados/{id}",data=json.dumps(clienteActualizado))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]








































def actualizarPagos():
    while True:
        print("""
 █████╗  ██████╗████████╗██╗   ██╗ █████╗ ██╗     ██╗███████╗ █████╗ ██████╗     
██╔══██╗██╔════╝╚══██╔══╝██║   ██║██╔══██╗██║     ██║╚══███╔╝██╔══██╗██╔══██╗    
███████║██║        ██║   ██║   ██║███████║██║     ██║  ███╔╝ ███████║██████╔╝    
██╔══██║██║        ██║   ██║   ██║██╔══██║██║     ██║ ███╔╝  ██╔══██║██╔══██╗    
██║  ██║╚██████╗   ██║   ╚██████╔╝██║  ██║███████╗██║███████╗██║  ██║██║  ██║    
╚═╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    
                                                                                 
███████╗███╗   ███╗██████╗ ██╗     ███████╗ █████╗ ██████╗  ██████╗ ███████╗     
██╔════╝████╗ ████║██╔══██╗██║     ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔════╝     
█████╗  ██╔████╔██║██████╔╝██║     █████╗  ███████║██║  ██║██║   ██║███████╗     
██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  ██╔══██║██║  ██║██║   ██║╚════██║     
███████╗██║ ╚═╝ ██║██║     ███████╗███████╗██║  ██║██████╔╝╚██████╔╝███████║     
╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝     
                                                                                                                                                                    
                                                                                        
        1. Actualizar código empleado
        2. Actualizar nombre empleado
        3. Actualizar apellidos  
        4. Actualizar email
        5. Actualizar código oficina
        6. Actualizar código jefe
        7. Actualizar puesto 
        8. Actualizar id

        9. Actualizar todas las anteriores     
                                   
        0. Atras 
        

        """)
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=9:  

                    if opcion == 1:
                        id=input("Ingrese la id del cliente que desea actualizar: ")
                        print(tabulate(actualizarPostEpleador(id),headers="keys",tablefmt="grid"))

                    if opcion == 9:
                        id=input("Ingrese la id del cliente que desea actualizar: ")
                        print(tabulate(actualizarTodoUnDatoempleados(id),headers="keys",tablefmt="grid"))
                                        
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
                                                                                                                          
██████╗  █████╗ ████████╗ ██████╗ ███████╗    ███████╗███╗   ███╗██████╗ ██╗     ███████╗ █████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝    ██╔════╝████╗ ████║██╔══██╗██║     ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║  ██║███████║   ██║   ██║   ██║███████╗    █████╗  ██╔████╔██║██████╔╝██║     █████╗  ███████║██║  ██║██║   ██║███████╗
██║  ██║██╔══██║   ██║   ██║   ██║╚════██║    ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  ██╔══██║██║  ██║██║   ██║╚════██║
██████╔╝██║  ██║   ██║   ╚██████╔╝███████║    ███████╗██║ ╚═╝ ██║██║     ███████╗███████╗██║  ██║██████╔╝╚██████╔╝███████║
╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝    ╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝
                                                                                                                             
         
        1. Guardar un nuevo dato de empleados
        2. Eliminar un dato
                    
        0. Atras          
          
          
        """)
        
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=2:      
                                 
                    if(opcion==1):
                        print(tabulate(agregarDatosempleados(), headers="keys",tablefmt="grid"))
                    if(opcion==2):
                        idProducto=input("Ingrese el id del producto que desea eliminar: ")
                        print(tabulate(deletearProduct(idProducto)["body"],headers="keys",tablefmt="grid"))                        
                    if(opcion==0):
                        break
