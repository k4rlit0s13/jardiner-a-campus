#vista para tablas


from tabulate import tabulate

import requests
import json
import re

import modules.getClients as cliente
import modules.getEmpleados as empleado
import modules.getGamaProducto as gama
import modules.getOficina as oficina               
import modules.getPago as getPa
import modules.getPedido as pedido
import modules.getProducto as producto
import modules.getDetallePedido as getDet







# import sys 
# for nombre,objeto in sys.modules.items():
#     if nombre.startswith("modules"):
#         modulo= getattr(objeto,"__name__", None)
#         file=modulo.split("get")[-1]
#         print(file)



# import sys

# def menu():
#     contador = 1
#     print("Menu Principal")
#     for nombre, objeto in sys.modules.items():
#         if nombre.startswith("modules"):
#             modulo_name = getattr(objeto, "*name*", None)
#             if modulo_name and modulo_name != "modules":
#                 print(f"{contador}. {modulo_name.split('get')[-1]} ")
#                 contador += 1
# menu()













# # https://manytools.org/hacker-tools/ascii-banner/
if (__name__=="__main__"):
    while True:





        print(f"""
          
███╗   ███╗███████╗███╗   ██╗██╗   ██╗                          
████╗ ████║██╔════╝████╗  ██║██║   ██║                          
██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║                          
██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║                          
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝                          
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝                           
                                                                
██████╗ ██████╗ ██╗███╗   ██╗ ██████╗██╗██████╗  █████╗ ██╗     
██╔══██╗██╔══██╗██║████╗  ██║██╔════╝██║██╔══██╗██╔══██╗██║     
██████╔╝██████╔╝██║██╔██╗ ██║██║     ██║██████╔╝███████║██║     
██╔═══╝ ██╔══██╗██║██║╚██╗██║██║     ██║██╔═══╝ ██╔══██║██║     
██║     ██║  ██║██║██║ ╚████║╚██████╗██║██║     ██║  ██║███████╗
╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝
                                                                
    1. Cliente
    2. Oficina
    3. Empleado
    4. Pedidos
    5. Detalle de pedidos
    6. Gama de producto
    7. Productos
    8. Pagos
              
    0.Salir del programa
              
""")
    
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=8:    
                        if(opcion==1):
                                cliente.menu()   
                        elif(opcion==2):
                                oficina.menu()
                        elif(opcion==3):
                                empleado.menu()
                        elif(opcion==4):
                                pedido.menu()
                        elif(opcion==5):
                                getDet.menu()        
                        elif(opcion==6):
                                gama.menu()
                        elif(opcion==7):
                                producto.menu()
                        elif(opcion==8):
                                getPa.menu()
                        elif(opcion==0):
                                break


       
# # ACTIVAR CODIGOS EN LA TERMINAL
"""
json-server storage/cliente.json -b 5001 & json-server storage/oficina.json -b 5002 & json-server storage/empleado.json -b 5003 & json-server storage/pedido.json -b 5004 & json-server storage/detalle_pedido.json -b 5005 & json-server storage/gama_producto.json -b 5006 & json-server storage/producto.json -b 5007 & json-server storage/pago.json -b 5008 
"""    
# si hize un cambio de pc cambiar ips !







# with open("storage/cliente.json", "r") as f:
#         fichero = f.read()
#         data = json.loads(fichero)
#         for i, val in enumerate(data):
#                 data[i]["id"] = (i+1)
#         data = json.dumps(data, indent=4).encode("utf-8")
# with open("storage/cliente.json", "wb+") as f1:
#                 f1.write(data)
#                 f1.close()      















# PRUEBAS DIRECTAS DE LAS FUNCIONES GET

#print(cliente.GetAllNamesSpain())

#print(pedido.obtener_estados_pedidos())

#print(pago.getAll2008Clients(),)

#print(oficina.getAllCityPhone())

#print(tabulate(pedido.obtener_pedidos_entrega_tardia(), tablefmt="grid"))

#print(tabulate(pedido.getAllOrderClientDates2DaysAgo(), tablefmt="grid"))

#print(tabulate(pedido.getAllOrdersRefused2009(), tablefmt="grid"))

# print(tabulate(pago.getAllFormToPay(), tablefmt="grid"))

#print(tabulate(pedido.getAllOrder01(), tablefmt="grid"))