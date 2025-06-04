#Sobrescribir un archivo de texto y luego añadir contenido

path = "Diario.txt"
#Crea (o sobrescribe) el archivo `diario.txt` y escribe en la primera línea:
#Fecha: 2025-06-02
with open (path,"w") as archivo:
    archivo.write ("Fecha: 2025-06-02\n")
#luego, abre el mismo archivo en modo append (`'a'`) para agregar dos líneas más con tus actividades del día.
with open (path,"a") as archivo: 
    archivo.write ("Estudie python\n")
    archivo.write ("Realize un examen\n")

print ("Contenido del diaro\n")
#Al final, vuelve a abrir en `'r'` y muestra todo el contenido por pantalla.
try:

    with open (path,"r") as archivo:
        contenido = archivo.read() 
        print(contenido)

except FileNotFoundError:
    print("Error el archivo:'Diario.txt' no se encontro\n")





