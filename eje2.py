try:
    archivo = open("frutas.txt","r")
    frutas=archivo.readlines()
    letrafr=archivo.readline()
    
    archivo.close()
    print(type(frutas))
    
    print(frutas)
    
    print(type(letrafr))
    for fruta in letrafr:
        print(fruta)
        
except IOError as error:
    print(error)