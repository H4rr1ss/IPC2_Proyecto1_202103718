from clases import Celula
from lista_patrones import ListaPatron
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
    
    def graficarLista(self, nombrePaciente, edad, dimension):
        nodo = self.primero
        i = 1

        graphviz = 'digraph Patron{ \n node[shape =box, width = 1, height = 1]; \n ranksep = 0 \n subgraph Cluster_A{ \n label = "' + 'Paciente: '+ nombrePaciente + ' | edad: ' + str(edad) + '"   \n fontcolor ="#FFFFFF" \n fontsize = 40 \n bgcolor ="#20B2AA" \n'

        while nodo is not None:
            if nodo.getEstado() == 1:
                graphviz += 'node{}[fontcolor = "#FFFFFF" fillcolor = "#C2458F" style = filled]; \n'.format(i)
            if nodo.getEstado() == 0:
                graphviz += 'node{}[fillcolor = "#E6BF9C" style = filled]; \n'.format(i)

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




    def validacionReglaUno(self, raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron):
        contador = 0


        if (arribaNodoAnt is not None) and raiz.getEstado() == arribaNodoAnt.getEstado():
            contador += 1

        if (arribaNodoAct is not None) and raiz.getEstado() == arribaNodoAct.getEstado():
            contador += 1

        if (arribaNodoSig is not None) and raiz.getEstado() == arribaNodoSig.getEstado():
            contador += 1






        if raizNodoAnt is not None:
            if str(raiz.getEstado()) == str(raiz.anterior.getEstado()):
                contador += 1

        if raizNodoSig is not None:
            if str(raiz.getEstado()) == str(raiz.siguiente.getEstado()):
                contador += 1








        if (abajoNodoAnt is not None) and raiz.getEstado() == abajoNodoAnt.getEstado():
            contador += 1

        if (abajoNodoAct is not None) and raiz.getEstado() == abajoNodoAct.getEstado():
            contador += 1

        if (abajoNodoSig is not None) and raiz.getEstado() == abajoNodoSig.getEstado():
            contador += 1

        if contador == 2 or contador == 3:
            print(" ----- INFECTADAS NUEVAS ----")
            nuevoPatron.append(raiz.getPosX(), raiz.getPosY(), raiz.getEstado())
        # SINO ES IGUAL A 2 O 3 ENTONCES SE SANA

    def reglaUno(self, nuevoPatron, dimension):
        raiz = self.primero
        
        while raiz is not None:
            if raiz.getEstado() == 1:
                # CON ESTO OBTENGO EL VALOR DE LAS POSICIONES
                # ANTERIORES = NODO A LA IZQUIERDA DE LA RAIZ
                # SIGUIENTES = NODO A LA DERECHA DE LA RAIZ

                #           VALIDACIONES DE LOS 8 CASOS PARA LA MATRIZ
                if int(raiz.getPosX()) == 0 and int(raiz.getPosY()) == 0: #Esquina superior izquierda
                    #Las de arriba seran None
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    raizNodoAnt = None
                    raizNodoSig = raiz.siguiente
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    abajoNodoAnt = None
                    self.validacionReglaUno(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

                elif int(raiz.getPosX()) == 0 and int(raiz.getPosY()) == (dimension -1):#Esquina superior derecha
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    raizNodoSig = None
                    raizNodoAnt = raiz.anterior
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    abajoNodoSig = None
                    self.validacionReglaUno(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

                elif int(raiz.getPosX()) == (dimension - 1) and int(raiz.getPosY()) == 0:#Esquina inferior izquierda
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    arribaNodoAnt = None
                    raizNodoAnt = None
                    raizNodoSig = raiz.siguiente
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    self.validacionReglaUno(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

                elif int(raiz.getPosX()) == (dimension -1) and int(raiz.getPosY()) == (dimension -1):#Esquina inferior derecha
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    arribaNodoSig = None
                    raizNodoSig = None
                    raizNodoAnt = raiz.anterior
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    self.validacionReglaUno(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

                elif int(raiz.getPosX()) == 0: #Primera fila cualquier columna
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    raizNodoAnt = raiz.anterior
                    raizNodoSig = raiz.siguiente
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    self.validacionReglaUno(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

                elif int(raiz.getPosY()) == 0: #Lateral columna 0
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    arribaNodoAnt = None
                    raizNodoAnt = None
                    raizNodoSig = raiz.siguiente
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    abajoNodoAnt = None
                    self.validacionReglaUno(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

                elif int(raiz.getPosY()) == (dimension - 1): #Lateral última columna
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    arribaNodoSig = None
                    raizNodoSig = None
                    raizNodoAnt = raiz.anterior
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    abajoNodoSig = None
                    self.validacionReglaUno(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

                elif int(raiz.getPosX()) == (dimension - 1):#Ultima fila cualquier columna
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    raizNodoSig = raiz.siguiente
                    raizNodoAnt = raiz.anterior
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    self.validacionReglaUno(raizNodoAnt, raizNodoSig, raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

                else:#Caso ideal
                    # NODOS DE ARRIBA Y NODOS DE ABAJO DE LA CELULA CONTAGIADA
                    arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                    abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()), dimension)
                    
                    #VALIDACION DE REGLA 1 ----------
                    self.validacionReglaUno(raiz, arribaNodoAnt, arribaNodoAct, arribaNodoSig, abajoNodoAnt, abajoNodoAct, abajoNodoSig, nuevoPatron)

            raiz = raiz.siguiente
        



    def reglaDos(self, nuevoPatron):
        raiz = self.primero

        while raiz is not None:
            if raiz.getEstado() == 0:
                arribaNodoAnt, arribaNodoAct, arribaNodoSig = self.filasArriba(int(raiz.getPosX()), int(raiz.getPosY()))
                # Si no existen arriba de la analizada devolverá None

                abajoNodoAnt, abajoNodoAct, abajoNodoSig = self.filasAbajo(int(raiz.getPosX()), int(raiz.getPosY()))



            raiz = raiz.siguiente


    def filasArriba(self, fil, col): #entran como int
        actual = self.primero
        fila_arriba = fil - 1

        if fil == 0:
            return None, None, None
        else:
            while int(actual.getPosX()) != fila_arriba:
                actual = actual.siguiente

            while int(actual.getPosX()) == fila_arriba:
                if int(actual.getPosY()) == col:
                    print("----- Filas arriba -----")
                    print("anterior -> Y: " + str(actual.anterior.getPosY()))
                    print("actual -> Y: " + str(actual.getPosY()))
                    print("siguiente -> Y: " + str(actual.siguiente.getPosY()))

                    return actual.anterior, actual, actual.siguiente #retorno el NODO
                actual = actual.siguiente

    # PENDIENTE VALIDACION SI FIL ES LA ULTIMA FILA DE LA MATRIZ
    def filasAbajo(self, fil, col, dimension):

        actualAbajo = self.primero
        fila_abajo = fil + 1
        
        if fila_abajo == dimension:
            return None, None, None
        else:
            while int(actualAbajo.getPosX()) != fila_abajo:
                actualAbajo = actualAbajo.siguiente

            while int(actualAbajo.getPosX()) == fila_abajo:
                if int(actualAbajo.getPosY()) == col:
                    print("\n----- Filas abajo -----")
                    print("anterior -> Y: " + str(actualAbajo.anterior.getPosY()))
                    print("actual -> Y: " + str(actualAbajo.getPosY()))
                    print("siguiente -> Y: " + str(actualAbajo.siguiente.getPosY()))

                    return actualAbajo.anterior, actualAbajo, actualAbajo.siguiente #retorna el NODO
                actualAbajo = actualAbajo.siguiente
