fichero = open ("fichero.txt","r")
caracter = fichero.read()
# si queremos leer caracter por caracter se usa el siguiente comando
#caracter = fichero.read(1)
while caracter != "":
    print (caracter)
    caracter = fichero.read()
