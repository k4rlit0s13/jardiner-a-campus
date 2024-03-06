import storage.pedido as pe

#filtro para devolver un listado con los distintos estados por los que puede pasar un pedido

def obtener_estados_pedidos():
    estados = set()  # Utilizamos un conjunto para asegurarnos de obtener estados únicos
    for val in pe.pedido:  
        estado = val.get("estado")
        if val.get not in estados:
            estados.add(estado)
    return estados

#filtro para 