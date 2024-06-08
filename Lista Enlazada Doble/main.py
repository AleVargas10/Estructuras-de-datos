from ListaDobleEnlazada import ListaDobleEnlazada

miLista = ListaDobleEnlazada()
numero = 0
opcion = 0

miLista.agregar_final("Ale",2)
miLista.agregar_final("Andy",3)
miLista.agregar_final("Kel",4)
miLista.agregar_inicio("Francel", 1)

while opcion != 10:
    opcion = int(input("\n1. Agregar al inicio.\n2. Agregar al final.\n3. Buscar competidor.\n4. Modificar competidor.\n5. Eliminar competidor.\n6. Mostrar posiciones.\n7. Correr posiciones.\n8. Cambiar posiciones.\n9. Simular carrera.\n10. Salir\nDigite la opcion que require realizar: 5"))
    
    match opcion:
        case 1:
            numero = input("Digite el numero del competidor: ")
            nombre = input("Digite el nombre: ")
            miLista.agregar_inicio(nombre, numero)
            
        case 2:
            numero = input("Digite el numero del competidor: ")
            nombre = input("Digite el nombre: ")
            miLista.agregar_final(nombre, numero)
            
        case 3:
            numero = int(input("Digite el numero del competidor que desea buscar: "))
            if (miLista.buscar(numero)):
                print("Competidor encontrada.")
            else:
                print("Competidor no encontrada.")
                
        case 4:
            miLista.modificar()
        
        case 5:
            numero = int(input("Digite la numero que desea eliminar: "))
            miLista.eliminar(numero)
            
        case 6:
            miLista.mostrar()

        case 7:
            miLista.correr()  
        case 8:
            miLista.mover()
        case 9:
            miLista.carrera()
        case 10:
            print("Saliendo del programa...")

        case _:
            print("Opcion invalida.")