#vista para tablas


from tabulate import tabulate

import requests
import json

import modules.getClients as cliente
import modules.getEmpleados as empleado
import modules.getGamaProducto as gama
import modules.getOficina as oficina               
import modules.getPago as pago
import modules.getPedido as pedido
import modules.getProducto as producto








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










import keyboard


# https://manytools.org/hacker-tools/ascii-banner/
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
    5. Gama de producto
    6. Productos
    7. Pagos
              
    0.Salir del programa
              
""")
    
        opcion=int(input("\nEscribe el número de una de las opciones: "))

        if(opcion==1):
            cliente.menu()
        elif(opcion==2):
            oficina.menu()
        elif(opcion==3):
            empleado.menu()
        elif(opcion==4):
            pedido.menu()
        elif(opcion==5):
            gama.menu()
        elif(opcion==6):
            producto.menu()
        elif(opcion==7):
            pago.menu()
        elif(opcion==0):
            break

       















#print(cliente.GetAllNamesSpain())

#print(pedido.obtener_estados_pedidos())

#print(pago.getAll2008Clients(),)

#print(oficina.getAllCityPhone())

#print(tabulate(pedido.obtener_pedidos_entrega_tardia(), tablefmt="grid"))

#print(tabulate(pedido.getAllOrderClientDates2DaysAgo(), tablefmt="grid"))

#print(tabulate(pedido.getAllOrdersRefused2009(), tablefmt="grid"))

# print(tabulate(pago.getAllFormToPay(), tablefmt="grid"))

#print(tabulate(pedido.getAllOrder01(), tablefmt="grid"))