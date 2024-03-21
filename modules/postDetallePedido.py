import json
import requests
from tabulate import tabulate
import re
import modules.getDetallePedido as getDe



def FuncionDeConeccionDetallePedidosJson():
      peticion=requests.get("http://10.0.2.15:5005/detalle_pedidos") 
      Informacion=peticion.json()  
      return Informacion        



#obtener un codigo de la lista directo(optimizado)
def getAllcode(codigo):
       peticion=requests.get(f"http://10.0.2.15:5005/detalle_pedidos/{codigo}")
       return[peticion.json()] if peticion.ok else []




# DELETE DATO
def deletearProduct(id):

    data=getDe.getAllcode(id)

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
    
# POST DATO
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
    peticion = requests.post("http://10.0.2.15:5005/detalle_pedidos",headers=headers, data=json.dumps(detalleProductos, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Dato Guardado"
    return [res]

# UPDATE DATO

def actualizarCodigoPedidoProducto(id):

    while True:
            # SEGUNDO hacemos las OPERACIONES para cada una de las actualizaciones que queremos hacer:

            # actualizar el codigo_pedido sin que se repita con alguno ya existente
            codigo_pedido = (input("Ingresa el nuevo código del pedido: "))
            # Validar solo números
            if not re.match(r"^[0-9]+$", codigo_pedido):
                print("El código del pedido debe ser un número.")
                continue
            # # NO SE VALIDA
            # response = requests.get(f"http://10.0.2.15:5005/detalle_pedidos/{codigo_pedido}")
            # if response.status_code == 200:
            #     print("El código pedido ya existe.")
            #     continue
            break

    # PRIMERO ponemos todo el listado de información de nuestra lista
    cliente = {
        "codigo_pedido":int(codigo_pedido),
        }


    clienteExistente=getAllcode(id)
    if not clienteExistente:
        return{"message":"Cliente no encontrado"}
    
    clienteActualizado= {**clienteExistente[0],**cliente}
    peticion=requests.put(f"http://10.0.2.15:5005/detalle_pedidos/{id}",data=json.dumps(clienteActualizado))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]

def actualizarCodigoProducto(id):
    # actualizar el codigo_producto  sin que se repita con alguno ya existente
    while True:
        # actualizar el codigo_producto del cliente/empresa
        codigo_producto = (input("Ingrese el nuevo código del producto(ejemplo:AA-123): "))
        # Validar código producto
        if not re.match(r"^([A-Z]{2})-(\d{3})$", codigo_producto):
            print("El nombre del código no es válido.")
            continue
        #  # no se asimila
        # response = requests.get(f"http://10.0.2.15:5005/detalle_pedidos/{codigo_producto}")
        # if response.status_code == 200:
        #     print("El código del cliente ya existe.")
        #     continue
        break

    # PRIMERO ponemos todo el listado de información de nuestra lista
    cliente = {
         "codigo_producto": (codigo_producto),
        }


    clienteExistente=getAllcode(id)
    if not clienteExistente:
        return{"message":"Cliente no encontrado"}
    
    clienteActualizado= {**clienteExistente[0],**cliente}
    peticion=requests.put(f"http://10.0.2.15:5005/detalle_pedidos/{id}",data=json.dumps(clienteActualizado))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]

def actualizarCantidadProducto(id):
   # actualizar el cantidad y se puede repetir
    while True:
        # actualizar el cantidad
        cantidad=(input("Ingrese la nueva cantidad: "))

        # Validar cantidad
        if not re.match(r"^[0-9]+$", cantidad):
            print("la cantidad no es válida.")
            continue
        #  # NO ES NECESARIO VALIDAR
        # response = requests.get(f"http://10.0.2.15:5005/detalle_pedidos/{nombre_contacto}")
        # if response.status_code == 200:
        #     print("El código del cliente ya existe.")
        #     continue
        break
    # PRIMERO ponemos todo el listado de información de nuestra lista
    cliente = {
         "cantidad":int(cantidad),
        }


    clienteExistente=getAllcode(id)
    if not clienteExistente:
        return{"message":"Cliente no encontrado"}
    
    clienteActualizado= {**clienteExistente[0],**cliente}
    peticion=requests.put(f"http://10.0.2.15:5005/detalle_pedidos/{id}",data=json.dumps(clienteActualizado))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]

def actualizarPrecioUnidadProducto(id):

    while True:
         # actualizar el teléfono del cliente sin que se repita con alguno ya existente
        numero_linea = (input("Ingresa el nuevo número de linea: "))
        # Validar solo 1 número
        if not re.match(r"^[0-9]$", numero_linea):
            print("El nuevo número de linea se costruye de un número.")
            continue
        # # NO VALIDAMOS
        # response = requests.get(f"http://10.0.2.15:5005/detalle_pedidos/{numero_linea}")
        # if response.status_code == 200:
        #     print("El teléfono del cliente ya existe.")
        #     continue
        break

    # PRIMERO ponemos todo el listado de información de nuestra lista
    cliente = {
         "numero_linea":int(numero_linea),
        }


    clienteExistente=getAllcode(id)
    if not clienteExistente:
        return{"message":"Cliente no encontrado"}
    
    clienteActualizado= {**clienteExistente[0],**cliente}
    peticion=requests.put(f"http://10.0.2.15:5005/detalle_pedidos/{id}",data=json.dumps(clienteActualizado))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]

def actualizarNumeroDeLineaProducto(id):

    while True:
         # actualizar el teléfono del cliente sin que se repita con alguno ya existente
        numero_linea = (input("Ingresa el nuevo número de linea: "))
        # Validar solo 1 número
        if not re.match(r"^[0-9]$", numero_linea):
            print("El nuevo número de linea se costruye de un número.")
            continue
        # # NO VALIDAMOS
        # response = requests.get(f"http://10.0.2.15:5005/detalle_pedidos/{numero_linea}")
        # if response.status_code == 200:
        #     print("El teléfono del cliente ya existe.")
        #     continue
        break



    # PRIMERO ponemos todo el listado de información de nuestra lista
    cliente = {
        "numero_linea":int(numero_linea),
        }


    clienteExistente=getAllcode(id)
    if not clienteExistente:
        return{"message":"Cliente no encontrado"}
    
    clienteActualizado= {**clienteExistente[0],**cliente}
    peticion=requests.put(f"http://10.0.2.15:5005/detalle_pedidos/{id}",data=json.dumps(clienteActualizado))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]

def actualizaridNuevaProducto(id):
    while True:
         # actualizar el codigo del cliente sin que se repita con alguno ya existente
        idNueva = (input("Ingresa el nuevo id del cliente(1,2,...): "))

        # Validar solo números
        if not re.match(r"^[0-9]+$", id):
            print("El id del cliente debe ser un número entero positivo.")
            continue
        # Validar si el código ya existe
        response = requests.get(f"http://10.0.2.15:5005/detalle_pedidos/{idNueva}")
        if response.status_code == 200:
            print("El id del cliente ya existe.")
            continue

        break




    # PRIMERO ponemos todo el listado de información de nuestra lista
    cliente = {
        "id":int(idNueva)
        }


    clienteExistente=getAllcode(id)
    if not clienteExistente:
        return{"message":"Cliente no encontrado"}
    
    clienteActualizado= {**clienteExistente[0],**cliente}
    peticion=requests.put(f"http://10.0.2.15:5005/detalle_pedidos/{id}",data=json.dumps(clienteActualizado))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]

def actualizarTodoUnDatoProducto(id):

    while True:
        # SEGUNDO hacemos las OPERACIONES para cada una de las actualizaciones que queremos hacer:

         # actualizar el codigo_pedido sin que se repita con alguno ya existente
        codigo_pedido = (input("Ingresa el nuevo código del pedido: "))
        # Validar solo números
        if not re.match(r"^[0-9]+$", codigo_pedido):
            print("El código del pedido debe ser un número.")
            continue
        # # NO SE VALIDA
        # response = requests.get(f"http://10.0.2.15:5005/detalle_pedidos/{codigo_pedido}")
        # if response.status_code == 200:
        #     print("El código pedido ya existe.")
        #     continue
        break



    # actualizar el codigo_producto  sin que se repita con alguno ya existente
    while True:
        # actualizar el codigo_producto del cliente/empresa
        codigo_producto = (input("Ingrese el nuevo código del producto(ejemplo:AA-123): "))
        # Validar código producto
        if not re.match(r"^([A-Z]{2})-(\d{3})$", codigo_producto):
            print("El nombre del código no es válido.")
            continue
        #  # no se asimila
        # response = requests.get(f"http://10.0.2.15:5005/detalle_pedidos/{codigo_producto}")
        # if response.status_code == 200:
        #     print("El código del cliente ya existe.")
        #     continue
        break


    # actualizar el cantidad y se puede repetir
    while True:
        # actualizar el cantidad
        cantidad=(input("Ingrese la nueva cantidad: "))

        # Validar cantidad
        if not re.match(r"^[0-9]+$", cantidad):
            print("la cantidad no es válida.")
            continue
        #  # NO ES NECESARIO VALIDAR
        # response = requests.get(f"http://10.0.2.15:5005/detalle_pedidos/{nombre_contacto}")
        # if response.status_code == 200:
        #     print("El código del cliente ya existe.")
        #     continue
        break



    # actualizar el apellido del contacto y se puede repetir
    while True:
        # actualizar el nombre del precio_unidad
        precio_unidad=(input("Ingrese el nuevo precio por unidad: "))

        # Validar precio_unidad
        if not re.match(r"^[0-9]+$", precio_unidad):
            print("El precio no es válido.")
            continue
        #  # NO ES NECESARIO VALIDAR
        # response = requests.get(f"http://10.0.2.15:5005/detalle_pedidos/{precio_unidad}")
        # if response.status_code == 200:
        #     print("El código del cliente ya existe.")
        #     continue
        break


    while True:
         # actualizar el teléfono del cliente sin que se repita con alguno ya existente
        numero_linea = (input("Ingresa el nuevo número de linea: "))
        # Validar solo 1 número
        if not re.match(r"^[0-9]$", numero_linea):
            print("El nuevo número de linea se costruye de un número.")
            continue
        # # NO VALIDAMOS
        # response = requests.get(f"http://10.0.2.15:5005/detalle_pedidos/{numero_linea}")
        # if response.status_code == 200:
        #     print("El teléfono del cliente ya existe.")
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
        response = requests.get(f"http://10.0.2.15:5005/detalle_pedidos/{idNueva}")
        if response.status_code == 200:
            print("El id del cliente ya existe.")
            continue

        break




    # PRIMERO ponemos todo el listado de información de nuestra lista
    cliente = {
        "codigo_pedido":int(codigo_pedido),
        "codigo_producto": (codigo_producto),
        "cantidad":int(cantidad),
        "precio_unidad":float(precio_unidad),
        "numero_linea":int(numero_linea),
        "id":int(idNueva)
        }


    clienteExistente=getAllcode(id)
    if not clienteExistente:
        return{"message":"Cliente no encontrado"}
    
    clienteActualizado= {**clienteExistente[0],**cliente}
    peticion=requests.put(f"http://10.0.2.15:5005/detalle_pedidos/{id}",data=json.dumps(clienteActualizado))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]


















def actualizarPedidos():
    while True:
        print("""
 █████╗  ██████╗████████╗██╗   ██╗ █████╗ ██╗     ██╗███████╗ █████╗ ██████╗         
██╔══██╗██╔════╝╚══██╔══╝██║   ██║██╔══██╗██║     ██║╚══███╔╝██╔══██╗██╔══██╗        
███████║██║        ██║   ██║   ██║███████║██║     ██║  ███╔╝ ███████║██████╔╝        
██╔══██║██║        ██║   ██║   ██║██╔══██║██║     ██║ ███╔╝  ██╔══██║██╔══██╗        
██║  ██║╚██████╗   ██║   ╚██████╔╝██║  ██║███████╗██║███████╗██║  ██║██║  ██║        
╚═╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝        
                                                                                     
██████╗ ███████╗████████╗ █████╗ ██╗     ██╗     ███████╗███████╗    ██████╗ ███████╗
██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔════╝██╔════╝    ██╔══██╗██╔════╝
██║  ██║█████╗     ██║   ███████║██║     ██║     █████╗  ███████╗    ██║  ██║█████╗  
██║  ██║██╔══╝     ██║   ██╔══██║██║     ██║     ██╔══╝  ╚════██║    ██║  ██║██╔══╝  
██████╔╝███████╗   ██║   ██║  ██║███████╗███████╗███████╗███████║    ██████╔╝███████╗
╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝    ╚═════╝ ╚══════╝
                                                                                     
██████╗ ███████╗██████╗ ██╗██████╗  ██████╗                                          
██╔══██╗██╔════╝██╔══██╗██║██╔══██╗██╔═══██╗                                         
██████╔╝█████╗  ██║  ██║██║██║  ██║██║   ██║                                         
██╔═══╝ ██╔══╝  ██║  ██║██║██║  ██║██║   ██║                                         
██║     ███████╗██████╔╝██║██████╔╝╚██████╔╝                                         
╚═╝     ╚══════╝╚═════╝ ╚═╝╚═════╝  ╚═════╝                                          
              

        1. Actualizar código de pedido
        2. Actualizar código de producto
        3. Actualizar cantidad
        4. Actualizar precio
        5. Actualizar número de línea
        6. Actualizar id

        7. Actualizar todas las opciones anteriores

        0. Atras
        

        """)
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=7:   

                    if opcion == 1:
                        id=input("Ingrese la id del cliente que desea actualizar: ")
                        print(tabulate(actualizarCodigoPedidoProducto(id),headers="keys",tablefmt="grid"))
                    
                    if opcion == 2:
                        id=input("Ingrese la id del cliente que desea actualizar: ")
                        print(tabulate(actualizarCodigoProducto(id),headers="keys",tablefmt="grid"))
                
                    if opcion == 3:
                        id=input("Ingrese la id del cliente que desea actualizar: ")
                        print(tabulate(actualizarCantidadProducto(id),headers="keys",tablefmt="grid"))

                    if opcion == 4:
                        id=input("Ingrese la id del cliente que desea actualizar: ")
                        print(tabulate(actualizarPrecioUnidadProducto(id),headers="keys",tablefmt="grid"))

                    if opcion == 5:
                        id=input("Ingrese la id del cliente que desea actualizar: ")
                        print(tabulate(actualizarNumeroDeLineaProducto(id),headers="keys",tablefmt="grid"))

                    if opcion == 6:
                        id=input("Ingrese la id del cliente que desea actualizar: ")
                        print(tabulate(actualizaridNuevaProducto(id),headers="keys",tablefmt="grid"))


                    if opcion == 7:
                        id=input("Ingrese la id del cliente que desea actualizar: ")
                        print(tabulate(actualizarTodoUnDatoProducto(id),headers="keys",tablefmt="grid"))
            
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
        2. Eliminar un dato
        3. Actualizar datos
                    
        0. Atras       


        """)
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=3:  
                             
                    if(opcion==1):
                        print(tabulate(agregarDetalleProductos(), headers="keys",tablefmt="grid"))
                    if(opcion==2):
                        idProducto=input("Ingrese el id del producto que desea eliminar: ")
                        print(tabulate(deletearProduct(idProducto)["body"],headers="keys",tablefmt="grid"))  
                    if(opcion==3):
                        actualizarPedidos()                                             
                    if(opcion==0):
                        break