from clases import Celula
import webbrowser
import os

class ListaCelula:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def append(self, data, x, y):
        actual = Celula(data, x, y)

        if self.primero == None:
            self.primero = actual
            self.ultimo = actual 
        
        elif self.primero.siguiente is None:
            self.primero.siguiente = actual
            actual.anterior = self.primero
            self.ultimo = actual
        else:
            self.ultimo.siguiente = actual
            actual.anterior = self.ultimo
            self.ultimo = actual
 
    def mostrarCelulas(self):
        actual = self.primero
        i = 1
        while actual is not None:
            print("Celula " + str(i) + "-> X:" + str(actual.getPosX()) + ", Y:" + str(actual.getPosY()) + " | Dato: " + str(actual.getEstado()))
            i +=1
            actual = actual.siguiente

    def returnCelula(self):
        return self.primero
    
    def graficarLista(self, nombrePaciente, edad, periodo, dimension):
        nodo = self.primero
        i = 1

        graphviz = 'digraph Patron{ \n node[shape =box, width = 1, height = 1]; \n edge[style = invis]; \n ranksep = 0 \n subgraph Cluster_A{ \n label = "' + '| Paciente: '+ nombrePaciente + ' | Edad: ' + str(edad) + ' | Periodo: ' + str(periodo) + ' |' + ' "   \n fontcolor ="black" \n fontsize = 41 \n bgcolor ="#F1DFB2" \n'

        while nodo is not None:
            if nodo.getEstado() == 1:#CONTAGIADAS
                graphviz += 'node{}[fontcolor = "#59A94A" fillcolor = "#59A94A" style = filled]; \n'.format(i)
            if nodo.getEstado() == 0:#SANAS
                graphviz += 'node{}[fontcolor = "#EEAEBA" fillcolor = "#EEAEBA" style = filled]; \n'.format(i)

            nodo = nodo.siguiente
            i += 1

        i = 1
        j = 2

        for h in range((dimension*dimension)-1):
            graphviz += 'node{}->node{} \n'.format(i, j)
            i += 1
            j += 1

        i = 1
        for h in range(dimension):
            graphviz += '{ rank = same'

            for g in range(dimension):
                graphviz += ';node{}'.format(i)
                i += 1
            graphviz += '} \n'

        graphviz += '} \n }'


        documento = 'grafica' + str(nombrePaciente) + '.txt'
        with open(documento, 'w') as grafica:
            grafica.write(graphviz)
        pdf = 'grafica' + str(nombrePaciente) + '.pdf'
        os.system("dot.exe -Tpdf " + documento + " -o " + pdf)
        webbrowser.open(pdf)

##----------------------------------------------------------------
    def __filasArriba(self, fil, col): #entran como int
        actual = self.primero
        fila_arriba = fil - 1

        if fil == 0:
            return None, None, None
        else:
            while int(actual.getPosX()) != fila_arriba:
                actual = actual.siguiente

            while int(actual.getPosX()) == fila_arriba:
                if int(actual.getPosY()) == col:
                    return actual.anterior, actual, actual.siguiente #retorno el NODO
                actual = actual.siguiente

    def __filasAbajo(self, fil, col, dimension):

        actualAbajo = self.primero
        fila_abajo = fil + 1
        
        if fila_abajo == dimension:
            return None, None, None
        else:
            while int(actualAbajo.getPosX()) != fila_abajo:
                actualAbajo = actualAbajo.siguiente

            while int(actualAbajo.getPosX()) == fila_abajo:
                if int(actualAbajo.getPosY()) == col:
                    return actualAbajo.anterior, actualAbajo, actualAbajo.siguiente #retorna el NODO
                actualAbajo = actualAbajo.siguiente

    def __validacionReglaUno(self, raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron):
        contador = 0

        if (arribaNodoAnt is not None) and raiz.getEstado() == arribaNodoAnt.getEstado():
            contador += 1

        if (arribaNodoAct is not None) and raiz.getEstado() == arribaNodoAct.getEstado():
            contador += 1

        if (arribaNodoSig is not None) and raiz.getEstado() == arribaNodoSig.getEstado():
            contador += 1

        if (raizNodoAnt is not None) and str(raiz.getEstado()) == str(raiz.anterior.getEstado()):
            contador += 1

        if (raizNodoSig is not None) and str(raiz.getEstado()) == str(raiz.siguiente.getEstado()):
            contador += 1

        if (abajoNodoAnt is not None) and raiz.getEstado() == abajoNodoAnt.getEstado():
            contador += 1

        if (abajoNodoAct is not None) and raiz.getEstado() == abajoNodoAct.getEstado():
            contador += 1

        if (abajoNodoSig is not None) and raiz.getEstado() == abajoNodoSig.getEstado():
            contador += 1

        if contador == 2 or contador == 3:
            nuevoPatron.append(raiz.getPosX(), raiz.getPosY(), raiz.getEstado())

    def __validacionReglaDos(self, raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron):
        contador = 0

        if (arribaNodoAnt is not None) and arribaNodoAnt.getEstado() == 1:
            contador += 1

        if (arribaNodoAct is not None) and arribaNodoAct.getEstado() == 1:
            contador += 1

        if (arribaNodoSig is not None) and arribaNodoSig.getEstado() == 1:
            contador += 1

        if (raizNodoAnt is not None) and raizNodoAnt.getEstado() == 1:
            contador += 1

        if (raizNodoSig is not None) and raizNodoSig.getEstado() == 1:
            contador += 1

        if (abajoNodoAnt is not None) and abajoNodoAnt.getEstado() == 1:
            contador += 1

        if (abajoNodoAct is not None) and abajoNodoAct.getEstado() == 1:
            contador += 1

        if (abajoNodoSig is not None) and abajoNodoSig.getEstado() == 1:
            contador += 1

        if contador == 3:
            nuevoPatron.append(raiz.getPosX(), raiz.getPosY(), raiz.getEstado())
        
    def __reglaUno(self, nuevoPatron, dimension):
        raiz = self.primero
        
        while raiz is not None:
            if raiz.getEstado() == 1:
                #           -----VALIDACIONES DE LOS 8 CASOS PARA LA MATRIZ-----
                if int(raiz.getPosX()) == 0 and int(raiz.getPosY()) == 0: #Esquina superior izquierda
                    #Las de arriba seran None
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.__filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    raizNodoAnt = None
                    raizNodoSig = raiz.siguiente
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.__filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    abajoNodoAnt = None
                    self.__validacionReglaUno(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

                elif int(raiz.getPosX()) == 0 and int(raiz.getPosY()) == (dimension -1):#Esquina superior derecha
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.__filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    raizNodoSig = None
                    raizNodoAnt = raiz.anterior
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.__filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    abajoNodoSig = None
                    self.__validacionReglaUno(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

                elif int(raiz.getPosX()) == (dimension - 1) and int(raiz.getPosY()) == 0:#Esquina inferior izquierda
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.__filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    arribaNodoAnt = None
                    raizNodoAnt = None
                    raizNodoSig = raiz.siguiente
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.__filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    self.__validacionReglaUno(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

                elif int(raiz.getPosX()) == (dimension -1) and int(raiz.getPosY()) == (dimension -1):#Esquina inferior derecha
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.__filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    arribaNodoSig = None
                    raizNodoSig = None
                    raizNodoAnt = raiz.anterior
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.__filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    self.__validacionReglaUno(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

                elif int(raiz.getPosX()) == 0: #Primera fila cualquier columna
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.__filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    raizNodoAnt = raiz.anterior
                    raizNodoSig = raiz.siguiente
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.__filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    self.__validacionReglaUno(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

                elif int(raiz.getPosY()) == 0: #Lateral columna 0
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.__filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    arribaNodoAnt = None
                    raizNodoAnt = None
                    raizNodoSig = raiz.siguiente
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.__filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    abajoNodoAnt = None
                    self.__validacionReglaUno(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

                elif int(raiz.getPosY()) == (dimension - 1): #Lateral última columna
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.__filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    arribaNodoSig = None
                    raizNodoSig = None
                    raizNodoAnt = raiz.anterior
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.__filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    abajoNodoSig = None
                    self.__validacionReglaUno(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

                elif int(raiz.getPosX()) == (dimension - 1):#Ultima fila cualquier columna
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.__filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    raizNodoSig = raiz.siguiente
                    raizNodoAnt = raiz.anterior
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.__filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    self.__validacionReglaUno(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

                else:#Caso ideal
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.__filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.__filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    raizNodoAnt = raiz.anterior
                    raizNodoSig = raiz.siguiente
                    self.__validacionReglaUno(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)
            raiz = raiz.siguiente
        
    def __reglaDos(self, nuevoPatron, dimension):
        raiz = self.primero

        while raiz is not None:
            if raiz.getEstado() == 0:
                #           -----VALIDACIONES DE LOS 8 CASOS PARA LA MATRIZ-----
                if int(raiz.getPosX()) == 0 and int(raiz.getPosY()) == 0: #Esquina superior izquierda
                    #Las de arriba seran None
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.__filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    raizNodoAnt = None
                    raizNodoSig = raiz.siguiente
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.__filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    abajoNodoAnt = None
                    self.__validacionReglaDos(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

                elif int(raiz.getPosX()) == 0 and int(raiz.getPosY()) == (dimension -1):#Esquina superior derecha
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.__filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    raizNodoSig = None
                    raizNodoAnt = raiz.anterior
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.__filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    abajoNodoSig = None
                    self.__validacionReglaDos(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

                elif int(raiz.getPosX()) == (dimension - 1) and int(raiz.getPosY()) == 0:#Esquina inferior izquierda
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.__filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    arribaNodoAnt = None
                    raizNodoAnt = None
                    raizNodoSig = raiz.siguiente
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.__filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    self.__validacionReglaDos(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

                elif int(raiz.getPosX()) == (dimension -1) and int(raiz.getPosY()) == (dimension -1):#Esquina inferior derecha
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.__filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    arribaNodoSig = None
                    raizNodoSig = None
                    raizNodoAnt = raiz.anterior
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.__filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    self.__validacionReglaDos(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

                elif int(raiz.getPosX()) == 0: #Primera fila cualquier columna
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.__filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    raizNodoAnt = raiz.anterior
                    raizNodoSig = raiz.siguiente
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.__filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    self.__validacionReglaDos(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

                elif int(raiz.getPosY()) == 0: #Lateral columna 0
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.__filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    arribaNodoAnt = None
                    raizNodoAnt = None
                    raizNodoSig = raiz.siguiente
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.__filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    abajoNodoAnt = None
                    self.__validacionReglaDos(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

                elif int(raiz.getPosY()) == (dimension - 1): #Lateral última columna
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.__filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    arribaNodoSig = None
                    raizNodoSig = None
                    raizNodoAnt = raiz.anterior
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.__filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    abajoNodoSig = None
                    self.__validacionReglaDos(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

                elif int(raiz.getPosX()) == (dimension - 1):#Ultima fila cualquier columna
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.__filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    raizNodoSig = raiz.siguiente
                    raizNodoAnt = raiz.anterior
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.__filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    self.__validacionReglaDos(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

                else:#Caso ideal
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.__filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.__filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    raizNodoAnt = raiz.anterior
                    raizNodoSig = raiz.siguiente
                    self.__validacionReglaDos(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)
            raiz = raiz.siguiente

    def comportamientoCelulas(self, nuevoPatron, dimension):

        self.__reglaUno(nuevoPatron, dimension)
        self.__reglaDos(nuevoPatron, dimension)
        nuevoPatron.infectarSanas()
        return nuevoPatron
