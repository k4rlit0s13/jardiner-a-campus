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



# opcion 2 borrar datos de la lista 
def deletearProduct(id):

    data=getOf.getAllcode(id)

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
        peticion = requests.post("http://10.0.2.15:5002",headers=headers, data=json.dumps(oficinas, indent=4).encode("UTF-8"))
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
                    
        0. Atras       




        """)
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=2:  
                             
                    if(opcion==1):
                        print(tabulate(agregarDatosoficina(), headers="keys",tablefmt="grid"))
                    if(opcion==2):
                        idProducto=input("Ingrese el id del producto que desea eliminar: ")
                        print(tabulate(deletearProduct(idProducto)["body"],headers="keys",tablefmt="grid"))                        
                    if(opcion==0):
                        break