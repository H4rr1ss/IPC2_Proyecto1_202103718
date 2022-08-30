from clases import Patron

class ListaPatron:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def append(self, posX, posY, estado):

        nuevo = Patron(posX, posY, estado)

        if self.primero is None:
            self.primero = nuevo
            self.ultimo = nuevo
        elif self.primero.siguiente is None:
            self.primero.siguiente = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo

    def returnInfectadas(self):
        actual = self.primero

        while actual is not None:
            print("Celula " + " X:" + str(actual.getPosX()) + ", Y:" + str(actual.getPosY()) + " |Estado: " + str(actual.getEstado()))
            actual = actual.siguiente

    def infectarSanas(self):
        actual = self.primero

        while actual is not None:
            if actual.getEstado() == 0:
                actual.setEstado(1)
            actual = actual.siguiente

    def returnInfectada(self):
        return self.primero