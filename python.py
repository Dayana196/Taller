
#Crea un archivo `notas.txt` con varias líneas de texto (por ejemplo, títulos de películas).
path = "Notas.txt"
mode= "r"
print ("📽️ Peliculas Elegidas📽️")

#Escribe un script que abra `notas.txt` en modo lectura y muestre cada línea numerada.
try: 
    with open(path,mode = "r") as ReadArchivo: 
        readlines = ReadArchivo.readlines() 
    for i,linea in enumerate (readlines,start= 1):
        print(f"{i}),{linea.strip()}")
#Si el archivo no existe, captura la excepción `FileNotFoundError` y muestra un mensaje amigable.
except FileNotFoundError:
    print (f"Error el archivo:'{path}'no se encontro ")
      





