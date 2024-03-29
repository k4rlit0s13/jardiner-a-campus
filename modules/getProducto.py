
from tabulate import tabulate
import requests
import json
import os
import modules.postProducto as postProd
import re


# IP DEL SERVIDOR PRODUCTO:
# http://10.0.2.15:5006

# Al simular los servidores con json tendremos que crear una funcion que nos ayude a llamar esos datos en nuevo formado ya que ya no son python
def FuncionDeConeccionClienteJson():
      # json-server storage/producto.json -b 5006
      peticion=requests.get("http://10.0.2.15:5007/productos") #aqui tendremos que solocar una ip que es la que tendremos al iniciar el servidor, esto se hace con: json-server storage/producto.json -b (numero de puerto) OJO NUNCA DARLE KILL SOLO CERRAR, SERVIDOR ACTIVO FUNCIONARA EL CODIGO
      Informacion=peticion.json()  # poner el servidor remoto, no el local, estamos usando simulacion de servidores
      return Informacion        




# AHORA A CAMBIAR TODAS LAS VARIABLES QUE ERAN IMPORTS POR LA FUNCION DE REQUEST OSEA VOLVEMOS LAS IP'S VARIABLES POR MEDIO DE NA FUNCION QUE OBTENDRA TODOS LOS DATOS



#obtener un codigo de la lista directo(optimizado)
def getAllcode(codigo):
       peticion=requests.get(f"http://10.0.2.15:5007/productos/{codigo}")
       return[peticion.json()]if peticion.ok else []





#obtener solo el código
def getAllCodeByCode(codigo):
        AllproductsProducts=[]
        for val in FuncionDeConeccionClienteJson():
                if val.get("codigo_producto")==codigo:
                        return [val]


#Obtener todos los productos
def getAllProducts():
        AllproductsProducts=[]
        for val in FuncionDeConeccionClienteJson():
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
        for val in FuncionDeConeccionClienteJson():
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
        for val in FuncionDeConeccionClienteJson():
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
        for val in FuncionDeConeccionClienteJson():
                if val.get("precio_venta")== 11:
                        AllProductsStorePrice.append({
                        "Código del Producto": val.get("codigo_producto"),
                        "Nombre": val.get("nombre"),
                        "Precio de Venta": val.get("precio_venta")
})
        return AllProductsStorePrice



#Obtener todos los productos que pertenecen a la gama ornamentales con mas de 100 unidades en stock
def getAllProductsOrnamentals(gama,stock):
        AllproductsOrnamentals=[]
        for val in FuncionDeConeccionClienteJson():
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
        3. Obtener todas las cantidades en stock 
        4. Obtener todos los productos con precio de venta a 11
        5. Obtener todos los productos de una categoria ordenando sus precios de venta, también que su cantidad de inventario sea superior (ejemplo: Ornamentales, 100)
        
        EDITAR DATOS:      
        6. Modificar datos de productos                        
        
        0. Salir al menu principal

""")
        opcion=input("\nEscribe el número de una de las opciones: ")
        if(re.match(r'[0-9]+$',opcion)is not None):
                opcion= int(opcion)
                if opcion>=0 and opcion<=6:      
                                 
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
                        if(opcion==6):
                                postProd.menu()
                        if(opcion==0):
                                break

