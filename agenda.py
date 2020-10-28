import os
def menu():
    print('********** MENU **********')
    print('1.- Crear Fichero')
    print('2.- Ingresar Datos')
    print('3.- Busqueda en fichero')
    print('4.- Consultar lista')
    print('5.- Salir')
    print()
 
def menu2():
    print('a.- Busqueda por nombre')
    print('b.- Busqueda por telefono')   
 
def menu3():
    print("Editar lista")
    print('a.- Eliminar contacto')
    print('b.- Editar  contacto')
    print('c.- Salir a menu principal')
 
opcionmenu = 0
menu()
x=0
op1 = "s"
while opcionmenu != 5:
    opcionmenu = int(input("Inserta un numero para elegir una opcion: "))
    os.system('cls')
    if opcionmenu == 1:
        if os.path.isfile('list.txt'):
            print('El archivo existe.');
            print('Desea Crear de nuevo el archivo, se borraran los datos del archivo');
            op1 = str (input("S/N:  "))
            if (op1 == "S" or op1 == "s"):
                fichero = open ("list.txt","w")
                print ("Fichero creado")
                fichero.close()
        else:
            print('El archivo NO existe.');
            print('Desea Crear el archivo.');
            op1 = str (input("S/N:  "))
            if (op1 == "S" or op1 == "s"):
                fichero = open ("list.txt","w")
                print ("Fichero creado")
                fichero.close()
            op1="N"
            while op1 != "S":    
                print('Desea volver al menu principal.');
                op1 = str (input("S/N:  "))
                op1 = op1.upper()
        os.system('cls')
        menu()         
    elif opcionmenu == 2:
        print("Agregar Nombre, Telefono")
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        fichero = open ("list.txt","a")
        dato = nombre +","+str(telefono)
        fichero.write(dato+"\n")       
        print("Registro Agregado") 
        op1="N"
        print()
        while op1 != "S":    
            print('Desea volver al menu principal.');
            op1 = str (input("S/N:  "))      
            op1 = op1.upper() 
        fichero.close()
        os.system('cls')
        menu() 
    elif opcionmenu == 3:
        print("Busqueda")
        menu2()
        opcionmenu2 = input("Inserta una letra para elegir una opcion: ")
        fichero = open ("list.txt","r")
        cont=0
        if opcionmenu2=="a":
            nombre = input("Nombre: ")
            for linea2 in fichero:
                texto = linea2.split(',')
                if  texto[0] == nombre:
                    cont=cont+1
                    print("Existe coincidencia")
                    print (texto[0].capitalize().strip()+"\t\t\t"+texto[1].strip())               
            if cont == 0:
                print(nombre, "no se encuentra") 
        elif opcionmenu2=="b":
            telefono = input("Telefono: ")            
            for linea2 in fichero:
                texto = linea2.split(',')
                if  (int(texto[1]) == int(telefono)):
                    cont=cont+1
                    print("Existe coincidencia")
                    print (texto[0].capitalize().strip()+"\t\t\t"+texto[1].strip())                
            if cont == 0:
                print(telefono, "no se encuentra")         
        op1="N"
        print('\n')
        while op1 != "S":    
            print('Desea volver al menu.');
            op1 = str (input("S/N:  "))      
            op1 = op1.upper() 
        fichero.close()
        os.system('cls')
        menu()
    elif opcionmenu == 4:
        fichero = open ("list.txt","r")
        ficheroTemp = open ("temp.txt","w")
        print ("Nro\tNOMBRE\t\t\tTELEFONO")
        cont=int(1)
        for linea2 in fichero:
            texto = linea2.split(',')
            dato = str(cont)+","+texto[0].strip()+","+texto[1].strip();           
            print(str(cont)+"\t"+texto[0].capitalize().strip()+"\t\t\t"+texto[1].strip());
            ficheroTemp.write(dato+"\n");
            cont=cont+1;
        ficheroTemp.close()
        fichero.close()
        print("\n")
        menu3()
        opcionmenu2 = input("Inserta una letra para elegir una opcion: ")
        opcionmenu2 = opcionmenu2.lower()
        if opcionmenu2=="a":
            fichero1 = open ("temp.txt","r")
            fichero = open ("list.txt","w")
            nro = input("Introduce el Nro: ")            
            for linea2 in fichero1:
                texto = linea2.split(',')
                if  (int(texto[0]) != int(nro)):
                    dato = texto[1].strip() +","+texto[2].strip()
                    fichero.write(dato+"\n")
            fichero.close()
            fichero1.close()

        elif opcionmenu2=="b":
            fichero1 = open ("temp.txt","r")
            fichero = open ("list.txt","w")
            nro = input("Introduce el Nro: ")  
            nombre = input("Nombre: ")
            telefono = input("Telefono: ")          
            for linea2 in fichero1:
                texto = linea2.split(',')
                if  (int(texto[0]) == int(nro)):
                    dato = nombre +","+str(telefono) 
                    fichero.write(dato+"\n")
                else:
                    dato = texto[1].strip() +","+texto[2].strip()
                    fichero.write(dato+"\n")
            fichero.close()
            fichero1.close() 
        elif opcionmenu2=="c":                   
            fichero.close()
        os.system('cls')
        menu() 
    elif opcionmenu != 5:
        menu()