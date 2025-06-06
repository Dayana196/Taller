import csv 
import os

archivo = 'usuarios.csv'
id_objetivo = '3'
nueva_ciudad = 'cali'

#crear el archivo si no existe 
if not os.path.exists (archivo):
    print("Archivo no encontrado")

usuarios_iniciales = [

    {'id': 1, 'nombre': 'ana', 'edad': '25', 'ciudad': 'Bogota'},
    {'id': 1, 'nombre': 'juan', 'edad': '30', 'ciudad': 'Medellin'},
    {'id': 1, 'nombre': 'luisa', 'edad': '22', 'ciudad': 'Barranquilla'},
    {'id': 1, 'nombre': 'camila', 'edad': '28', 'ciudad': 'Bucaramanga'},
]

campos = ['id', 'nombre', 'edad', 'ciudad']

with open (archivo, mode='w', newline="", encoding= 'utf-8') as archivo_creado: 
    escritor = csv.DictWriter (archivo_creado, fieldnames=campos)
    escritor.writeheader ()
    escritor.writerows (usuarios_iniciales)

    print ("Archivo creado exitosamente.\n")

try: 
    with open (archivo,mode='r', newline="") as archivo_entrada:
        lector = csv.DictReader (archivo_entrada)
        usuarios = list (lector)
        campos = lector.fieldnames
        if campos is None:
            raise ValueError ("El archivo CSV no tiene encabezados")
    
    for usuario in usuarios:
        if usuario ['id'] == id_objetivo:
            usuario['ciudad']= nueva_ciudad 

    with open (archivo,mode='w',newline="") as archivo_salida:
        escritor = csv.DictWriter(archivo_salida, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(usuarios)
    print(f"Ciudad del usuario con ID {id_objetivo} actualizada a '{nueva_ciudad}',")

except FileNotFoundError:
    print ("Error el archivo no fue encontrado")
