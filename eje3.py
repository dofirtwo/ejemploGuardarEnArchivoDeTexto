try:
    archivo=open("frutas.txt","a")
    frutas=input("Ingrese nombre de fruta ")
    archivo.write(f"{frutas}\n")
    archivo.close
except IOError as error:
    print(error)