fichero=open("fichero.txt","r")
#metodo 1
#for linea in fichero:
 #   if linea[-1] == "\n":
  #      linea = linea[:-1]
   # print (linea)
   # print (linea)[:-1]#no incluye a la ultimo caracter

#metodo 2
#for linea2 in fichero:
 #   print (linea2.strip())
 
#metodo 3
linea = fichero.readline()
while linea != "":
    print (linea.rstrip())
    linea=fichero.readline()



