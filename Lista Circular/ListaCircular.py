from Nodo import Nodo

class ListaCircular():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    def es_vacia(self):
        return self.primero is None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        
        if self.es_vacia():
            self.primero = nuevo_nodo    
        else:
            self.ultimo.siguiente = nuevo_nodo
            
        self.ultimo = nuevo_nodo
        self.ultimo.siguiente = self.primero    
    
    def mostrar(self):
        if self.es_vacia():
            print("La lista está vacía.")
            return 
        nodo_actual = self.primero
        
        while True:
            print(nodo_actual.dato, end= " -> ")
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primero:
                break
        print()

    def buscar(self, dato):
        nodo_actual = self.primero
        encontrado= False
        
        while True:
            if nodo_actual.dato == dato:
               encontrado = True
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primero:
                break
        return encontrado
    
    def modificar(self):
        numero= int(input("Digite el número que desea modificar:"))
        nodo_actual = self.primero
        modificado= False
        
        while True:
            if nodo_actual.dato == numero:
                nuevoNumero = int(input("Digite el NUEVO número que desea:"))
                nodo_actual.set_dato(nuevoNumero)
                modificado = True
            nodo_actual = nodo_actual.get_siguiente()
            if nodo_actual == self.primero:
                break
        return modificado
    
    def eliminar_malo(self):
        numero= int(input("Digite el número que desea eliminar:"))
        nodo_actual = self.primero

        if nodo_actual is not None and nodo_actual.dato == numero:
            self.primero = nodo_actual.get_siguiente()
            nodo_actual = self.ultimo
            
            
        anterior = None
        while nodo_actual is not None and nodo_actual.get_dato() != numero:
            anterior = nodo_actual
            nodo_actual = nodo_actual.get_siguiente()

            if nodo_actual == self.primero:
                break
            
        if nodo_actual is None:
            return

        anterior.set_siguiente(nodo_actual.get_siguiente())
        nodo_actual = None
        
    
    def eliminar(self, dato):
        if self.es_vacia():
            print("La lista esta vacia.")
            return

        nodo_actual = self.primero
        nodo_anterior = None
        
        while True:
            if nodo_actual.dato == dato:
                if nodo_anterior:
                    nodo_anterior.siguiente = nodo_actual.siguiente
                    
                else:
                    self.primero = nodo_actual.siguiente
                    self.ultimo.siguiente = self.primero
                
                if nodo_actual == self.ultimo:
                    self.ultimo = nodo_anterior
                
                print(f'Se elimino el nodo con el dato {dato}')
                return
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primero:
                break
        print(f'No se encontro el dato {dato} en la lista.')
        