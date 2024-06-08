from arbol import ArbolBinario

# Crear un árbol binario
arbol = ArbolBinario()
opcion = 0 

arbol.agregar(45)
arbol.agregar(23)
arbol.agregar(2)
arbol.agregar(38)
arbol.agregar(7)
arbol.agregar(65)
arbol.agregar(52)
arbol.agregar(96)
arbol.agregar(48)
arbol.agregar(5)

while opcion != 13:
    opcion = int(input('1. Agregar Nodo.\n2. Mostrar Arbol.\n3. Buscar Nodo.\n4. Modificar Nodo.\n5. Eliminar Nodo.\n6. Preorder.\n7. PostOrder\n8. Buscar valor mínimo. \n13. Salir.\nDigite la opcion que desea realizar: '))
    
    match opcion:
        case 1:
            valor = int(input('Digite el valor: '))
            arbol.agregar(valor)
        
        case 2:
            arbol.in_order_traversal()
        
        case 3:
            valor = int(input("Digite el valor del nodo a buscar: "))
            if arbol.buscar(valor) is True:
                print('Valor encontrado.')
            else: 
                print('Valor NO encontrado.')
        
        case 4:
            arbol.modificar()
            
        case 5:
            valor = int(input('Digite el numero a ELIMINAR: '))
            arbol.eliminar(valor)
            
        case 6:
            arbol.preorder()
        
        case 7:
            arbol.postorder()
            
        case 8:
            arbol.minimo()
            
        case 9:
            arbol.maximo()
        
        case 10:
            print("La altura del arbol es de:", arbol.altura())
            
        case 13:
            print('Saliendo del programa...')
        
        case _:
            print('Opcion invalida.')

