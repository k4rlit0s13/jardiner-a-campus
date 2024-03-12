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



#Obtner todos los productos que pertenecen a la gama ornamentales con mas de 100 unidades en stock
def getAllProductsOrnamentals(gama,stock):
        AllproductsOrnamentals=[]
        for val in pro.producto:
            if (val.get("gama")==gama and val.get("cantidad_en_stock")>=stock):
                AllproductsOrnamentals.append(val)
        def price(val):
                return val.get("precio_venta")
        AllproductsOrnamentals.sort(key=price,reverse=True)
        for i,val in enumerate(AllproductsOrnamentals):
                AllproductsOrnamentals[i]={
                        "codigo":val.get("codigo_producto"),
                        "venta":val.get("precio_venta"),
                        "nombre":val.get("nombre"),
                        "gama":val.get("gama"),
                        "dimensiones":val.get("dimensiones"),
                        "proveedor":val.get("proveedor"),
                        "descripcion":f'{val.get("descripcion")[:5]}...' if  AllproductsOrnamentals[i].get("descripcion") else val.get("descripcion"),
                        "stock":val.get("cantidad_en_stock"),
                        "base":val.get("precio_proveedor"),
                  }
        return AllproductsOrnamentals
            












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
        5. Obtner todos los productos de una categoria ordenando sus precios de venta, también que su cantidad de inventario sea superior (ejemplo: Ornamentales, 100)
                   
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
        if(opcion==5):
            gama=input("ingrese la gama que deseas mostrar: ")
            stock=int(input("ingrese las unidades que deseas mostrar: "))
            print(tabulate(getAllProductsOrnamentals(gama,stock), headers="keys",tablefmt="grid"))
        if(opcion==0):
            break

