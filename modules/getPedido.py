import storage.pedido as pe

#filtro para devolver un listado con los distintos estados por los que puede pasar un pedido

def obtener_estados_pedidos():
    estados = set()  # Utilizamos un conjunto para asegurarnos de obtener estados únicos
    for val in pe.pedido:  
        estado = val.get("estado")
        if val.get not in estados:
            estados.add(estado)
    return estados

#filtro que devuelva un listado con el codigo de pedido, codigo de cliente, fecha esperada y fecha de entrega de los pedidos que no han sido entregados a tiempo
#importar fechas
# def obtener_pedidos_entrega_tardia():
#     pedidos_entrega_tardia = []
#     for pedido in pe.pedido:
#         estado = pedido.get("estado")
#         if estado == "Entregado":
#             fecha_entrega = pedido.get("fecha_entrega")
#             fecha_esperada = pedido.get("fecha_esperada")
#             if fecha_entrega is not None and fecha_esperada is not None:
#                 fecha_entrega_split = fecha_entrega.split("-")
#                 fecha_esperada_split = fecha_esperada.split("-")
#                 if len(fecha_entrega_split) == 3 and len(fecha_esperada_split) == 3:
#                     fecha_entrega = "/".join(fecha_entrega_split[::-1])
#                     fecha_esperada = "/".join(fecha_esperada_split[::-1])
#                     if fecha_entrega > fecha_esperada:
#                         codigo_pedido = pedido.get("codigo_pedido")
#                         codigo_cliente = pedido.get("codigo_cliente")
#                         pedidos_entrega_tardia.append({
#                             "Código_de_pedido": codigo_pedido,
#                             "Código_de_cliente": codigo_cliente,
#                             "Fecha_esperada": fecha_esperada,
#                             "Fecha_de_entrega": fecha_entrega
#                         })
#     return pedidos_entrega_tardia
def obtener_pedidos_entrega_tardia():
   pedidos_entrega_tardia=[{
        "Código_de_pedido": pedido.get("codigo_pedido"),
        "Código_de_cliente": pedido.get("codigo_cliente"),
        "Fecha_esperada": "/".join(pedido.get("fecha_esperada").split("-")[::-1]),
        "Fecha_de_entrega": "/".join(pedido.get("fecha_entrega").split("-")[::-1])
        } 
            for pedido in pe.pedido if pedido.get("estado") == "Entregado"
            and pedido.get("fecha_entrega") and pedido.get("fecha_esperada")
            and pedido.get("fecha_entrega") > pedido.get("fecha_esperada")]
   return pedidos_entrega_tardia 