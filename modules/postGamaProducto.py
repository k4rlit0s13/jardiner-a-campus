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


#obtener un codigo de la lista directo(optimizado)
def getAllcode(id):
       peticion=requests.get(f"http://10.0.2.15:5006/gama_productos/{'id'}")
       return[peticion.json()] if peticion.ok else []


# DELETE DATOS
def deletearProduct(code):

    data=getgama.getAllcode(code)

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
    


# POST DATOS 
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
    peticion = requests.post("http://10.0.2.15:5006/gama_productos",headers=headers, data=json.dumps(gamasProducto, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Dato Guardado"
    return [res]


# UPDATE DATOS
def actualizarTodosdatosGamaProductos(id):
    while True:
        # SEGUNDO hacemos las OPERACIONES para cada una de las actualizaciones que queremos hacer:

         # actualizar el codigo del cliente sin que se repita con alguno ya existente
        gama = (input("Ingresa nueva gama del producto: "))

        # Validar solo números
        if not re.match(r"^([A-ZÁÉÍÓÚÑÜ]{1}[a-záéíóúñü]*)$", gama):
            print("La gama es con primera en mayuscula y solo una palabra.")
            continue
        # Validar si el código ya existe
        response = requests.get(f"http://10.0.2.15:5006/gama_productos{gama}")
        if response.status_code == 200:
            print("gama ya existe.")
            continue

        break



    # actualizar el nombre del cliente sin que se repita con alguno ya existente
    while True:
        # actualizar el nombre del cliente/empresa
        descripcion_texto = (input("Ingrese la nueva descripcion del texto: "))

        # Validar nombre
        if not re.match(r"^([A-ZÁÉÍÓÚÑÜa-záéíóúñü]+[ _-]?)+$",descripcion_texto):
            print("la descripción es solo texto.")
            continue
        #  # NO SE ASIMILA
        # response = requests.get(f"http://10.0.2.15:5006/gama_productos{descripcion_texto}")
        # if response.status_code == 200:
        #     print("El código del cliente ya existe.")
        #     continue

        break

     # PRIMERO ponemos todo el listado de información de nuestra lista
    cliente = {
        "gama":str(gama),
        "descripcion_texto":str(descripcion_texto),}


    clienteExistente=getAllcode(id)
    if not clienteExistente:
        return{"message":"Cliente no encontrado"}
    
    clienteActualizado= {**clienteExistente[0],**cliente}
    peticion=requests.put(f"http://10.0.2.15:5006/gama_productos{id}",data=json.dumps(clienteActualizado))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]

def actualizarGama(id):
    while True:
        # SEGUNDO hacemos las OPERACIONES para cada una de las actualizaciones que queremos hacer:

         # actualizar el codigo del cliente sin que se repita con alguno ya existente
        gama = (input("Ingresa nueva gama del producto: "))

        # Validar solo números
        if not re.match(r"^([A-ZÁÉÍÓÚÑÜ]{1}[a-záéíóúñü]*)$", gama):
            print("La gama es con primera en mayuscula y solo una palabra.")
            continue
        # Validar si el código ya existe
        response = requests.get(f"http://10.0.2.15:5006/gama_productos{gama}")
        if response.status_code == 200:
            print("gama ya existe.")
            continue

        break


     # PRIMERO ponemos todo el listado de información de nuestra lista
    cliente = {
        "gama":str(gama),}


    clienteExistente=getAllcode(id)
    if not clienteExistente:
        return{"message":"Cliente no encontrado"}
    
    clienteActualizado= {**clienteExistente[0],**cliente}
    peticion=requests.put(f"http://10.0.2.15:5006/gama_productos{id}",data=json.dumps(clienteActualizado))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]

def actualizardescripcion(id):

    # actualizar el nombre del cliente sin que se repita con alguno ya existente
    while True:
        # actualizar el nombre del cliente/empresa
        descripcion_texto = (input("Ingrese la nueva descripcion del texto: "))

        # Validar nombre
        if not re.match(r"^([A-ZÁÉÍÓÚÑÜa-záéíóúñü]+[ _-]?)+$",descripcion_texto):
            print("la descripción es solo texto.")
            continue
        #  # NO SE ASIMILA
        # response = requests.get(f"http://10.0.2.15:5006/gama_productos{descripcion_texto}")
        # if response.status_code == 200:
        #     print("El código del cliente ya existe.")
        #     continue

        break

     # PRIMERO ponemos todo el listado de información de nuestra lista
    cliente = {
        "descripcion_texto":str(descripcion_texto),}


    clienteExistente=getAllcode(id)
    if not clienteExistente:
        return{"message":"Cliente no encontrado"}
    
    clienteActualizado= {**clienteExistente[0],**cliente}
    peticion=requests.put(f"http://10.0.2.15:5006/gama_productos{id}",data=json.dumps(clienteActualizado))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]




























def actualizarGamaProoductos():
    while True:
        print("""
 █████╗  ██████╗████████╗██╗   ██╗ █████╗ ██╗     ██╗███████╗ █████╗ ██████╗     
██╔══██╗██╔════╝╚══██╔══╝██║   ██║██╔══██╗██║     ██║╚══███╔╝██╔══██╗██╔══██╗    
███████║██║        ██║   ██║   ██║███████║██║     ██║  ███╔╝ ███████║██████╔╝    
██╔══██║██║        ██║   ██║   ██║██╔══██║██║     ██║ ███╔╝  ██╔══██║██╔══██╗    
██║  ██║╚██████╗   ██║   ╚██████╔╝██║  ██║███████╗██║███████╗██║  ██║██║  ██║    
╚═╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    
                                                                                 
 ██████╗  █████╗ ███╗   ███╗ █████╗     ██████╗ ███████╗                         
██╔════╝ ██╔══██╗████╗ ████║██╔══██╗    ██╔══██╗██╔════╝                         
██║  ███╗███████║██╔████╔██║███████║    ██║  ██║█████╗                           
██║   ██║██╔══██║██║╚██╔╝██║██╔══██║    ██║  ██║██╔══╝                           
╚██████╔╝██║  ██║██║ ╚═╝ ██║██║  ██║    ██████╔╝███████╗                         
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝                         
                                                                                 
██████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗ ██████╗ ██████╗██╗ ██████╗ ███╗   ██╗ 
██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║   ██║██╔════╝██╔════╝██║██╔═══██╗████╗  ██║ 
██████╔╝██████╔╝██║   ██║██║  ██║██║   ██║██║     ██║     ██║██║   ██║██╔██╗ ██║ 
██╔═══╝ ██╔══██╗██║   ██║██║  ██║██║   ██║██║     ██║     ██║██║   ██║██║╚██╗██║ 
██║     ██║  ██║╚██████╔╝██████╔╝╚██████╔╝╚██████╗╚██████╗██║╚██████╔╝██║ ╚████║ 
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝ 
                                                                                 
                                                                                        

        1. Actualizar gama
        2. Actualizar descripción   
              
        3. Actualizar ambos
                   
        0. Atras                                                                                                           
          
        
          
        

        """)
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=3:   
                           
                    if opcion == 1:
                        id=input("Ingrese la id del cliente que desea actualizar: ")
                        print(tabulate(actualizarGama(id),headers="keys",tablefmt="grid"))

                    if opcion == 2:
                        id=input("Ingrese la id del cliente que desea actualizar: ")
                        print(tabulate(actualizardescripcion(id),headers="keys",tablefmt="grid"))

                    if opcion == 3:
                        id=input("Ingrese la id del cliente que desea actualizar: ")
                        print(tabulate(actualizarTodosdatosGamaProductos(id),headers="keys",tablefmt="grid"))
                                       
                  
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
        3. Actualizar gama de productos
                          
        0. Atras          
          
          
          
        

        """)
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
            opcion=int(opcion)
            if opcion>=0 and opcion<=3:      
                if(opcion==1):
                    print(tabulate(agregarDatosGama(), headers="keys",tablefmt="grid"))
                if(opcion==2):
                    idProducto=input("Ingrese el id del producto que desea eliminar: ")
                    print(tabulate(deletearProduct(idProducto)["body"],headers="keys",tablefmt="grid"))                    
                if(opcion==3):
                    actualizarGamaProoductos()
                if(opcion==0):
                    break        

                