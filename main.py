#vista para tablas
from tabulate import tabulate


import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPedido as pedido
import modules.getPago as pago




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



# https://manytools.org/hacker-tools/ascii-banner/
if (__name__=="__main__"):
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
                                                                
    1.Cliente
    2.Oficina
    3.Empleado
    4.Pedidos
""")
    
    opcion=int(input("\nEscibe el número de una de las opciones: "))
    
    if(opcion==1):
        cliente.menu()
    elif(opcion==2):
        oficina.menu()
    elif(opcion==3):
        empleado.menu()
    elif(opcion==4):
        pedido.menu() 















#print(cliente.GetAllNamesSpain())

#print(pedido.obtener_estados_pedidos())

#print(pago.getAll2008Clients(),)

#print(oficina.getAllCityPhone())

#print(tabulate(pedido.obtener_pedidos_entrega_tardia(), tablefmt="grid"))

#print(tabulate(pedido.getAllOrderClientDates2DaysAgo(), tablefmt="grid"))

#print(tabulate(pedido.getAllOrdersRefused2009(), tablefmt="grid"))

# print(tabulate(pago.getAllFormToPay(), tablefmt="grid"))

#print(tabulate(pedido.getAllOrder01(), tablefmt="grid"))