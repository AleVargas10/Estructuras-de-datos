from ListaEnlazada import ListaEnlazada

miLista = ListaEnlazada()
numero = 0
opcion = 0

while opcion != 9:
    opcion = int(input("\n1.Ingresar\n2.Mostrar\n3.Buscar\n4.Modificar\n5.Eliminar\n6.Persona de mayor edad\n7.Persona menor edad\n8.Promedio total de edad\n9.Salir\nSeleccione una opcion: "))
    
    match opcion:
        case 1:
            nombre = str(input("Digite el nombre de la persona: "))
            edad = int(input("Digite la edad de la persona: "))
            miLista.insertarNodo(nombre, edad)
            
        case 2:
            print(miLista.mostrarLista())
        
        case 3:
            nombre = str(input("Digite el nombre a buscar: "))
            if (miLista.buscarLista(nombre)):
                print("Persona encontrada.")
        case 4:
            miLista.modificarNodo() 
            
        case 5:
            miLista.eliminarNodo()
            
        case 6:
            print(miLista.mayorEdad())
            
        case 7:
            print(miLista.menorEdad())
        
        case 8:
            print(miLista.promedioEdad())
               
        case 9:
            print("Saliendo del programa...")

        case _:
            print("Opcion invalida.") 