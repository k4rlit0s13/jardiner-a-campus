import json
import requests
from tabulate import tabulate
import re

import modules.getProducto as getPro





# EL MODULO DE LAS EXPRESIONES REGULARES PARA AGREGAR UN DATO:

# while True:
#     try:

#         if not NombreDeLDiccionarioDentroDeLaFuncion.get("LakeyDelJson"):
#             variableNombre =input("Ingresa el dato ---")
#             if(re.match(r'LA EXPRESION REGULAR',variableNombre)is not None):
#                 Data= importDelGetRespectivo.laFuncionQueNeseciteComprobar(nombreDeLaVariableQueActuaDeparámetro(lo que esta en los get))
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

# ESTRUCTURA DE DATOS DE PRODUCTOS

# def agregarDatosProducto():
#     producto = {
#     "codigo_producto": input("Ingrese el código del producto: "),
#     "nombre": input("Ingrese el nombre del producto: "),
#     "gama": input("Ingrese el tipo de gama(ejemplo: Ornamentales): "),
#     "dimensiones": input("Ingrese las dimensiones del producto: "),
#     "proveedor": input("Ingrese el proveedor: "),
#     "cantidad_en_stock": int(input("Ingrese la cantidad en stock: ")),
#     "precio_venta": int(input("Ingrese el precio de venta: ")),
#     "precio_proveedor": int(input("Ingrese el precio del proveedor: "))

# }
#     headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
#     peticion = requests.post("http://10.0.2.15:5006",headers=headers, data=json.dumps(producto, indent=4).encode("UTF-8"))
#     res = peticion.json()
#     res["Mensaje"] = "Producto Guardado"
#     return [res]




#SERVER A CONECTAR LOS DATOS(JSON DE ESTE ARCHIVO.PY)

def FuncionDeConeccionClienteJson():
      # json-server storage/producto.json -b 5006
      peticion=requests.get("http://10.0.2.15:5007/productos") #aqui tendremos que solocar una ip que es la que tendremos al iniciar el servidor, esto se hace con: json-server storage/producto.json -b (numero de puerto) OJO NUNCA DARLE KILL SOLO CERRAR, SERVIDOR ACTIVO FUNCIONARA EL CODIGO
      Informacion=peticion.json()  # poner el servidor remoto, no el local, estamos usando simulacion de servidores
      return Informacion




def agregarDatosProducto():
    producto={}
    while True:
        try:

            # expresion regular que deje escribir un codigo tipo OR-123 que sea obligatorio los 2 primeros datos en mayusculas y que sean letras nada de simbolos o especiales, un guión pegado y por ultimo 3 numeros todo pegado
            if not producto.get("codigo_producto"):
                codigo=input("Ingresa el código del producto (ejemplo:OR-123): ")
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$',codigo)is not None):
                    Data=getPro.getAllCodeByCode(codigo)
                    if(Data):
                        print(tabulate(Data, headers="keys",tablefmt="grid"))
                        raise Exception("El código del producto ya es existente")
                        #break #solo para el ultimo modulo sino se rompe
                    else:
                        producto["codigo_producto"]=codigo
                        print("El código cumple con el estandar, OK")

            else:
                raise Exception("El código del producto no cumple con el estandar establecido, DENEGADO")



            # expresion regular que tenga en cuenta la escritura de un nombre con la primera letra en mayusc, que se pueda escribir en una sola palabra o mas de una y respete espacios entre si
            if not producto.get("nombre"):
                nombre =input("Ingrese el nombre del producto: ")
                if(re.match(r'^[A-Z][a-z]*(?: [A-Z][a-z]*)*$',nombre)is not None):
                    producto["nombre"]=nombre
                    print("El nombre cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El nombre del producto no cumple con el estandar establecido")


            # expresion regular que tenga en cuenta la escritura de palabras primera letra en mayuscula seguidas de minusculas, una palabra única, nada más, sin numeros ni simbolos especiales
            if not producto.get("gama"):
                gama =input("Ingresa la gama del producto (ejemplos existentes: Herramientas, Ornamentales, Herbaceas, Aromáticas, Frutales): ")
                if(re.match(r'^[A-Z][a-z]+$',gama)is not None):
                    producto["gama"]=gama
                    print("El dato cumple con el estandar,OK")
                    #break #solo para el ultimo modulo sino se rompe
                else:
                    raise Exception("El dato no cumple con el estandar establecid")


            # expresion regular que tenga en cuenta la escritura de unas dimenciones, un numero seguido de una x y terminando con otro numero, estos deben ser enteros y un ejemplo debe quedar asi: 20x50
            if not producto.get("dimensiones"):
                dimenciones=input("Ingresa las dimenciones de tu producto (ejemplo: 20x50): ")
                if(re.match(r'^\d+x\d+$',dimenciones)is not None):
                        producto["dimensiones"]=dimenciones
                        print("El código cumple con el estandar, OK")
                        #break # el break se deja solo para el ultimo modulo sino se rompe toda la cadena
                else:
                    raise Exception("La dimención no cumple con el estandar establecido")


            # expresion regular que tenga en cuenta la escritura de un nombre con primera en mayuscula,seguido de minusculas, que pueda tener mayusculas entremedio si es solo un nombre, que pueda tener más de una palabra nombre y separados con espacios 
            if not producto.get("proveedor"):
                dimenciones=input("Ingresa el nombre del proveedor: ")
                if(re.match(r'^[A-Z][a-zA-Z]*(\s[A-Z][a-z]*)*$',dimenciones)is not None):
                        producto["proveedor"]=dimenciones
                        print("El nombre cumple con el estandar, OK")
                        #break # el break se deja solo para el ultimo modulo sino se rompe toda la cadena
                else:
                    raise Exception("El nombre no cumple con el estandar establecido")            


            # expresion regular que solo tenga en cuenta datos numericos, nada de letras ni simbolos/caracteres especiales, solo valores numericos
            if not producto.get("cantidad_en_stock"):
                stock=input("Ingresa la cantidad de producto en stock: ")
                if (re.match(r'^\d+$',stock)is not None):
                        stock= int(stock)  # SE DEBE TRANSFORMAR DE STRING A VALOR NUMERICO
                        producto["cantidad_en_stock"]=stock
                        print("El dato cumple con el estandar, OK")
                        #break # el break se deja solo para el ultimo modulo sino se rompe toda la cadena
                else:
                    raise Exception("El dato no cumple con el estandar establecido")   


            # expresion regular que solo tenga en cuenta datos numericos, nada de letras ni simbolos/caracteres especiales, solo valores numericos
            if not producto.get("precio_venta"):
                precioVenta=input("Ingresa el valor del precio de venta en dolares (precio entero): ")
                if (re.match(r'^\d+$',precioVenta)is not None):
                        precioVenta= int(precioVenta)
                        producto["precio_venta"]=precioVenta
                        print("El dato cumple con el estandar, OK")
                        #break # el break se deja solo para el ultimo modulo sino se rompe toda la cadena
                else:
                    raise Exception("El dato no cumple con el estandar establecido")  



            # expresion regular que solo tenga en cuenta datos numericos, nada de letras ni simbolos/caracteres especiales, solo valores numericos
            if not producto.get("precio_proveedor"):
                precioProveedor=input("Ingresa el valor del precio del proveedor en dolares (precio entero): ")
                if (re.match(r'^\d+$',precioProveedor)is not None):
                        precioProveedor= int(precioProveedor)
                        producto["precio_proveedor"]=precioProveedor
                        print("El dato cumple con el estandar, OK")
                        break # el break se deja solo para el ultimo modulo sino se rompe toda la cadena
                else:
                    raise Exception("El dato no cumple con el estandar establecido")  



        except Exception as error:
            print(error)

    # PARA SUBIR LOS DATOS AL JSON DE LOS DATOS DE ESTE .PY
    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://10.0.2.15:5007/productos",headers=headers, data=json.dumps(producto, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]

   



# opcion 2 borrar datos de la lista 
def deletearProduct(id):

    data=getPro.deleteProducto(id)

    if(len(data)):  
        peticion=requests.delete(f"http://10.0.2.15:5007/productos/{id}")
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

██████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗ ██████╗████████╗ ██████╗
██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔═══██╗
██████╔╝██████╔╝██║   ██║██║  ██║██║   ██║██║        ██║   ██║   ██║
██╔═══╝ ██╔══██╗██║   ██║██║  ██║██║   ██║██║        ██║   ██║   ██║
██║     ██║  ██║╚██████╔╝██████╔╝╚██████╔╝╚██████╗   ██║   ╚██████╔╝
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝   ╚═╝    ╚═════╝

        1. Guardar un nuevo dato de Producto
        2. Borrar un dato 
        3. Actualizar un dato de producto

        0. Atras




        """)
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=3:

                    if(opcion==1):
                        print(tabulate(agregarDatosProducto(), headers="keys",tablefmt="grid"))
                    if(opcion==2):
                        idProducto=input("Ingrese el id del producto que desea eliminar: ")
                        print(tabulate(deletearProduct(idProducto)["body"],headers="keys",tablefmt="grid"))
                    if(opcion==0):
                        break