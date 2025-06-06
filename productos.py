import json

lista_productos = [
    {"id": 1, "nombre": "Televisor", "precio": 746.0},
    {"id": 2, "nombre": "Cama", "precio": 1240.0},
    {"id": 3, "nombre": "Celular", "precio": 340.0}
]

try:
    with open('productos.json', 'w') as archivo:
        json.dump(lista_productos, archivo, indent=2)

    with open('productos.json', 'r') as archivo:
        productos_cargados = json.load(archivo)

    nuevo_producto = {"id": 4, "nombre": "Lapto", "precio": 456.0}
    productos_cargados.append(nuevo_producto)

    with open('productos.json', 'w') as archivo:
        json.dump(productos_cargados, archivo, indent=2)

    print("Felicitaciones el producto fue agregado con exito ")

except json.JSONDecodeError:
    print("Realiza de nuevo el archivo no se pudo encontrar ")
