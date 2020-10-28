fichero = open ("FicheroEj.txt","w")
h= "hola"
n= 123
dato = h +","+ str(n)
print (dato)
fichero.write (dato+"\n")
fichero.close()
