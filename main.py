#vista para tablas
from tabulate import tabulate


import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPedido as pedido
import modules.getPago as pago

#print(cliente.GetAllNamesSpain())

#print(pedido.obtener_estados_pedidos())

#print(pago.getAll2008Clients(),)

#print(oficina.getAllCityPhone())

#print(tabulate(pedido.obtener_pedidos_entrega_tardia(), tablefmt="grid"))

#print(tabulate(pedido.getAllOrderClientDates2DaysAgo(), tablefmt="grid"))

#print(tabulate(pedido.getAllOrdersRefused2009(), tablefmt="grid"))

print(tabulate(pago.getAllFormToPay(), tablefmt="grid"))