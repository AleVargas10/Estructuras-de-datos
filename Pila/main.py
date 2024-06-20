# pilas semana 8 C33859
from pilas import Pila

pila = Pila()
opcion = 0
print('la pila está vacía...a no ser',pila.esta_vacia())

pila.apilar(1)
pila.apilar(2)
pila.apilar(3)

print('la pila está vacía...a no ser',pila.esta_vacia())
print('la cima es: ',pila.ver_cima())

print('Desapilando elementos: ')
while not pila.esta_vacia():
    print(pila.desapilar())


while opcion != 11:
    opcion = int(input("""
1 - ¿Pila vacía?
2 - Apilar 
3 - Desapilar
4 - Mostrar elementos
5 - Vaciar
6 - Buscar
7 - Copiar
8 - Ordenar
9 - Cantidad de elementos
10 - Salir\n----------------------\nDigite la opción que requiera: """))
    
    match opcion:
        case 1:
            print(pila.esta_vacia())
        case 2:
            jugada=input('Ingrese un elemento para APILARLO: ')
            print(pila.apilar(jugada))
        case 3:
            print('Desapilando elementos: ')
            while not pila.esta_vacia():
                print(pila.desapilar())
        case 4:
            print(pila.mostrar())
        case 5:
            print(pila.destruir())
        case 6:
            jugada=input('Ingrese un elemento para BUSCAR:')
            print(pila.buscar(jugada))
        case 7:
            print(pila.copiar())
        case 8:
            print(pila.ordenar())
        case 9:
            print(pila.cantidadElementos())
            
        case 10:
            print("Saliendo del programa...")
        case _:
            print("Opción Inválida")



















