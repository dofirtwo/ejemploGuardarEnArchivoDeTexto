try:
    archivo=open("frutas.txt","w")

    print("Archivo creado")

    print(type(archivo))

    archivo.close()
except IOError as error:
    print(error)