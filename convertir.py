import csv
import json

def convertir_csv_a_json(csv_archivo, json_archivo):
    try:
        #abrimos y leemos el CSV
        with open (csv_archivo, newline="", ) as archivo_csv:
            lector_csv = csv.DictReader (archivo_csv)
            datos= []
            for fila in lector_csv:
                datos.append(fila)

            #escribimos los datos en formato json 
            with open (json_archivo, "w", ) as archivo_json:
                json.dump(datos, archivo_json, indent=2)
            print ("Archivo convertido exitosamente en json")
    except FileNotFoundError:
        print("El archivo csv no fue encontrado")

#call de funcion 
convertir_csv_a_json ('usuarios.csv', 'usuarios.json')
