while True:
    try:
        nombre = input("Ingresa tu nombre: ")
        edad_input = input("Ingresa tu edad: ")
        edad = int(edad_input)  #  convertir a entero

        mensaje = "La edad de " + nombre + " es " + str(edad)
        print(mensaje)
        break  # salir del ciclo si todo está bien

    except ValueError:
        print(" La edad debe ser un número. Intenta de nuevo.\n")
