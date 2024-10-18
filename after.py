"""

nombre_producto = ""
stock_producto = 0
cant_productos = 0

while nombre_producto != "salir":
    nombre_producto = input("Ingrese el nombre del productos nuevo o salir para finalizar")

    if nombre_producto != "salir":
        stock_producto = input("Ingrese la cantidad de stock disponible")
        print(f"Producto:{nombre_producto} Stock:{stock_producto}")
        cant_productos = cant_productos + 1
    else:
        print("Cerrando el programa")
        print(f"Productos agregados:{cant_productos}")

"""


"""
precio_producto = int(input("Ingrese el precio del producto"))


while precio_producto <= 0:
    print("Solo se premiten precios positivos")
    precio_producto = int(input("Ingrese el precio del producto"))

print(precio_producto)

"""





intentos = 0


while intentos < 3:
    nombre_producto = input("Ingrese el nombre del productos nuevo")
    precio_producto = int(input("Ingrese el precio del producto"))

    if precio_producto > 0:
        print(f"Producto:{nombre_producto} Precio:{precio_producto}")
        break
    else:
        intentos = intentos + 1
        print(f"No se pueden ingresar precio negativos")
        print(f"Cantidad de intentos disponibles {3-intentos}")

