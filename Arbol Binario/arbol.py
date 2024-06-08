from nodo import Nodo

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar_recursivo(valor, self.raiz)

    def _agregar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._agregar_recursivo(valor, nodo_actual.izquierdo)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._agregar_recursivo(valor, nodo_actual.derecho)

    def in_order_traversal(self):
        self._in_order_traversal_recursivo(self.raiz)

    def _in_order_traversal_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            self._in_order_traversal_recursivo(nodo_actual.izquierdo)
            print(nodo_actual.valor)
            self._in_order_traversal_recursivo(nodo_actual.derecho)
    
    def buscar(self, valor):
        nodo_actual = self.raiz
        
        while nodo_actual != None:
            
            if nodo_actual.valor < valor:
                nodo_actual = nodo_actual.derecho
            
            elif nodo_actual.valor > valor:
                nodo_actual = nodo_actual.izquierdo

            else:
                return True
            
        return False
    
    def modificar(self, valor, modificar):
        nodo_actual = self.raiz
        
        if self.buscar(valor):
            
            if nodo_actual.valor < valor:
                nodo_actual = nodo_actual.derecho
            
            elif nodo_actual.valor > valor:
                nodo_actual = nodo_actual.izquierdo
            
            if nodo_actual == valor:
                nodo_actual.valor = modificar
                return print('Valor modificado.')
                
        else:
            print('El valor no existe en el arbol.')
            
    def _eliminar_recursivo(self, nodo, valor):
        
        if nodo is None:
            return print("El arbol esta vacio.")
        
        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, valor)
        
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, valor)
        
        else:
            if nodo.izquierdo is None and nodo.derecho is None: #perdí al bebé
                return None
        
            if nodo.izquierdo is None:# un solo hijo
                return nodo.derecho
            
            elif nodo.derecho is None:
                return nodo.izquierdo

            temp = self._buscar_un_minimo(nodo.derecho) # dos hijos
            nodo.valor = temp.valor
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, temp.valor)
        return nodo

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)
        print('El valor de la raiz es: ', self.raiz.valor)
            
    def _buscar_un_minimo(self, nodo):
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual
    
    def modificar(self):
        valor = int(input('Digite el valor a MODIFICAR: '))
        if self.buscar(valor):
            modificar = int(input('Digite el valor para REEMPLAZAR: '))
            self.eliminar(valor)
            self.agregar(modificar)
    
    def recursivo_preorder(self, nodo):
        if nodo is not None:
            print(nodo.valor)
            self.recursivo_preorder(nodo.izquierdo)
            self.recursivo_preorder(nodo.derecho)
            
    def preorder(self):
        self.recursivo_preorder(self.raiz)
    
    def recursivo_postorder(self,nodo):
       if nodo is not None:
           self.recursivo_postorder(nodo.izquierdo)          
           self.recursivo_postorder(nodo.derecho)
           print(nodo.valor) 

    def postorder(self):
        self.recursivo_postorder(self.raiz)
    
    def minimo(self):
        nodo = self.raiz
        print(self._buscar_un_minimo(nodo).valor)
        
    def maximo(self):
        nodo = self.raiz
        while nodo.derecho is not None:
            nodo = nodo.derecho
        print(nodo.valor)
    
    def altura_derecha(self, nodo):
        altura = 0
        if nodo is not None:
            self.altura_derecha(nodo.derecha)
            altura += 1
            
    def altura_recursivo(self, nodo):
        if nodo is None:
            return -1
        if nodo.izquierdo is None and nodo.derecho is None:
            return 0 
        else:
            x = -1
            y = -1
            
            if nodo.izquierdo is not None:
                x = self.altura_recursivo(nodo.izquierdo)
            if nodo.derecho is not None:
                y = self.altura_recursivo(nodo.derecho)
                
            return 1 + max(x, y) 
        
    def altura(self):
        return self.altura_recursivo(self.raiz)
