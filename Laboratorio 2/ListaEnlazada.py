from Nodo import Nodo
    
class ListaEnlazada():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def get_primero(self):
        return self.primero

    def set_primero(self, nuevo_primero):
        self.primero = nuevo_primero

    def get_ultimo(self):
        return self.ultimo

    def set_ultimo(self, nuevo_ultimo):
        self.ultimo = nuevo_ultimo

    def insertarNodo(self, nombre, edad):
        nodoNuevo = Nodo(nombre, edad)
        
        if self.get_primero() == None:
            self.primero = nodoNuevo
            self.primero.set_siguiente(None)
            self.ultimo = self.primero
            print("Inserte bien 1")

        else:
            self.ultimo.set_siguiente(nodoNuevo)
            nodoNuevo.set_siguiente(None)
            self.ultimo = nodoNuevo
            print("Inserte bien 2") 
            
    def mostrarLista(self):
        nodoActual = self.primero
        listaString = ""
        
        while nodoActual != None:
            listaString = listaString + str(nodoActual.__str__()) + "\n"       
            nodoActual = nodoActual.get_siguiente()
        return listaString
    
    def buscarLista(self, nombre):
        nodoActual = self.primero
        encontrado = False
        
        while nodoActual != None:
            if nombre == nodoActual.get_nombre():
                encontrado = True
            return encontrado
        nodoActual = nodoActual.get_siguiente()
 
    def modificarNodo(self):
        nombre = input("Digite el nombre que desea modificar:")
        nodoActual = self.primero
        modificado= False
        
        while nodoActual != None:
            
            if nodoActual.get_nombre() == nombre:
                nuevaEdad = input(f"Digite la NUEVA edad de {nombre}: " )
                nodoActual.set_edad(nuevaEdad)
                modificado = True
                
            nodoActual = nodoActual.get_siguiente()
            
        return modificado 
    
    def eliminarNodo(self):
        nombre= input("Digite el nombre que desea eliminar:")
        nodoActual = self.primero

        if nodoActual is not None and nodoActual.get_nombre() == nombre:
            self.primero = nodoActual.get_siguiente()
            nodoActual = None
            return

        anterior = None
        while nodoActual is not None and nodoActual.get_nombre() != nombre:
            anterior = nodoActual
            nodoActual = nodoActual.get_siguiente()

        if nodoActual is None:
            return

        anterior.set_siguiente(nodoActual.get_siguiente())
        nodoActual = None       

    #Devuelve al persona de mayor edad.
    def mayorEdad(self):
        nodoActual = self.primero
        mayor = -float('inf')
        nodoMayor = None

        while nodoActual != None:
            edad_actual = nodoActual.get_edad()

            if edad_actual > mayor:
                mayor = edad_actual
                nodoMayor = nodoActual

            nodoActual = nodoActual.get_siguiente()

        if mayor != -float('inf'):
            return "\nLa persona de mayor edad es {} con {} años.".format(nodoMayor.get_nombre(), nodoMayor.get_edad()) 

        else:
            return "\nNo hay personas registradas."

    #Devuelve la persona de menor edad    
    def menorEdad(self):
        nodoActual = self.primero
        menor = float('inf')
        nodoMenor = None
        
        while nodoActual != None:
            edad_actual = nodoActual.get_edad()
            
            if edad_actual < menor:
                menor = edad_actual
                nodoMenor = nodoActual
            
            nodoActual = nodoActual.get_siguiente()
        
        if menor != float('inf'):
            return "\nLa persona de menor edad es {} con {} años.".format(nodoMenor.get_nombre(), nodoMenor.get_edad()) 

        else:
            return "\nNo hay personas registradas."

    #Saca un promedio de edad con todos las personas agregadas anteriormente.
    def promedioEdad(self):
        nodoActual = self.primero
        edades = 0
        cantidad = 0
        
        while nodoActual != None:
            edades +=  int(nodoActual.get_edad())        
            nodoActual = nodoActual.get_siguiente()
            cantidad += 1
            
        promedio = edades/cantidad
            
        return "\nEl promedio de edad es de {}.".format(promedio)
            
