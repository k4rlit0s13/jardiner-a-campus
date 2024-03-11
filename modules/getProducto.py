import storage.producto as pro
from tabulate import tabulate

#Obtener todos los productos
def getAllProducts():
        AllproductsProducts=[]
        for val in pro.producto:
                AllproductsProducts.append({
                        "Código del Producto": val.get("codigo_producto"),
                        "Nombre": val.get("nombre"),
                        "Gama": val.get("gama"),
                        "Dimensiones": val.get("dimensiones"),
                        "Proveedor": val.get("proveedor"),
                        "Descripción": val.get("descripcion"),
                        "Cantidad en stock": val.get("cantidad_en_stock"),
                        "Precio de Venta": val.get("precio_venta")
})
        return AllproductsProducts


#Obtener la gama de cada producto 
def getAllProductsGama():
        AllProductsGama=[]
        for val in pro.producto:
                AllProductsGama.append({
                        "Código del Producto": val.get("codigo_producto"),
                        "Nombre": val.get("nombre"),
                        "Gama": val.get("gama"),
                        "Precio de Venta": val.get("precio_venta")
})
        return AllProductsGama


#Obtener todas las catidades en stock 
def getAllProductsStock():
        AllProductsStock=[]
        for val in pro.producto:
                AllProductsStock.append({
                        "Código del Producto": val.get("codigo_producto"),
                        "Nombre": val.get("nombre"),
                        "Dimensiones": val.get("dimensiones"),
                        "Cantidad en stock": val.get("cantidad_en_stock"),
})
        return AllProductsStock


# Obtener todos los productos con precio de venta a 11
def getAllProductsStorePrice():
        AllProductsStorePrice=[]
        for val in pro.producto:
                if val.get("precio_venta")== 11:
                        AllProductsStorePrice.append({
                        "Código del Producto": val.get("codigo_producto"),
                        "Nombre": val.get("nombre"),
                        "Precio de Venta": val.get("precio_venta")
})
        return AllProductsStorePrice




def menu():
    while True:
        print(f"""
              
██████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗ ██████╗████████╗ ██████╗ ███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔═══██╗██╔════╝
██████╔╝██████╔╝██║   ██║██║  ██║██║   ██║██║        ██║   ██║   ██║███████╗
██╔═══╝ ██╔══██╗██║   ██║██║  ██║██║   ██║██║        ██║   ██║   ██║╚════██║
██║     ██║  ██║╚██████╔╝██████╔╝╚██████╔╝╚██████╗   ██║   ╚██████╔╝███████║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝   ╚═╝    ╚═════╝ ╚══════╝
                                                                            
        1. Obtener todos los productos
        2. Obtener la gama de cada producto 
        3. Obtener todas las catidades en stock 
        4. Obtener todos los productos con precio de venta a 11
              
        0. Salir al menu principal

""")
        opcion=int(input("\nSeleccione una de las opciones: "))
        
        if(opcion==1):
            print(tabulate(getAllProducts(), headers="keys",tablefmt="grid"))
        if(opcion==2):
            print(tabulate(getAllProductsGama(), headers="keys",tablefmt="grid"))
        if(opcion==3):
            print(tabulate(getAllProductsStock(), headers="keys",tablefmt="grid"))
        if(opcion==4):
            print(tabulate(getAllProductsStorePrice(), headers="keys",tablefmt="grid"))

        if(opcion==0):
            break

