#lista con almenos 5 usuarios 
import csv 
usuarios = [

    {"id": 100, "nombre": "Fernando", "ciudad": "Bogota"},
    {"id": 101, "nombre": "Victoria", "ciudad": "Medellin"},
    {"id": 102, "nombre": "Santiago", "ciudad": "Bogota"},
    {"id": 103, "nombre": "Dayana", "ciudad": "Cali"},
    {"id": 104, "nombre": "Lia", "ciudad": "Bogota"},

    ]

#Crear un archivo usuarios.csv con encabezado

with open("usuarios.csv", mode= "w", newline="", encoding= "utf-8") as  archivo:
    campos = ["id", "nombre", "ciudad"]
    escritor = csv.DictWriter (archivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(usuarios)

print ("Archivo 'usuarios.csv' creado exitosamente.💯")

#Leer archivo y filtrar usuarios que vivan en Bogotá
try: 
    with open ("usuarios.csv", mode = "r", newline="") as archivo:
        lector = csv.DictReader(archivo)
        print ("usuarios que viven en bogota: 👇" )
        for fila in lector:
             if fila["ciudad"]=="Bogota":
                print (f"id: {fila['id']}, Nombre : {fila['nombre']}")
except FileNotFoundError :
        print ("🚫 Error: El archivo 'usuarios.csv' no fue encontrado🚫.")
