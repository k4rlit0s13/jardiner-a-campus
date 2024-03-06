import storage.pedido as pe

#filtro para devolver un listado con los distintos estados por los que puede pasar un pedido

def obtener_estados_pedidos():
    estados = set()  # Utilizamos un conjunto para asegurarnos de obtener estados únicos
    for pedido in pe.pedido:  
        estado = pedido.get("estado")
        if estado not in estados:
            estados.add(estado)
    return estados

