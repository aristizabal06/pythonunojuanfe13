#Creando variables y cicloen en python

menuOpciones=0

#Pasos para crear una lista
#1. Secrea la variable y se iguala a corchetes
listaProductos=[]

while menuOpciones != 5:
    print("Bienvenido a Bodegas juanfe")
    print("***************************")

    print("1. Digita 1 para agregar un producto a la bodega: ")
    print("2. Digita 2 para ver todos los productos de la bodega:" )
    print("3. Digita 3 para calcular al costo total de la bodega: ")

    menuOpciones=int(input("\nDigita una opcion: "))
    
    if menuOpciones == 1:
        print("🛒 comensaremos a registrar un producto: \n")
        #Un producto es un diccionario(objetos)
        #Pasos para crear un diccionario
        #1. creamos la variable utilizando llaves
        diccionarioProductos={}
        #2. Agregamos valores y llaves al diccionario
        diccionarioProductos["id"]=int(input("Digita el id del producto: "))
        diccionarioProductos["nombre"]=int(input("Digita el nombre del producto: "))
        diccionarioProductos["descripcion"]=int(input("Digita la descripcion del producto: "))
        diccionarioProductos["precioUnitario"]=int(input("Digita el precio del producto: "))
        diccionarioProductos["cantidadBodega"]=int(input("Digita la cantidad del producto: "))
        #fotografia
        #marca
        diccionarioProductos["fotografia"]=int(input("Digita la fotografia del producto: "))
        diccionarioProductos["marca"]=int(input("Digita la marca del producto: "))
        #3. Agregando un diccionario a una lista 
        listaProductos.append(diccionarioProductos)
        print("/n Exito agregado el producto 😁 /n")

    elif menuOpciones == 2:
        print("📒 revisaremos nuestro inventario: \n")
    elif menuOpciones == 3:
        print("💰 estamos calculando: \n")       
    else:
        print("😔 aun no contamos con esa opcion... \n")    