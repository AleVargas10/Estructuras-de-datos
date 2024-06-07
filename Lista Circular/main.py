from ListaCircular import ListaCircular
miLista = ListaCircular()
numero = 0
opcion = 0

while opcion != 6:
    opcion = int(input("\n1.Ingresar\n2.Mostrar\n3.Buscar\n4.Modificar\n5.Eliminar\n6.Salir\nDigite la opcion que require realizar:"))
    
    match opcion:
        case 1:
            numero = int(input("Digite el número que desea insertar: "))
            miLista.agregar(numero)
            
        case 2:
            print(miLista.mostrar())
            
        case 3:
            numero= int(input("Digite el número que desea buscar: "))
            if (miLista.buscar(numero)):
                print("Número encontrado.")
            else:
                print("Número no encontrado.")
                
        case 4:
            miLista.modificar()
        
        case 5:
            numero = int(input("Digite el numero que desea eliminar: "))
            miLista.eliminar(numero)
            
        case 6:
            print("Saliendo del programa...")

        case _:
            print("Opcion invalida.")