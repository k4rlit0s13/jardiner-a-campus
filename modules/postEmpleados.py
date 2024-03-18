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



# opcion 2 borrar datos de la lista 
def deletearProduct(id):

    data=getEm.deleteProducto(id)

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
    peticion = requests.post("http://10.0.2.15:5003",headers=headers, data=json.dumps(empleados, indent=4).encode("UTF-8"))
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
                                                                                                                          
██████╗  █████╗ ████████╗ ██████╗ ███████╗    ███████╗███╗   ███╗██████╗ ██╗     ███████╗ █████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝    ██╔════╝████╗ ████║██╔══██╗██║     ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║  ██║███████║   ██║   ██║   ██║███████╗    █████╗  ██╔████╔██║██████╔╝██║     █████╗  ███████║██║  ██║██║   ██║███████╗
██║  ██║██╔══██║   ██║   ██║   ██║╚════██║    ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  ██╔══██║██║  ██║██║   ██║╚════██║
██████╔╝██║  ██║   ██║   ╚██████╔╝███████║    ███████╗██║ ╚═╝ ██║██║     ███████╗███████╗██║  ██║██████╔╝╚██████╔╝███████║
╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝    ╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝
                                                                                                                             
         
        1. Guardar un nuevo dato de empleados
              
        0. Atras          
          
          
        """)
        
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=1:      
                                 
                    if(opcion==1):
                        print(tabulate(agregarDatosempleados(), headers="keys",tablefmt="grid"))
                    if(opcion==0):
                        break
