import storage.cliente as cli

def search ():
    clienteNames= list()
    for val in cli.clientes:
        codigoName=dict({
        "codigo_cliente": val.get("codigo_cliente"),
        "nombre_cliente": val.get ("nombre_cliente")
     })
        clienteNames.append(codigoNames)
        return clienteNames
    

def getOneClienteCodigo (codigo):
    clienteNames= list()
    for val in cli.clientes:
        if (val.get("codigo_cliente")==codigo):
            return{
                "codigo_cliente": val.get("codigo_cliente"),
                "nombre_cliente": val.get("nombre_cliente")
            }


def  getAllClientCreditCiudad (limiteCredit,ciudad):
    clienteCredit=list()
    for val in cli.clientes:
        if(val.get("limite_credito")>=limiteCredit and val.get("ciudad")==ciudad):
            clienteCredit.append(val)
    return clienteCredit

def getAllPaisRegionCiudad (pais,region=None,ciudad=None):
    clientZone = list()
    for val in cli.clientes:
        if(
            val.get('pais')==pais and
            (val.get('region')==region or val.get('region')==None) or
            (val.get('ciudad')==ciudad or val.get('ciudad')==None)    
        ):
            clientZone.append(val)
    return clientZone         



#filtro par obtener nombre con la direccion numero 2 de los clientes
def obtener_informacion_clientes():
    clientes_info = []
    for cliente in cli.clientes:
        info = {
            "nombre_cliente": cliente.get("nombre_cliente"),
            "linea_direccion2": cliente.get("linea_direccion2")
        }
        clientes_info.append(info)
    return clientes_info