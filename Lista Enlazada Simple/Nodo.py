from Persona import Persona

class Nodo(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.siguiente = None
        
    def get_siguiente(self):
        return self.siguiente

    def set_siguiente(self, nuevo_siguiente):
        self.siguiente = nuevo_siguiente




