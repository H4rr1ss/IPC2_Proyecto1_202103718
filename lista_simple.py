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
                if actual.siguiente is not None:
                    actual = actual.siguiente
                    cadena += "\n"
                else:
                    break
            else:
                break
        print(cadena)

    def returnP(self):
        return self.raiz

    def h(self, nombre):
        actual = self.raiz

        while actual is not None:
            if actual.getNombre() == nombre:
                return actual
            actual = actual.siguiente



    def generarSalidaXML2(self):
        actual = self.raiz

        xml = '<?xml version ='+ '"' + str(1.0) + '"' + ' encoding = ' + str('"UTF-8"') + '?>\n'
        xml += '<pacientes>\n'

        while actual is not None:
            xml += '    <paciente>\n'
            xml += '        <datospersonales>\n'
            xml += '            <nombre>' + actual.getNombre() + '</nombre>\n'
            xml += '            <edad>' + str(actual.getEdad()) + '</edad>\n'
            xml += '        </datospersonales>\n'
            xml += '        <periodos>' + str(actual.getPeriodo()) + '</periodos>\n'
            xml += '        <m>' + str(actual.getDimension()) + '</m>\n'
            xml += '        <resultado>' + actual.getEstado() + '</resultado>\n'
            xml += '        <n>' + str(actual.getPeriodoContagiado()) + '</n>\n'
            xml += '    </paciente>\n'

            actual = actual.siguiente

        xml += '</pacientes>'

        documento = 'SalidaXML' + '.xml'
        with open(documento, 'w') as grafica:
            grafica.write(xml)









    def returnPaciente(self, numero):
        actual = self.raiz
        i = 1

        while actual is not None:
            if i == numero:
                return actual.getNombre(), actual.getEdad(), actual.getPeriodo(), actual.getDimension(), actual.getListaCelda(), actual.getListaPatron()
            actual = actual.siguiente
            i += 1

    # FUNCION ELIMINAR