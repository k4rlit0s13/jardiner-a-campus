import storage.gama_producto as gama
from tabulate import tabulate


#Obtener toda la gama de productos
def getAllGamaProducts():
    AllStockPriceGama=[]
    for precio in gama.gama_producto:
        AllStockPriceGama.append({
            "Gama": precio.get("gama"),
            "Descripcion del produ": precio.get("descripcion_texto")
        })
    return AllStockPriceGama




def menu():
    while True:
        print(f"""
              
 ██████╗  █████╗ ███╗   ███╗ █████╗     ██████╗ ███████╗                    
██╔════╝ ██╔══██╗████╗ ████║██╔══██╗    ██╔══██╗██╔════╝                    
██║  ███╗███████║██╔████╔██║███████║    ██║  ██║█████╗                      
██║   ██║██╔══██║██║╚██╔╝██║██╔══██║    ██║  ██║██╔══╝                      
╚██████╔╝██║  ██║██║ ╚═╝ ██║██║  ██║    ██████╔╝███████╗                    
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝                    
                                                                            
██████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗ ██████╗████████╗ ██████╗ ███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔═══██╗██╔════╝
██████╔╝██████╔╝██║   ██║██║  ██║██║   ██║██║        ██║   ██║   ██║███████╗
██╔═══╝ ██╔══██╗██║   ██║██║  ██║██║   ██║██║        ██║   ██║   ██║╚════██║
██║     ██║  ██║╚██████╔╝██████╔╝╚██████╔╝╚██████╗   ██║   ╚██████╔╝███████║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝   ╚═╝    ╚═════╝ ╚══════╝
                                                                            

              1. Obtener toda la gama de productos
            
              0. Salir al menu principal

""")
        
        opcion=int(input("\n Seleccione una opcion: "))

        if (opcion==1):
            print(tabulate(getAllGamaProducts(), headers="keys",tablefmt="grid"))
        if(opcion==0):
            break