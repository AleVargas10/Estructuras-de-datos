from Nodo import Nodo
import random

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        
    def agregar_final(self, nombre, numero):
        nuevo_nodo = Nodo(nombre, numero)
        
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
            nuevo_nodo.anterior = self.cola
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cola = nuevo_nodo

    def agregar_inicio(self, nombre, numero):
        nuevo_nodo = Nodo(nombre, numero)
        
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
            nuevo_nodo.anterior = self.cola
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cabeza = nuevo_nodo
            
    def eliminar(self, numero):
        if self.cabeza is None:
            return
        actual = self.cabeza
        while int(actual.get_numero()) != numero:
            actual = actual.siguiente
            if actual == self.cabeza:
                print(f"El numero {numero} no se encuentra en la lista.")

        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
        elif actual == self.cabeza:
            self.cabeza = actual.siguiente
            self.cola.siguiente = self.cabeza
            self.cabeza.anterior = self.cola
        elif actual == self.cola:
            self.cola = actual.anterior
            self.cola.siguiente = self.cabeza
            self.cabeza.anterior = self.cola
        else:
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
            
    def mostrar(self):
        actual = self.cabeza
        bandera = True
        if actual.siguiente.siguiente == self.cabeza:
            print("\n" + "Debe haber como minimo 3 competidores para ver el comportamiento de la carrera.")
            bandera = False
        while bandera != False:
            print(f"- Detras del atleta {actual.numero} va el {actual.anterior.numero}, delante del {actual.numero} va el {actual.siguiente.numero}" + "\n")
            actual = actual.siguiente
            if actual == self.cabeza:
                bandera = False    
    
    def mostrarr(self):
        actual = self.cola
        bandera = True
        n = 1
        
        while bandera:
            print('Posición ',n,' - ', actual.get_nombre(), actual.get_numero(), "\n")
            actual = actual.anterior
            n += 1
            if actual == self.cola:
                bandera = False
            
    def buscar(self, numero):
        actual = self.cabeza
        encontrado = False
        bandera = True
        
        while bandera:
            if numero == actual.numero:
                encontrado = True
            actual = actual.siguiente
            if actual == self.cabeza:
                bandera = False
        return encontrado
    
    def modificar(self):
        numero = int(input("Digite el numero del competidor a modificar: "))
        actual = self.cabeza
        bandera = True
        
        while bandera:
            if actual.get_numero() == numero:
                nombre = input("Digite el NUEVO nombre: ")
                actual.set_nombre(nombre)
            actual = actual.siguiente
            if actual == self.cabeza:
                bandera = False
            
    def correr(self):
        actual = self.cabeza
        
        self.cola = self.cola.anterior 
        self.cabeza = actual.anterior 
        self.cola.siguiente = self.cabeza
        actual.siguiente.anterior = actual
        self.cabeza.anterior = self.cola
    
    def mover(self):
        competidor1 = int(input("Digite el número del competidor que desea interecambiar: "))
        competidor2 = int(input("Digite el número del OTRO competidor: "))
        actual = self.cabeza
        bandera = True
        
        while bandera:
            if competidor1 == actual.get_numero():
                numero = actual.get_numero()
                nombre = actual.get_nombre()
                competidor1 = actual
            
            if competidor2 == actual.get_numero():
                competidor2 = actual
                
            actual = actual.siguiente
            
            if actual == self.cabeza:     
                bandera = False
        
        competidor1.set_nombre(competidor2.get_nombre())
        competidor1.set_numero(competidor2.get_numero())
        competidor2.set_nombre(nombre)
        competidor2.set_numero(numero)
        
        
    def carrera(self):
        actual = self.cabeza
        bandera = 1
        
        while bandera != 4:
            avance = random.randint(1,2)
            if avance == 2:
                print("------- Vuelta {} -------".format(bandera))
                numero = actual.siguiente.get_numero()
                nombre = actual.siguiente.get_nombre()
                actual.siguiente.set_nombre(actual.get_nombre())
                actual.siguiente.set_numero(actual.get_numero())
                actual.set_nombre(nombre)
                actual.set_numero(numero)
                actual = actual.siguiente
                bandera += 1
                self.mostrarr()
            elif avance == 1:
                print("------- Vuelta {} -------".format(bandera))
                numero = actual.anterior.get_numero()
                nombre = actual.anterior.get_nombre()
                actual.anterior.set_nombre(actual.get_nombre())
                actual.anterior.set_numero(actual.get_numero())
                actual.set_nombre(nombre)
                actual.set_numero(numero)
                actual = actual.anterior
                bandera += 1
                self.mostrarr()
        
        print(f"El ganador de la carrera fue {self.cola.get_nombre()} con el número {self.cola.get_numero()}")
        
