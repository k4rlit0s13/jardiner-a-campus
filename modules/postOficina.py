import json
import requests
from tabulate import tabulate
import re
import modules.getOficina as getOf





# agregar datos en oficina

# def agregarDatosOficina():
#     oficina = {
#     "codigo_oficina": input("Ingrese el codigo de la oficina: "),
#     "ciudad": input("Ingrese la ciudad de la oficina: "),
#     "pais": input("Ingrese el país de la oficina: "),
#     "region": input("Ingrese la región de la oficina: "),
#     "codigo_postal": input("Ingrese el código postal de la oficina: "),
#     "telefono": input("Ingrese el teléfono de la oficina: "),
#     "linea_direccion1": int(input("Ingrese la dirección 1 de la oficina: ")),
#     "linea_direccion2": int(input("Ingrese la dirección 2 de la oficina: "))
# }
#     headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
#     peticion = requests.post("http://10.0.2.15:5002",headers=headers, data=json.dumps(oficina, indent=4).encode("UTF-8"))
#     res = peticion.json()
#     res["Mensaje"] = "Producto Guardado"
#     return [res]


def FuncionDeConeccionOficinaJson():
      peticion=requests.get("http://10.0.2.15:5002/oficinas") 
      Informacion=peticion.json()  
      return Informacion        

#obtener un codigo de la lista directo(optimizado)
def getAllcode(id):
       peticion=requests.get(f"http://10.0.2.15:5002/oficinas/{id}")
       return[peticion.json()] if peticion.ok else []



# DELETE DATOS
def deletearProduct(id):

    data=getOf.getAllcode(code)

    if(len(data)):  
        peticion=requests.delete(f"http://10.0.2.15:5002/oficinas/{id}")
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
    
# AGREGAR DATOS OFICINAS
def agregarDatosoficina():
    oficinas={}
    while True:
        try:
            # expresion regular que tenga en cuenta escribir un numero solamente
            if not oficinas.get("codigo_oficina"):
                codigoOficina=input("Ingresa el código de la oficina(AAA-AAA): ")
                if(re.match(r'^[A-Z]+-[A-Z]+$',codigoOficina)is not None):
                    Data=getOf.getCodeOfficeCode(codigoOficina)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("El código de la oficina ya es existente")
                        #break #solo para el ultimo modulo sino se rompe
                    else:
                        oficinas["codigo_oficina"]=codigoOficina
                        print("El dato cumple con el estandar,OK")

                else:
                    raise Exception("El dato no cumple con el estandar establecido")


            # expresion regular que tenga en cuenta una palabra con mayuscula al principio,o  que pueda ser toda mayuscula, o que pueda tener un guion, que puedan ser varias palabras, que pueda tener numeros ni caracteres especiales
            if not oficinas.get("ciudad"):
                ciudad =input("Ingresa la ciudad de la oficina: ")
                if(re.match(r'^([A-ZÁÉÍÓÚÜ][a-záéíóúü]*-?)+[A-ZÁÉÍÓÚÜ]?[a-záéíóúü]*$',ciudad)is not None):
                    oficinas["ciudad"]=ciudad
                    print("El dato cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")



            if not oficinas.get("pais"):
                pais =input("Ingresa el país de la oficina: ")
                if(re.match(r'^([A-ZÁÉÍÓÚÜ][a-záéíóúü]*-?)+[A-ZÁÉÍÓÚÜ]?[a-záéíóúü]*$',pais)is not None):
                    oficinas["pais"]=pais
                    print("El dato cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")



            if not oficinas.get("region"):
                region =input("Ingresa la región de la oficina: ")
                if(re.match(r'^([A-ZÁÉÍÓÚÜ][a-záéíóúü]*-?)+[A-ZÁÉÍÓÚÜ]?[a-záéíóúü]*$',region)is not None):
                    oficinas["region"]=region
                    print("El dato cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")



            #expresion regular que tenga en cuenta la escritura de numeros solamente, o que escriba unas letras(obligatorio en mayuscula) junto con numeros separados por un espacio, o que pueda ser un numero seguido de un guión y luego más numeros todo pegado
            if not oficinas.get("codigo_postal"):
                codigoPostal =input("Ingresa el código postal de la oficina: ")
                if(re.match(r'^(\d+|[A-Z]+\s\d+|\d+-\d+)$',codigoPostal)is not None):
                    oficinas["codigo_postal"]=codigoPostal
                    print("El dato cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecido")


            # expresion que tenga en cuenta la escritura de un telefono de oficina, debe ser 11 numeros en total pueden llevar espacios, es obligatorio que tenga un  +de primero, un numero pegado y un espacio, separado del resto de numeros
            if not oficinas.get("telefono"):
                telefono=input("Ingresa el teléfono de la oficina(+00 000 0000 000): ")
                if(re.match(r'^\+\d{1,2} \d{1,3} \d{1,4} \d{1,4}$',telefono)is not None):
                    Data=getOf.getTelFromTel(telefono)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("El telefono de la oficina ya existe")
                        #break #solo para el ultimo modulo sino se rompe
                    else:
                        oficinas["telefono"]=telefono
                        print("El dato cumple con el estandar,OK")

                else:
                    raise Exception("El dato no cumple con el estandar establecido")




            # expresion que tenga en cuenta la escritura de una direccion 
            if not oficinas.get("linea_direccion1"):
                direcion1=input("Ingresa la primera direccion de la oficina: ")
                if(re.match(r'\w+',direcion1)is not None):
                    Data=getOf.getDireccion1FromDireccion(direcion1)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("la dirección de la oficina ya existe")
                        #break #solo para el ultimo modulo sino se rompe
                    else:
                        oficinas["linea_direccion1"]=direcion1
                        print("El dato cumple con el estandar,OK")

                else:
                    raise Exception("El dato no cumple con el estandar establecido")
                


            if not oficinas.get("linea_direccion2"):
                direccion2=input("Ingresa la segunda direccion de la oficina: ")
                if(re.match(r'\w+',direccion2)is not None):
                    Data=getOf.getDireccion2FromDireccion(direccion2)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("La dirección de la oficina ya existe")
                        #break #solo para el ultimo modulo sino se rompe
                    else:
                        oficinas["linea_direccion2"]=direccion2
                        print("El dato cumple con el estandar,OK")

                else:
                    raise Exception("El dato no cumple con el estandar establecido")


        except Exception as error:
            print(error)
   

        headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
        peticion = requests.post("http://10.0.2.15:5002/oficinas/",headers=headers, data=json.dumps(oficinas, indent=4).encode("UTF-8"))
        res = peticion.json()
        res["Mensaje"] = "Producto Guardado"
        return [res]

# UPDATE DATOS
def actualizarTodoUnDatoOficina(id):

    while True:
        # SEGUNDO hacemos las OPERACIONES para cada una de las actualizaciones que queremos hacer:

         # actualizar el codigo del cliente sin que se repita con alguno ya existente
        codigo_oficina = (input("Ingresa el nuevo código de la oficina(ejemplo:AAA-AAA): "))

        # Validar solo números
        if not re.match(r"^([A-Z]{3})-([A-Z]+)$", codigo_oficina):
            print("El código de la oficina no es valido.")
            continue
        # Validar si el código ya existe
        response = requests.get(f"http://10.0.2.15:5002/oficinas/{codigo_oficina}")
        if response.status_code == 200:
            print("El código de oficina ya existe.")
            continue

        break


    while True:
            # actualizar la ciudad del cliente sin que se repita con alguno ya existente
            ciudad = (input("Ingresa una nueva ciudad de la oficina: "))
            # Validar números,letras espacios y carácteres especiales
            if not re.match(r"^([A-Za-záéíóúñü]{2,}(?:\s?[A-Za-záéíóúñü]{2,})*)$",ciudad):
                print("La ciudad se indica con primera en mayuscula .")
                continue
            # NO NESECITA VALIDAR
            # response = requests.get(f"http://10.0.2.15:5002/oficinas{ciudad}")
            # if response.status_code == 200:
            #     print("El dato de la ciudad del cliente ya existe.")
            #     continue
            break
    

    while True:
        # actualizar el pais del cliente sin que se repita con alguno ya existente
        pais = (input("Ingresa un nuevo país de la oficina: "))
        # Validar números,letras espacios y carácteres especiales
        if not re.match(r"^([A-Za-záéíóúñü]{2,}(?:\s?[A-Za-záéíóúñü]{2,})*)$",pais):
            print("El país se indica con primera en mayuscula .")
            continue
        # NO NESECITA VALIDAR
        # response = requests.get(f"http://10.0.2.15:5002/oficinas{pais}")
        # if response.status_code == 200:
        #     print("El dato de pais del cliente ya existe.")
        #     continue
        break


    while True:
        # actualizar la region del cliente sin que se repita con alguno ya existente
        region = (input("Ingresa una nueva región de la oficina: "))
        # Validar números,letras espacios y carácteres especiales
        if not re.match(r"^([A-Za-záéíóúñü]{2,}(?:\s?[A-Za-záéíóúñü]{2,})*)$",region):
            print("La región se indica con primera en mayuscula .")
            continue
        # NO NESECITA VALIDAR
        # response = requests.get(f"http://10.0.2.15:5002/oficinas{region}")
        # if response.status_code == 200:
        #     print("El dato de region del cliente ya existe.")
        #     continue
        break


    while True:
        # actualizar el codigo postal sin que se repita con alguno ya existente
        codigo_postal = (input("Ingresa un nuevo código postal de la oficina (5 números 00000): "))
        # Validar números,letras espacios y carácteres especiales
        if not re.match(r"^[0-9]{5}$",codigo_postal):
            print("El código postal no es válido .")
            continue
        # NO NESECITA VALIDAR
        # response = requests.get(f"http://10.0.2.15:5002/oficinas{region}")
        # if response.status_code == 200:
        #     print("El dato de pais del cliente ya existe.")
        #     continue
        break
       

    while True:
         # actualizar el teléfono del cliente sin que se repita con alguno ya existente
        telefono = (input("Ingresa el nuevo teléfono dela oficina(11 dijitos 00000000000): "))
        # Validar solo 11 números
        if not re.match(r"^[0-9]{11}$", telefono):
            print("El teléfono del cliente se construye de 11 dígitos 00000000000.")
            continue
        # Validar si el telefono ya existe
        response = requests.get(f"http://10.0.2.15:5002/oficinas/{telefono}")
        if response.status_code == 200:
            print("El teléfono del cliente ya existe.")
            continue
        break


    while True:
            # actualizar la linea_direccion1 del cliente sin que se repita con alguno ya existente
            linea_direccion1 = (input("Ingresa la nueva dirección de la oficina: "))
            # Validar números,letras espacios y carácteres especiales
            if not re.match(r"^[\x00-\xFF]+$",linea_direccion1):
                print("La dirección del cliente se construye por números,letras y carácteres especiales como el /.")
                continue
            # Validar si la direccion ya existe
            response = requests.get(f"http://10.0.2.15:5002/oficinas/{linea_direccion1}")
            if response.status_code == 200:
                print("La dirección del cliente ya existe.")
                continue
            break


    while True:
            # actualizar la linea_direccion2 del cliente sin que se repita con alguno ya existente
            linea_direccion2 = (input("Ingresa una nueva indicacion a la direccion de la oficina: "))
            # Validar números,letras espacios y carácteres especiales
            if not re.match(r"^[\x00-\xFF]+$",linea_direccion2):
                print("La dirección del cliente se construye por números,letras y carácteres especiales como el /.")
                continue
            # Validar si la direccion2 ya existe
            response = requests.get(f"http://10.0.2.15:5002/oficinas/{linea_direccion2}")
            if response.status_code == 200:
                print("El dato de la dirección del cliente ya existe.")
                continue
            break
    

    # PRIMERO ponemos todo el listado de información de nuestra lista
    cliente = {
        "codigo_oficina":str(codigo_oficina),
        "ciudad":str(ciudad),
        "region":str(region),
        "pais":str(pais),
        "codigo_postal":str(codigo_postal),
        "telefono":str(telefono),
        "linea_direccion1":str(linea_direccion1),
        "linea_direccion2":str(linea_direccion2)
        }


    clienteExistente=getAllcode(id)
    if not clienteExistente:
        return{"message":"Cliente no encontrado"}
    
    clienteActualizado= {**clienteExistente[0],**cliente}
    peticion=requests.put(f"http://10.0.2.15:5002/oficinas/{id}",data=json.dumps(clienteActualizado))
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
                                                                                               
██████╗  █████╗ ████████╗ ██████╗ ███████╗     ██████╗ ███████╗██╗ ██████╗██╗███╗   ██╗ █████╗ 
██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝    ██╔═══██╗██╔════╝██║██╔════╝██║████╗  ██║██╔══██╗
██║  ██║███████║   ██║   ██║   ██║███████╗    ██║   ██║█████╗  ██║██║     ██║██╔██╗ ██║███████║
██║  ██║██╔══██║   ██║   ██║   ██║╚════██║    ██║   ██║██╔══╝  ██║██║     ██║██║╚██╗██║██╔══██║
██████╔╝██║  ██║   ██║   ╚██████╔╝███████║    ╚██████╔╝██║     ██║╚██████╗██║██║ ╚████║██║  ██║
╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝     ╚═════╝ ╚═╝     ╚═╝ ╚═════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
                                                                                               
                                                                                        

        1. Actualizar codigo oficina      
        2. Actualizar ciudad   
        3. Actualizar pais  
        4. Actualizar region
        5. Actualizar codigo postal
        6. Actualizar telefono
        7. Actualizar direcciones

        8. Actualizar todas      
                                   
        0. Atras                                                                                                           
          
          
          
        

        """)
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=8:   
                           
                   
                    if opcion == 1:
                        id=input("Ingrese la id del cliente que desea actualizar: ")
                        print(tabulate((id),headers="keys",tablefmt="grid"))

                    if opcion == 2:
                        id=input("Ingrese la id del cliente que desea actualizar: ")
                        print(tabulate((id),headers="keys",tablefmt="grid"))

                    if opcion == 3:
                        id=input("Ingrese la id del cliente que desea actualizar: ")
                        print(tabulate((id),headers="keys",tablefmt="grid"))                     
                    
                    if opcion == 4:
                        id=input("Ingrese la id del cliente que desea actualizar: ")
                        print(tabulate((id),headers="keys",tablefmt="grid"))                   
                    
                    if opcion == 5:
                        id=input("Ingrese la id del cliente que desea actualizar: ")
                        print(tabulate((id),headers="keys",tablefmt="grid")) 

                    if opcion == 6:
                        id=input("Ingrese la id del cliente que desea actualizar: ")
                        print(tabulate((id),headers="keys",tablefmt="grid")) 

                    if opcion == 7:
                        id=input("Ingrese la id del cliente que desea actualizar: ")
                        print(tabulate((id),headers="keys",tablefmt="grid")) 

                    if opcion == 8:
                        id=input("Ingrese la id de la ofificna que desea actualizar: ")
                        print(tabulate(actualizarTodoUnDatoOficina(id),headers="keys",tablefmt="grid"))                    
                    
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
                                                                                    
██████╗  █████╗ ████████╗ ██████╗ ███████╗    ██████╗ ███████╗    ██╗      █████╗   
██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝    ██╔══██╗██╔════╝    ██║     ██╔══██╗  
██║  ██║███████║   ██║   ██║   ██║███████╗    ██║  ██║█████╗      ██║     ███████║  
██║  ██║██╔══██║   ██║   ██║   ██║╚════██║    ██║  ██║██╔══╝      ██║     ██╔══██║  
██████╔╝██║  ██║   ██║   ╚██████╔╝███████║    ██████╔╝███████╗    ███████╗██║  ██║  
╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝    ╚═════╝ ╚══════╝    ╚══════╝╚═╝  ╚═╝  
                                                                                    
 ██████╗ ███████╗██╗ ██████╗██╗███╗   ██╗ █████╗                                    
██╔═══██╗██╔════╝██║██╔════╝██║████╗  ██║██╔══██╗                                   
██║   ██║█████╗  ██║██║     ██║██╔██╗ ██║███████║                                   
██║   ██║██╔══╝  ██║██║     ██║██║╚██╗██║██╔══██║                                   
╚██████╔╝██║     ██║╚██████╗██║██║ ╚████║██║  ██║                                   
 ╚═════╝ ╚═╝     ╚═╝ ╚═════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝                                   
                                                                                             

        1. Guardar nuevo dato de oficina
        2. Borrar un dato 
        3. Actualizar datos oficina
                          
        0. Atras       




        """)
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=3:  
                             
                    if(opcion==1):
                        print(tabulate(agregarDatosoficina(), headers="keys",tablefmt="grid"))
                    if(opcion==2):
                        idProducto=input("Ingrese el id del producto que desea eliminar: ")
                        print(tabulate(deletearProduct(idProducto)["body"],headers="keys",tablefmt="grid"))                        
                    if(opcion==3):
                        actualizarPagos()              
                    if(opcion==0):
                        break