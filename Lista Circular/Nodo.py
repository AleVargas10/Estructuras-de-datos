class Nodo():
    def __init__(self, dato):
        self.siguiente = None
        self.dato = dato

    def get_dato(self):
        return self.dato

    def set_dato(self, dato):
        self.dato = dato

    def get_siguiente(self):
        return self.siguiente

    def set_siguiente(self, nuevo_siguiente):
        self.siguiente = nuevo_siguiente