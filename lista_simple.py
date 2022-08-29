from clases import Paciente

class Lista_Paciente:
    def __init__(self):
        self.raiz = Paciente()
        self.ultimo = Paciente()

    def append(self, nuevoPaciente):
        if self.raiz.getNombre() is None:
            self.raiz = nuevoPaciente
            self.ultimo = nuevoPaciente
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevoPaciente
            self.ultimo = nuevoPaciente
        else:
            self.ultimo.siguiente = nuevoPaciente
            self.ultimo = nuevoPaciente  

    def print(self):
        actual = self.raiz
        cadena = ""
        contador = 0
        while True:
            contador += 1
            if actual.getNombre() is not None:
                cadena += "   " + str(contador) + "| Nombre: " + actual.getNombre() + " -> Edad: " + str(actual.getEdad())
                cadena += "\n       Rejilla de paciente:"
                cadena += "\n        "
                cadena += str(actual.getListaCelda())
                if actual.siguiente is not None:
                    actual = actual.siguiente
                    cadena += "\n"
                else:
                    break
            else:
                break
        print(cadena)

    def returnPaciente(self, numero):
        actual = self.raiz
        i = 1

        while actual is not None:
            if i == numero:
                return actual.getNombre(), actual.getEdad(), actual.getPeriodo(), actual.getDimension(), actual.getListaCelda(), actual.getListaPatron()
            actual = actual.siguiente
            i += 1

    # FUNCION ELIMINAR