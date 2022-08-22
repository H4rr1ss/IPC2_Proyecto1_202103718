from clases import Paciente

class ListaSimpleEnlazada:
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
                if actual.siguiente is not None:
                    actual = actual.siguiente
                    cadena += "\n"
                else:
                    break
            else:
                break
                
        print(cadena)

    # FUNCION ELIMINAR