import storage.cliente as cli

def search ():
    clienteNames= list()
    for val in cli.clientes:
        codigoName=dict({
        "codigo_cliente": val.get("codigo_cliente"),
        "nombre_cliente": val.get ("nombre_cliente")
     })
        clienteNames.append(codigoName)
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





#filtro para obtener nombre con la direccion numero 2 de los clientes
def obtener_informacion_clientes():
    clientes_info = []
    for cliente in cli.clientes:
        info = {
            "nombre_cliente": cliente.get("nombre_cliente"),
            "linea_direccion2": cliente.get("linea_direccion2")
        }
        clientes_info.append(info)
    return clientes_info


#filtro para obtener los nombres de los clientes que contengan un código con número par
def GetAllCodePar ():
    clientes_info = []
    for cliente in cli.clientes:
        codigo_cliente = cliente.get("codigo_cliente")
        if codigo_cliente % 2 == 0:  # Verifica si el código del cliente es par
            info = {
                "nombre_cliente": cliente.get("nombre_cliente"),
                "codigo_cliente": codigo_cliente
            }
            clientes_info.append(info)
    return clientes_info


#filtro que permita buscar clientes cuyos nombres coincidan parcialmente con un término de búsqueda proporcionado
def GetAllsimilarNames(nombre_busqueda):
    clientes_info = []
    for cliente in cli.clientes:
        nombre_cliente = cliente.get("nombre_contacto")
        codigo_cliente = cliente.get("codigo_cliente")
        if nombre_busqueda.lower() in nombre_cliente.lower():  # Verificar si el término de búsqueda está contenido en el nombre del cliente
            info = {
                "nombre_contacto": nombre_cliente,
                "codigo_cliente": codigo_cliente
            }
            clientes_info.append(info)
    return clientes_info


#filtro que muestre clientes por país según el seleccionado
def GetAllClientCountry(pais):
    clientes_info = []
    for cliente in cli.clientes:
        if cliente.get("pais") == pais:
            info = {
            "nombre_cliente": cliente.get("nombre_cliente"),
            "pais":cliente.get("pais")
        }
            clientes_info.append(info)
    return clientes_info


#filtro que muestre los clientes con el primer digito de telefono igual
def GetAllClientTel(numero_telefono):
    clientes_info = []
    for cliente in cli.clientes:
        telefono_cliente = cliente.get("telefono", "")
        if str(telefono_cliente).startswith(str(numero_telefono)): #str para para convertir un objeto en su representación de cadena
            info = {
                "nombre_cliente": cliente.get("nombre_cliente"),
                "telefono": telefono_cliente
            }
            clientes_info.append(info)
    return clientes_info

#filtro que devuelve un listado con el nombre de todos los clientes españoles 
def GetAllNamesSpain():
    clientesEspañoles=[]
    for cliente in cli.clientes:
        if (cliente.get("pais")=='Spain'):
            clientesEspañoles.append(
            {
             "Nombre":cliente.get("nombre_cliente")
            })
    return  clientesEspañoles