from clases import Patron

class ListaPatron:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def append(self, posX, posY, estado):

        nuevo = Patron(posX, posY, estado)
        self.size += 1

        if self.primero is None:
            self.primero = nuevo
            self.ultimo = nuevo
        elif self.primero.siguiente is None:
            self.primero.siguiente = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo

    def infectarSanas(self):
        actual = self.primero

        while actual is not None:
            if actual.getEstado() == 0:
                actual.setEstado(1)
            actual = actual.siguiente

    def returnInfectada(self):
        return self.primero