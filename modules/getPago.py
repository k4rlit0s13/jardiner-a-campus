import storage.pago as pago
#filtro para que devulve un listado en el codigo de cliente de aquellos clientes que realizaron algun pago en 2008, tenga en cuenta que debera eliminar  aquellos codigos de clientes que aparezcan repetidos. Resuelva la consulta

def getAll2008Clients():
    clientes_pagos_2008 = set()  # Utilizamos un conjunto para asegurarnos de obtener códigos de cliente únicos
    for val in pago.pago:  # Suponemos que pago.pago es una lista que contiene todos los pagos
        fecha_pago = val.get("fecha_pago")
        if fecha_pago.startswith("2008"):  # Verificamos si la fecha de pago comienza con "2008"
            clientes_pagos_2008.add(val.get("codigo_cliente"))

    return clientes_pagos_2008

    

