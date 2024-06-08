class Nodo():
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, value):
        self.nombre = value

    def get_numero(self):
        return int(self.numero)

    def set_numero(self, value):
        self.numero = value

    def get_siguiente(self):
        return self.siguiente

    def set_siguiente(self, siguiente):
        self.siguiente = siguiente

    def get_anterior(self):
        return self.anterior

    def set_anterior(self, anterior):
        self.anterior = anterior

        