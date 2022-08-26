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
            self.ultimo = actual
        else:
            self.ultimo.siguiente = actual
            self.ultimo = actual

    # POSIBLEMENTE SE BORRARA, DESCARTADA        
    def appendInfectada(self, x, y):
        actual = self.primero #LISTA
        
        while actual is not None:
            if(int(actual.getPosX()) == int(x)) and (int(actual.getPosY()) == int(y)):
                actual.setEstado("X")
            actual = actual.siguiente

 
    def mostrarCelulas(self):
        actual = self.primero
        i = 1
        while actual is not None:
            print("Celula " + str(i) + "-> X:" + str(actual.getPosX()) + ", Y:" + str(actual.getPosY()) + " | Dato: " + actual.getEstado())
            i +=1
            actual = actual.siguiente

    #def mostarCelulasContagiadas(self):
     #   actual = self.primero
      #  i = 1
       # while actual is not None:
        #    if actual.getEstado() == "X":
         #       return actual.getPosX(), actual.getPosY(), actual.getEstado()
          #      i += 1#NECESITO RETORNAR EL NODO
           # actual = actual.siguiente

    def returnCelula(self):
        return self.primero
    
    def graficarLista(self, nombrePaciente, edad, dimension):
        nodo = self.primero
        i = 1

        graphviz = 'digraph Patron{ \n node[shape =box, width = 2, height = 2]; \n ranksep = 0 \n nodesep = 0.1 \n subgraph Cluster_A{ \n label = "' + 'Paciente: '+ nombrePaciente + '| edad: ' + str(edad) + '"   \n fontcolor ="#FFFFFF" \n fontsize = 30 \n bgcolor ="#20B2AA" \n'

        while nodo is not None:
            if nodo.getEstado().lower() == "X".lower():
                graphviz += 'node{}[fontcolor = "#FFFFFF" fillcolor = "yellow" style = filled]; \n'.format(i)
            if nodo.getEstado().lower() == "O".lower():
                graphviz += 'node{}[fillcolor = "blue" style = filled]; \n'.format(i)

            nodo = nodo.siguiente
            i += 1

        i = 1
        j = 1

        for h in range((dimension*dimension)-1):
            graphviz += 'node{}->node{} \n'.format(i, j)
            i += 1
            j += 1
        
        # Conección de cabezales
   








        # ESTE ES EL CASO TOMANDO COMO EJEMPLO
        #UNA MATRIZ
        #               3X3 -> 9 NODOS

        primero = 1

        actual = 1
        z = dimension

        for actual in range((dimension*dimension)-1): # range(8)

            if int(actual) == z: # Si (9) == (9)

                z += dimension # z=9+3= 12

                head = actual + 1 # head = 10
                # primero = 7
                graphviz += 'node{}->node{}\n'.format(primero, head)
                # node7 -> node10

                actual = head # actual = 10
                primero = head # primero = 10

            actual += 1 # actual = 9
        
        #1RA. -> z = 6, head = 4, primero = 4, actual = variable
        #2DA. -> z = 9, head = 7, primero = 7, actual = variable
        #3RA. -> z = 9, head = 7, primero = 7, actual = variable





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


    # GETTERS
    def getPosX(self, numero):
        actual = self.primero
        i = 1

        while actual is not None:
            if i == numero:
                return actual.getPosX()
            actual = actual.siguiente
            i += 1

    def getPosY(self, numero):
        actual = self.primero
        i = 1

        while actual is not None:
            if i == numero:
                return actual.getPosY()
            actual = actual.siguiente
            i += 1

    def getEstado(self, numero):
        actual = self.primero
        i = 1

        while actual is not None:
            if i == numero:
                return actual.getEstado()
            actual = actual.siguiente
            i += 1
