# pilas semana 8 C33859
from nodo import Nodo
class Pila:
    def __init__(self):
        self.cima = None
#------------------------------------------- 
    def esta_vacia(self):
        return self.cima is None
#-------------------------------------------
    def apilar(self,valor):
        nuevo_nodo = Nodo(valor)
        if self.cima is None:
            self.cima = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cima
            self.cima = nuevo_nodo
#-------------------------------------------
    def desapilar(self):
        if self.cima is None:
            print("La pila esta vacia.")
        else:
            valor = self.cima.valor
            self.cima = self.cima.siguiente
            return valor
#-------------------------------------------
    def ver_cima(self):
        if self.cima is None:
            print('la pila está vacía')
        else:
            return self.cima.valor
#-------------------------------------------
    def mostrar(self):
        actual = self.cima
        while actual != None:
            print(actual.valor)
            actual = actual.siguiente
#-------------------------------------------
    def destruir(self):
        while not self.esta_vacia():
            self.desapilar()
        print("Pila vacia.")
#-------------------------------------------
    def buscar(self, valor):
        actual = self.cima
        encontrado = False
        while actual != None:
            if actual.valor == valor:
                encontrado = True
            actual = actual.siguiente
        return encontrado
#-------------------------------------------
    def copiar(self):
        actual = self.cima
        copia_pila = Pila()
        while actual != None:
            copia_pila.apilar(actual.valor)
            actual = actual.siguiente
        actual = self.cima
        while actual != None:
            copia_pila.apilar(actual.valor)
            actual = actual.siguiente
        return copia_pila
#-------------------------------------------
    def ordenar(self):
        actual = self.cima
        nodoMenor = self.cima
        while actual != None:
            while nodoMenor != None:
                if actual.valor >= nodoMenor.valor:
                    nodoMenor = nodoMenor.siguiente
                elif actual.valor < nodoMenor.valor:                    
                    valor = actual.valor
                    actual.valor = nodoMenor.valor 
                    nodoMenor.valor = valor   
                    nodoMenor = self.cima
            actual = actual.siguiente
            nodoMenor = self.cima
#-------------------------------------------
    def cantidadElementos(self):
        cantidad = 0
        actual = self.cima
        while actual != None:
            cantidad += 1
            actual = actual.siguiente
        return cantidad
#-------------------------------------------

