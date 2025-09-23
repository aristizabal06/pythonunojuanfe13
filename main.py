#Creando variables y cicloen en python

menuOpciones=0

while menuOpciones != 5:
    print("Bienvenido a Bodegas juanfe")
    print("***************************")

    print("1. Digita 1 para agregar un producto a la bodega: ")
    print("2. Digita 2 para ver todos los productos de la bodega:" )
    print("3. Digita 3 para calcular al costo total de la bodega: ")

    menuOpciones=int(input("\nDigita una opcion: "))
    
    if menuOpciones == 1:
        print("🛒 comensaremos a registrar un producto: \n")
    elif menuOpciones == 2:
        print("📒 revisaremos nuestro inventario: \n")
    elif menuOpciones == 3:
        print("💰 estamos calculando: \n")       
    else:
        print("😔 aun no contamos con esa opcion... \n")    